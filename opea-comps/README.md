## Running Ollama Third-Party Service

### Choosing a model

You can get the model_id that Ollama will launch from the [Ollama Library](https://ollama.com/library)

eg. https://ollama.com/library/llama3.2


### Getting the host IP

Use this commadn to find the ip address of your computer as that is needed as host_ip:

```sh
ifconfig
```


NO_PROXY=localhost LLM_ENDPOINT_PORT=8008 LLM_MODEL_ID="llama3.2:ib"
host_ip=192.168.1.121 docker compose up


### Ollama API

Once the server is running in a container, we can make API calls to the Ollama API

https://github.com/ollala/ollama/blob/main/docs/api.md

### Download (pull) a model

curl http://localhost:11434/api/pull -d '{
    "model": "llama3.2:1b"
}'

### Generate a request

curl http://localhost:8008/api/generate -d '{
    "model": "llama3.2:1b",
    "prompt": "Why is the sky blue?"
}'

This command is downloading everything into the container.


### Technical uncertainty

Question: Does bridge mode mean we can only access Ollama API with another model in the docker compose?

Answers: No, the host machine will be able to access it

Q: Which port is being mapped 8008 -> 11434

A: In this case 8008 is the port that host machine will access. The other in the guest port (the port of the service inside)

Q: If we pass the LLM_MODEL_ID to the Ollama server, will it downlaod the model whe on start?

A: It does not appear so. The Ollama CLI might be running multiple APIs so you need to call the pull api before trying to 
generate text. 

Q: will the model be downloaded in the container? Does that mean the ml model will be deleted when the container stops running?

A: The model will download into the container, and vanich when the container stops running. You need to mount a local drive
and there is probably more work to be done. 

Q: For the LLM service which can do text-generation, it suggests it will only work with TGI/vLLM and all you have to do is 
to have it running. Does TGI and vLLM have a standardised API or is there code to detect which one is running? Do we 
really have to use Xeon or Guadi processor?

vLLM, TGI and Ollama all offer APIs with OpenAI compatibility, so in theory they should be interchangeable. 