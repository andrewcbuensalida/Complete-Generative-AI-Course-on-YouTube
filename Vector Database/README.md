Following https://docs.smith.langchain.com/tutorials/Developers/observability to add langsmith


Following https://www.youtube.com/watch?v=8KrTO9bS91s
Except that I'm not using google colab. I'm using vs code jupyter notebook.

TODO
- make an outline for the presentation
- agentic ai, maybe using "langchain tools" or langgraphs. langchain agents basically making llm's take an input and decide which tool to use. tools are basically functions like triggering an aws lambda or commenting on a github PR or sending an email.
- implement chat history so there's memory of previous questions
- deploy to hugging face using fastapi or gradio, flask, django OR langserve
- llama index
- compare speed of CRUD chroma vs pinecone
- compare cost of chroma vs pinecone
- compare top k recall, aka correctness
- try different models other than openai, maybe using openrouter. Or local llms like privategpt or gpt4all
- computer vision
- speech to text
- is it possible to have multiple correct answers when evaluating experiments
- is it possible to have a non binary score when evaluating. maybe have a different embedding other than openai.


DONE
- when running qa.invoke(query), need to see what chunks get passed to the openai. something about langsmith?
- try to invoke each step of qa.invoke()
- get metadata from docsearch.similarity_search. Tutorial was wrong. It was upserting to the index without metadata.
- optimize conversion of pdf to text so it is more readable for the model or getting raw text. This might not be needed since openai seems to be able to understand "August 2017\xa0-\xa0February 2020" even if there are a lot of escape characters