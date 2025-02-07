## Functional Requirements

The company wants to invest in owning their infrastructure.
The reason is because they there is a concern about the privacy of user data and also a concern that the cost of managed services for GenAI will be too high.

They want to invest an AI PC where they can afford spend of 10-15K
They have 300 active students, and students are located within the city of London.

## Assumptions

We are assuming that the Open-source LLMs that we choose will be powerful enough to run on hardware with an investment of 10-15K.

We're just going to hook up a single server in the office to the internet and this should give enough bandwidth to serve the 300 students.

## Data Strategy

There is a concern of copyrighted materials, so we must purchase and supply materials and store them for access in our database. This is why we would use a vector database that RAG will access. There will be a consideration whether RAG will
be accessing only the vector database or internet as well.

## Considerations

We're considering using IBM Granite because its a truly open-source model with training data that is traceable so we can avoid any copyright issues and we are able to know what is going on in the model.

https://huggingface.co/ibm-granite