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

- **Python 3.9+**
- **Jupyter Notebook**
- **LLM Platform**: Ollama / Hugging Face Transformers
- **(Optional)**: Qudrant or ChromaDB for vector-based retrieval
- **LangChain** *(optional, if used for chaining LLM with retrieval)*

---

## 📁 File Structure
ctse-chatbot/
│
├── data/
│   ├── lecture_notes.pdf       # or pptx files
│   └── sample_slides.pptx
├── rag4LecNote_QnA_ChatBot.ipynb    # ChatBot
├── requirements.txt                 # All dependencies
└── README.md                        # Project overview


## Set up
```
python -m venv .venv # create vertual environment
```
```
.venv\Scripts\activate  # activate vertual environment
```
```
pip install -r requirements.txt # install dependencies
```


## Vector database (Qdrant)

### How to run qdrant docker
```
docker pull qdrant/qdrant
```

### Run
```
docker run -p 6333:6333 -p 6334:6334 -v "${PWD}/qdrant_storage:/qdrant/storage:z" qdrant/qdrant
```

## Ollama
Download Ollama & Install .exe 

### Models
```
ollama run gemma3:1b
ollama run deepseek-r1:1.5b
ollama run llama3.1:8b
```
### Run
In CMD
```
ollama serve 
```
OR
```
Run ollama.exe then ollama
```
serve on 'http://127.0.0.1:11434'

## Prompt
You said:
my task is Develop a simple chatbot using an LLM to answer questions based on CTSE(current trends in software enginerring ) lecture notes. The chatbot should be implemented inside Jupyter Notebook(.ipynb) use proper file structure can you more jupiter notebook files. Criteria Working Jupyter Notebook Chatbot - Robust, smooth and insightful responses Justification of LLM Choice - Strong, thorough and critical reasoning Justification of Development Approach - Highly reasoned, evidence based method Transparency of GenAI Prompts Used - All prompts with reflections on their use  Important Notes Students may use GenAI tools for assistance, but must provide prompts and outputs. Focus on functionality, clarity of explanation, and transparency. Plagiarism or hiding GenAI use will lead to penalties.
Integrating RAG what will do.i like to use RAG And for UI I like to use Chainlit that hel to upload pdf or pptx and ask question from chat.
For LLM need to use mistral-7b-instruct-v0.1.Q4_K_M.gguf becuse Chatgpt is paid.can you use better file structure. also Students can add Pdm And Presentaion Slides and Ask Questions.
act As a AI ML Expert and also a Software engineer.


### RAG
Retrieval Augmented Generation (RAG) is a technique used to combine LLMs with reliable knowledge bases to improve their performance at a specific task.

This is one of the most popular use cases for LLMs, and data scientists at tech companies (like mine) are currently working on building reliable RAGs using our company’s databases and documents.

This course will teach you to build RAG systems with vector databases and embedding techniques —in-demand skills that make you an attractive candidate in today’s tech market.
