## Generating the next app

The Next.js application was created using V0.dev with the prompt ``prompt.md``-file. 

The app has a simple UI that allows user in input 'thematic category' and click 'generate vocabulary'. This will call the Groq.com API, a service that provides extremely fast access to large language models (LLMs), which will use the selected LLM model to create a list of 5 vocabulary items and return that to the frontend.

The Next.js app created by V0.dev was mostly functional, although some slight modifications were neeeded 
especially to ensure the returned JSON is formatted correctly. 