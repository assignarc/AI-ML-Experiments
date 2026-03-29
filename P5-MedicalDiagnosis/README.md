# P5-MedicalDiagnosis
> Learning through experiments and data!

## What was the goal?
Medical professionals face severe information overload when trying to quickly locate specific protocols or diagnostic criteria in massive encyclopedias (like the Merck Manuals) during high-stakes situations. Trying to solve this by building a highly-educated medical search engine that:

## Why does this matter? (Business Context)
The healthcare industry is rapidly evolving, with professionals facing increasing challenges in managing vast volumes of medical data while delivering accurate and timely diagnoses. The need for quick access to comprehensive, reliable, and up-to-date medical knowledge is critical for improving patient outcomes and ensuring informed decision-making in a fast-paced environment.

## Tech Stack
### Packages Needed For This Module:
- `huggingface_hub`
- `langchain_community`
- `langchain_text_splitters`
- `llama_cpp`
- `pandas`
- `tiktoken`


- **Python 3.10+**
- **Langchain** - RAG orchestration
- **Llama.cpp** - Local LLM inference (Mistral GGUF)
- **Hugging Face Hub** - Sentence Embeddings
- **ChromaDB** - Vector Database
- **Pandas / Jupyter** - Data analysis and execution

---

## Stuff I used (Libraries)
IPython, huggingface_hub, langchain_community, langchain_text_splitters, llama_cpp, pandas, tiktoken

## What did I notice?
The **Merck Manuals** are medical references published by the American pharmaceutical company Merck & Co., that cover a wide range of medical topics, including disorders, tests, diagnoses, and drugs. The manuals have been published since 1899, when Merck & Co. was still a subsidiary of the German company Merck.

## What I Found (Insights)
### Key Takeaways for the Business

## What I Learned
- Setting up local LLMs with `llama-cpp` is super powerful (and saves API costs).
- Langchain's text splitters require a lot of testing to get the overlaps right.
- You absolutely must use programmatic evaluations (like the Groundedness prompt) instead of manually reading 50 responses (took way longer than expected otherwise).

---

## How did it do? (Results)
Placeholder: Final model scores or summary.

## Wrapping up
Placeholder: Final thoughts.

