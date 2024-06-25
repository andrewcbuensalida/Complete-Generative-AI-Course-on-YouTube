Following https://www.youtube.com/watch?v=8KrTO9bS91s
Except that I'm not using google colab. I'm using vs code jupyter notebook.

TODO
- try to invoke each step of qa.invoke()
- when running qa.invoke(query), need to see what chunks get passed to the openai
- deploy to hugging face using fastapi or gradio, flask, django
- llama index
- compare speed of CRUD chroma vs pinecone
- compare cost of chroma vs pinecone
- compare top k recall, aka correctness
- optimize conversion of pdf to text so it is more readable for the model or getting raw text
- try different models other than openai, maybe using openrouter


DONE
- get metadata from docsearch.similarity_search. Tutorial was wrong. It was upserting to the index without metadata.