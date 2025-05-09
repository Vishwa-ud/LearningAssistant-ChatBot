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

#### List Available Models
```
ollama list
```
# pull from ollama
```
ollama run gemma3:1b
ollama run deepseek-r1:1.5b-qwen-distill-q4_K_M
ollama run llama3.2:3b
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

# Models
```

```

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


Here's a clear and concise **comparison table** between using `PyPDF` and `LlamaParse` for PDF parsing, specifically in the context of preparing text for LLM-based question answering with `RecursiveCharacterTextSplitter`.

---

### PyPDF vs LlamaParse for PDF Text Extraction**

| Feature                          | **PyPDF**                                                  | **LlamaParse**                                                                |
| -------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Library**                      | `pypdf` (open source, local)                               | `llama_parse` (cloud-based, requires API key)                                 |
| **Extraction Method**            | Extracts raw text page-by-page using `page.extract_text()` | Uses AI models to parse layout into structured **markdown** or plain **text** |
| **Handling of Complex Layouts**  | Poor – struggles with columns, tables, headings            | Excellent – preserves structure, bullet points, and semantic layout           |
| **Accuracy of Output**           | Basic and depends on PDF structure                         | High-quality, semantically segmented markdown or text                         |
| **Output Format**                | Single plain string                                        | List of documents (`Document` objects), with `doc.text` as markdown           |
| **Page Number Tracking**         | Manual – you can track by looping through `reader.pages`   | Not available by default                                                      |
| **Setup & Dependencies**         | No account/API key needed; runs locally                    | Requires `llama_parse` package and LLamaParse Cloud API key                   |
| **Speed**                        | Fast (local processing)                                    | Slower (uses external API calls)                                              |
| **Text Splitting Compatibility** | Directly compatible with `RecursiveCharacterTextSplitter`  | Also compatible after joining `doc.text` fields                               |
| **Use Case Fit**                 | Good for simple PDFs with consistent structure             | Best for academic PDFs, presentations, scanned or structured content          |

---

### 🟩 **When to Use PyPDF**

* PDF is **simple** and contains clean, linear text.
* You need **offline/local processing** without external API calls.
* You're okay with **manual metadata tracking** (e.g., page numbers).

### 🟦 **When to Use LlamaParse**

* PDF has **complex layout** (e.g., slides, columns, bullets).
* You want **high-quality parsing** into markdown with clean structure.
* You're building a **QA or RAG system** that benefits from semantic segmentation.
* You're okay using an **API key** and cloud processing.

---


### ADD Page number
```
from pypdf import PdfReader
import os

FILE_PATH = os.path.join("data", "Lecture1-a.pdf")
reader = PdfReader(FILE_PATH)
number_of_pages = len(reader.pages)

entire_text = ""
# Loop through each page and print its text with page number
for page_num in range(number_of_pages):
    page = reader.pages[page_num]
    text = page.extract_text()
    entire_text += page.extract_text()

    print(f"\n--- Page {page_num + 1} ---\n")
    print(text if text else "[No text found on this page]")
```

PyPDF
output = 
```
Intro to DevOps and Beyond\nRavindu Nirmal FernandoAbout Me\n• STL - DevOps @ Sysco LABS - Sri Lanka\n• MSc in Computer Science specialized in \nCloud Computing (UOM)\n• AWS Certified Solutions Architect -
```
LlamaParse 
output = 
```
--- Extracted Text Preview ---


--- Document 1 ---

# Intro to DevOps and Beyond

# Ravindu Nirmal Fernando

[...truncated...]


--- Document 2 ---

# About Me

- STL - DevOps @ Sysco LABS - Sri Lanka
- MSc in Computer Science specialized in Cloud Computing (UOM)
- AWS Certified Solutions Architect - Professional
- Certified Kubernetes Administrator (CKA)
- AWS Community Builder

Ravindu Nirmal Fernando
...
Thank You!

```