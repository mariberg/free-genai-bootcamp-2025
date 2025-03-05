## Generating the Next.js app

The Next.js application was created using V0.dev with the prompt ``prompt.md``-file. 

The app has a simple UI that allows user in input 'thematic category' and click 'generate vocabulary'. This will call the Groq.com API, a service that provides extremely fast access to large language models (LLMs), which will use the selected LLM model to create a list of 5 vocabulary items and return that to the frontend.

The Next.js app created by V0.dev was mostly functional, although some slight modifications were neeeded 
especially to ensure the returned JSON is formatted correctly. 


## Running the application locally

**1. Set up your environment:**

Create an `.env` file: In the root directory of your project, create a new file named `.env`.
Add your Groq API key: Inside the `.env` file, add your Groq API key in the following format:
    ```
    GROQ_API_KEY=your_actual_api_key
    ```

**2. Install dependencies (if you haven't already):**

Open your terminal and navigate to your project's root directory.
Run `npm install` to install all the necessary dependencies.

**3. Start the development server:**

In your terminal, run `npm run dev`.
This will start the Next.js development server. You should see a message indicating that the server is running, usually on `localhost:3000`.

**4. Access the application:**

Open your web browser and navigate to `http://localhost:3000`.
You should now be able to interact with the application.