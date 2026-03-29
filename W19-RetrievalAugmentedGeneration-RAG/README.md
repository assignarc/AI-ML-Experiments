# W19-RetrievalAugmentedGeneration-RAG
> Learning through experiments and data!

## What was the goal?
- Parse and split large PDFs or text files into digestible chunks.
- Convert text into massive arrays of numbers (Embeddings).
- Store them in a Vector Database.
- Retrieve the most statistically similar text to the user's question, and force the LLM to answer *only* using that text.

## Why does this matter? (Business Context)
Placeholder: Why does this analysis matter for a business?

## Tech Stack
### Packages Needed For This Module:
- `huggingface_hub`
- `langchain_community`
- `langchain_text_splitters`
- `llama_cpp`
- `pandas`
- `tiktoken`


- **Python 3.8+**
- **Langchain** - The framework gluing this all together.
- **Hugging Face Hub** - Embedding algorithms (all-MiniLM-L6-v2 is a favorite).
- **ChromaDB** - A fast, local vector database SQLite engine.
- **Llama.cpp / OpenAI API** - Generative model for finalizing the answer.

---

## Stuff I used (Libraries)
Standard Libraries

## What did I notice?
Placeholder: What interesting things popped up in the data?

## What I Found (Insights)
Placeholder: What did you find out?

## What I Learned
- Vector DBs are basically highly specialized search engines.
- RAG is the ultimate cure for LLM hallucinations. If the vector search doesn't find the answer in the context doc, you can strictly instruct the LLM to say "I don't know" instead of making things up.
- Setting up RAG pipelines requires balancing token limits—you can't retrieve 100 chunks because the LLM context limits will max out.

---

## How did it do? (Results)
Placeholder: Final model scores or summary.

## Wrapping up
Placeholder: Final thoughts.

## Exercises
- [Problem Statement](./AppleHBR/README.md)
- [Retrieval-Augmented Generation (RAG)](./DeloitteArticle/README.md)

