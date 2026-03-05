# 🤖 LLM Prompt Engineering (W18)

> **Learning Module:** Learning how to talk to Large Language Models (LLMs) to get out exactly what you want.

---

## What's this about?

Everyone knows how to use ChatGPT, but *engineering* a prompt for a repeatable, programmatic, enterprise-grade AI pipeline is entirely different. This week is all about controlling the chaos of generative AI.

### The Goal

LLMs naturally want to ramble. The objective here is to:

- Create rigid `System Prompts` that define the AI's persona and constraints.
- Inject dynamic variables into `User Prompts`.
- Force the model to output structured data (like JSON) instead of blocks of text.
- Tune generation parameters to control creativity vs. factual recall.

---

## The Concepts

### Key LLM Hyperparameters

| Parameter | What it does | Example Use Case |
| ----------------------- | -------------------------------- | ----------- |
| Temperature (0.0 to 1.0) | Controls randomness/creativity | 0.0 for code/facts, 0.8 for storytelling |
| Top-P (Nucleus Sampling) | Cuts off lower-probability words | P=0.5 limits the vocabulary strongly |
| Top-K | Only considers the top K tokens | K=10 for very strict constraint |
| Max Tokens | Hard limit on response length | Prevents infinite rambling |
| Stop Sequences | Stops generating immediately | Tell it to stop on `\n\n` |

---

## What I'm trying to do

### 1. Zero-Shot vs Few-Shot Prompting

- **Zero-Shot:** Giving the model a task with no examples.
- **Few-Shot:** Passing 3-4 examples of identical input/output inside the prompt so the model catches the pattern.

### 2. Output Formatting

- Asking the model to "Return only a valid JSON array" and debugging when it hallucinates markdown code blocks around it (Trial and error - lots of error!).

### 3. API Integration

- Loading Langchain or OpenAI libraries, passing the prompt payload, and extracting the text from the response object.

---

## What I Found

- Prompting is highly iterative. If a model fails to return the right data, 90% of the time your prompt was too vague.
- Changing `temperature` from 0.7 down to 0.1 instantly fixes formatting bugs when doing data extraction.

---

## Tech Stack
### Packages Needed For This Module:
- `huggingface_hub`
- `llama_cpp`
- `numpy`
- `pandas`
- `torch`
- `tqdm`
- `transformers`


- **Python 3.8+**
- **Langchain** - PromptTemplate wrappers
- **OpenAI API / Llama.cpp** - The actual LLM engines
- **JSON** - Parsing the outputs

---

## What I Learned

- You have to be incredibly explicit with LLMs. Tell them exactly what to do, what *not* to do, and how to format it.
- "You are a helpful assistant" is a terrible system prompt for production. Better: "You are a strict data extraction tool that only returns valid JSON and never apologizes."

---

## 🔗 Links

- [Back to Main Repository](../)
- [W19: Retrieval Augmented Generation](../W19-RetrievalAugmentedGeneration-RAG)

---

**Project Date:** 2024  
**Domain:** Generative AI & Prompt Engineering
