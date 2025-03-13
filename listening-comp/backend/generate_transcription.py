import boto3
import time
import os
from pytube import YouTube
from moviepy.editor import AudioFileClip
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AWS credentials
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = "us-east-1"
S3_BUCKET_NAME = "videobucket1303"

# Initialize AWS clients
s3_client = boto3.client('s3', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
transcribe_client = boto3.client('transcribe', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def download_audio_from_youtube(video_url: str, output_path: str) -> str:
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download(output_path=output_path)
    return audio_file

def upload_to_s3(file_path: str, bucket_name: str, object_name: str) -> str:
    s3_client.upload_file(file_path, bucket_name, object_name)
    s3_url = f"s3://{bucket_name}/{object_name}"
    return s3_url

def transcribe_audio(s3_url: str, job_name: str) -> str:
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': s3_url},
        MediaFormat='mp4',
        IdentifyLanguage=True  # Enable automatic language identification
    )
    
    while True:
        status = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Waiting for transcription to complete...")
        time.sleep(10)
    
    if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        transcript_url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
        return transcript_url
    else:
        raise Exception("Transcription job failed")

def main(video_url: str):
    # Step 1: Download audio from YouTube video
    audio_file = download_audio_from_youtube(video_url, output_path=".")
    
    # Step 2: Upload audio to S3
    s3_url = upload_to_s3(audio_file, S3_BUCKET_NAME, os.path.basename(audio_file))
    
    # Step 3: Use Amazon Transcribe to generate transcription
    job_name = f"transcription-job-{int(time.time())}"
    transcript_url = transcribe_audio(s3_url, job_name)
    
    print(f"Transcription completed. Transcript URL: {transcript_url}")

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=sY7L5cfCWno&list=PLkGU7DnOLgRMl-h4NxxrGbK-UdZHIXzKQ"
    main(video_url)