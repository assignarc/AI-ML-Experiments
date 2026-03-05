# 🏥 Medical Diagnosis RAG System

> **Applied AI Project:** Building a Retrieval-Augmented Generation (RAG) pipeline to cut through information overload and provide immediate, grounded clinical answers.

---

## What's this project about?

**Domain:** Healthcare AI & NLP  
**Project Type:** Retrieval-Augmented Generation (RAG)  
**Difficulty Level:** Advanced

### The Goal

Medical professionals face severe information overload when trying to quickly locate specific protocols or diagnostic criteria in massive encyclopedias (like the Merck Manuals) during high-stakes situations. Trying to solve this by building a highly-educated medical search engine that:

- Retrieves the exact relevant context from 4,000+ pages of dense text.
- Standardizes care practices via automated, accurate LLM extraction.
- Prevents AI hallucinations by strictly evaluating groundedness.

---

## The Data

**Source:** Dense medical PDFs (Merck Manuals or equivalent)  
**Format:** Unstructured text

### Data Pipeline

| Component | Description | Tech Used |
| ----------------------- | -------------------------------- | ----------- |
| Document Loader | Parses raw PDF pages | PyMuPDFLoader |
| Chunking | Splits text without breaking logic | RecursiveCharacterTextSplitter |
| Embedding | Dense vector representation | SentenceTransformer/HuggingFace |
| Vector DB | Local storage and semantic search | Chroma |

---

## What I'm trying to do

### 1. Base LLM Setup & Prompting

- Load local GGUF models (Mistral-7B).
- Write custom system prompts dictating a professional medical tone.

### 2. Information Retrieval (RAG)

- Extract, chunk, and embed thousands of pages of medical PDFs.
- Query the vector database to retrieve the top $K$ most relevant chunks.

### 3. Tuning & Evaluation

- Run combinations of LLM temperatures and context windows (RAG Tuning).
- Implement an automated LLM-as-a-judge system to score responses on:
  - **Groundedness**: Did it hallucinate or stick to the PDF?
  - **Relevance**: Did it actually answer the user's question?

---

## Quick Numbers & Tuning Runs

Tested across 10 different parameter combinations (GridSearch for LLMs, essentially!). 

**Key Runs Analyzed:**
- `1.TEST`: Baseline LLM knowledge.
- `2.PROMPT_ENG_T_0.7`: Tested high temperature creativity.
- `4.RAG_TUNING_T_0.5`: The sweet spot for RAG extraction.
- `4b.RAG_TUNING_K_5`: Strict semantic search, pulling only 5 dense chunks.
- `5.GROUND_RELEVANCE`: LLM evaluation metrics.

---

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

## 📁 Project Structure

```
P4-MedicalDiagnosis/
├── NLP_RAG_Project_Notebook.ipynb
├── req1.txt
├── medical_db/ (Chroma vector store)
└── README.md (this file)
```

---

## Running This

### You'll need:

```bash
# Install the exact packages required
pip install -r req1.txt
# Note: Llama-cpp-python installation might need CMAKE/metal flags for macOS!
```

### Run the Analysis

```bash
# Launch Jupyter Notebook
jupyter notebook NLP_RAG_Project_Notebook.ipynb
```

---

## What I Found

### Hallucinations are Solvable
Going from a raw base LLM to a RAG pipeline entirely stripped away random "AI noise." The system flawlessly diagnosed symptoms (like appendicitis and alopecia) directly from the text.

### Parameter Tuning Matters
Retrieving 20 chunks caused some context limits to bloat, but tuning down to `K=5` and `Temperature=0.5` made the answers sharp, fast, and completely grounded.

### Business Impact
This prototype actually proves we can mitigate information overload for clinicians, guaranteeing they pull from a verified, standard bedrock of knowledge instead of Googling.

---

## What I Learned

- Setting up local LLMs with `llama-cpp` is super powerful (and saves API costs).
- Langchain's text splitters require a lot of testing to get the overlaps right.
- You absolutely must use programmatic evaluations (like the Groundedness prompt) instead of manually reading 50 responses (took way longer than expected otherwise).

---

## 🔗 Links

- [Back to Main Repository](../)
- [View Full Code Notebook](./NLP_RAG_Project_Notebook.ipynb)

---

**Project Type:** NLP & RAG Pipeline  
**Domain:** Healthcare AI
