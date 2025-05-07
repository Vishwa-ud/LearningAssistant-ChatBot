# 🤖 LearningAssistant- CHATBOT

**LearningAssistant** is a smart chatbot powered by a Large Language Model (LLM) that allows students to ask questions based on CTSE (Current Trends in Software Engineering) lecture notes. This project was developed as part of an AI/ML Semester 1 (2025) assignment to demonstrate how LLMs can support education by answering subject-specific queries inside a Jupyter Notebook.

---

## 📌 Project Overview

- **🎯 Objective**: Build a chatbot that can answer CTSE lecture note-based questions using LLMs.
- **🧠 Focus**: Natural language understanding and context-aware response generation.
- **💻 Environment**: Implemented entirely inside a Jupyter Notebook for interactivity and easy experimentation.
- **📚 Input**: CTSE lecture notes (text format).
- **🔍 Output**: Answers to user questions based on those notes.

---

## 🚀 Features

- 📘 Ask context-rich questions about CTSE topics.
- 🧠 Powered by a pre-trained LLM (e.g., GPT or Hugging Face model).
- 📎 Context-aware responses from provided notes.
- 🧩 Easy to extend with additional subjects or notes.
- 🎓 Ideal for exam prep, concept clarification, and learning assistance.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Jupyter Notebook**
- **LLM Platform**: OpenAI GPT / Hugging Face Transformers
- **(Optional)**: FAISS or ChromaDB for vector-based retrieval
- **LangChain** *(optional, if used for chaining LLM with retrieval)*

---

## 📁 File Structure
ctse-chatbot/
│
├── data/
│   ├── ctse_lecture_notes.pdf       # or pptx files
│   └── sample_slides.pptx
│
├── notebooks/
│   ├── 1_data_ingestion.ipynb       # Load & preprocess lecture notes
│   ├── 2_embed_store.ipynb          # Embed text and store in vector DB
│   ├── 3_llm_setup_rag.ipynb        # LLM (Mistral) + RAG integration
│   ├── 4_chainlit_app.ipynb         # Chainlit chatbot interface
│   └── 5_justification_and_prompts.ipynb  # LLM + Approach justification & prompt log
│
├── models/
│   └── mistral-7b-instruct-v0.1.Q4_K_M.gguf  # Your local LLM file
│
├── vectorstore/
│   └── ctse_faiss_index/            # FAISS or other vector DB
│
├── chainlit_app/
│   └── app.py                       # Chainlit frontend
│
├── your_rag_module.py               # Python module to reuse RAG code in Chainlit
├── requirements.txt                 # All dependencies
└── README.md                        # Project overview


## Set up
python -m venv .venv
.venv\Scripts\activate  -activate vertual environment
pip install -r requirements.txt


## Vector database (Qdrant)

### How to run qdrant docker
```
docker pull qdrant/qdrant
```

### Run
```
docker run -p 6333:6333 -p 6334:6334 -v "${PWD}/qdrant_storage:/qdrant/storage:z" qdrant/qdrant
```

## Prompt
You said:
my task is Develop a simple chatbot using an LLM to answer questions based on CTSE(current trends in software enginerring ) lecture notes. The chatbot should be implemented inside Jupyter Notebook(.ipynb) use proper file structure can you more jupiter notebook files. Criteria Working Jupyter Notebook Chatbot - Robust, smooth and insightful responses Justification of LLM Choice - Strong, thorough and critical reasoning Justification of Development Approach - Highly reasoned, evidence based method Transparency of GenAI Prompts Used - All prompts with reflections on their use  Important Notes Students may use GenAI tools for assistance, but must provide prompts and outputs. Focus on functionality, clarity of explanation, and transparency. Plagiarism or hiding GenAI use will lead to penalties.
Integrating RAG what will do.i like to use RAG And for UI I like to use Chainlit that hel to upload pdf or pptx and ask question from chat.
For LLM need to use mistral-7b-instruct-v0.1.Q4_K_M.gguf becuse Chatgpt is paid.can you use better file structure. also Students can add Pdm And Presentaion Slides and Ask Questions.
act As a AI ML Expert and also a Software engineer.
