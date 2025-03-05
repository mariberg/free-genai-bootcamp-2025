## Prompt

Give me please vocabulary language importer where we have a text field that allows us to import a thematic category for the generation of language vocabulary.

When submitting that text field, it should hit an api endpoint (api route in app router) to invoke an LLM chat completions in Groq (LLM) on the server-side and then pass that information back to the front-end. 

I has to create a structure json output like this example:
```
  {
    "latin_spelling": "mlih",
    "origin_language": "Arabic",
    "arabic_spelling": "مليح",
    "english": "good"
  },
```
It should return raw json only and nothing else.

The json that is outputted back to the front-end should be copy-able. So it should be sent to an input field and there should be a copy button so that it can be copies to the clipboard and that should give an alert that it was copied to the user's clipboard.

The app shiould use app router and the latest version of next.js and the llm calls should run in an api route on the server-side. 