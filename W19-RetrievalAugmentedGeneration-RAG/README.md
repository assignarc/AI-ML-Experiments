# 🧠 Retrieval-Augmented Generation (W19)

> **Learning Module:** Giving LLMs memory by hooking them up to vector databases so they stop hallucinating facts.

---

## What's this about?

Large Language Models (LLMs) are frozen in time—they only know what they were trained on. If you ask them about proprietary company documents or very specific, recent data, they either hallucinate or say "I don't know." **Retrieval-Augmented Generation (RAG)** fixes this by searching your custom documents *first*, and feeding them to the LLM to read before answering.

### The Goal

- Parse and split large PDFs or text files into digestible chunks.
- Convert text into massive arrays of numbers (Embeddings).
- Store them in a Vector Database.
- Retrieve the most statistically similar text to the user's question, and force the LLM to answer *only* using that text.

---

## The RAG Pipeline

### Core Architecture Components

| Step | Technique | Purpose |
| ----------------------- | -------------------------------- | ----------- |
| 1. Ingestion | Loaders (PyPDF, CSV, Text) | Extract raw strings from messy files |
| 2. Splitting | RecursiveCharacterTextSplitter | Break massive texts into 1000-character chunks with overlap |
| 3. Embedding | Sentence Transformers | Convert text chunks into dense vectors (e.g., 384 dimensions) |
| 4. Storage | ChromaDB, FAISS | Store vectors for lightning-fast similarity search |
| 5. Retrieval | Cosine Similarity Search | Grab the top K chunks most related to the user query |
| 6. Generation | LLM Prompt Injection | "Answer this using ONLY the following context: [Chunks]" |

---

## What I'm trying to do

### Build the Knowledge Base
- Load up complex documents.
- Split them carefully. If you break a sentence in half, semantic meaning is ruined (making features that actually help).

### Vector Search
- Use HuggingFace embeddings to vectorize everything.
- Calculate distance metrics to find exactly which paragraph holds the answer to a question.

### The Agentic Output
- Take the retrieved paragraphs, paste them into a system prompt, and see if the LLM can synthesize a smart response.

---

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

## What I Found

- Embedding models matter immensely. If the embedding is weak, your vector search pulls irrelevant paragraphs, and the LLM response is useless.
- `chunk_overlap` is crucial. If you don't overlap your splits, you might chop a critical definition in half right across two separate chunks!

---

## What I Learned

- Vector DBs are basically highly specialized search engines.
- RAG is the ultimate cure for LLM hallucinations. If the vector search doesn't find the answer in the context doc, you can strictly instruct the LLM to say "I don't know" instead of making things up.
- Setting up RAG pipelines requires balancing token limits—you can't retrieve 100 chunks because the LLM context limits will max out.

---

## 🔗 Links

- [Back to Main Repository](../)
- [P4: Applied Medical RAG System](../P4-MedicalDiagnosis)

---

**Project Date:** 2024  
**Domain:** Generative AI Architecture
