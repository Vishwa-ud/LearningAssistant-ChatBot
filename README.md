# 🤖 LearningAssistant- CHATBOT

**LearningAssistant** is a smart chatbot powered by a Large Language Model (LLM) that allows students to ask questions based on CTSE (Current Trends in Software Engineering) lecture notes. This project was developed as part of an AI/ML Semester 1 (2025) assignment to demonstrate how LLMs can support education by answering subject-specific queries inside a Jupyter Notebook.

### RAG
Retrieval Augmented Generation (RAG) is a technique used to combine LLMs with reliable knowledge bases to improve their performance at a specific task.
This is one of the most popular use cases for LLMs, and data scientists at tech companies (like mine) are currently working on building reliable RAGs using our company’s databases and documents.

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
- 🧠 Powered by a pre-trained LLM.
- 📎 Context-aware responses from provided notes.
- 🧩 Easy to extend with additional subjects or notes.
- 🎓 Ideal for exam prep, concept clarification, and learning assistance.

---

## 💻 Tech Stack
🔧 Programming Language & Environment
   - Python – Core language for implementation
   - Jupyter Notebook – Interactive development environment

📚 Libraries & Frameworks
   - LangChain Text Splitters – For text chunking
   - LlamaIndex – Index creation and retrieval
   - LlamaIndex LLMs Ollama – Integration of LLaMA via Ollama
   - Llama Parse – PDF parsing and document loading
   - SentenceTransformers – Semantic embeddings for document and query encoding
   - Qdrant Client – Vector database for storing and retrieving embeddings
   - PyPDF – PDF processing utility
   - python-dotenv / dotenv – Environment variable management

🧠 Model
   - LLaMA (via Ollama) – Local LLM used for generating answers

📦 Other Tools
   - Qdrant – Vector similarity search engine for retrieval

---

## 📁 File Structure
ctse-chatbot/
├── .venv
├── data/
│   └── lecture_notes.pdf 
├── .env      
├── rag4LecNote_QnA.ipynb    # ChatBot Jupyter Notebook
├── requirements.txt                 # All dependencies
├── README.md                        # Project overview
└── System diagram.jpg

---

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

## Laama Parse
docs = 'https://docs.cloud.llamaindex.ai/llamaparse/getting_started'
1. SignIn
2. Get your API Key
Follow these quick steps in LlamaCloud:
- Go to the API Key section in the left sidebar
- Click "Generate New Key"
- Give your key a name and hit "Create"
- Copy the key immediately – you won't be able to view it again

## Vector database (Qdrant)

## Setting Up Your Qdrant Cloud Cluster

When setting up a Qdrant Cloud cluster, you'll need to choose a cluster name and several other configuration options. Here's a comprehensive guide to help you through the process:

### Creating a Qdrant Cloud Cluster

### Step 1: Sign Up and Access the Dashboard

1. Go to [cloud.qdrant.io](https://cloud.qdrant.io/)
2. Sign up or sign in to your account
3. Navigate to the dashboard

### Step 2: Create a New Cluster

Click on "Create Cluster" and you'll need to provide these key details:

1. **Cluster Name**: Choose a meaningful name for your cluster
   - Examples: `devops-rag`, `lecture-embeddings`, `qa-system`
   - This name helps you identify the cluster but doesn't affect functionality
   - Use lowercase letters, numbers, and hyphens (no spaces)

2. **Cloud Provider & Region**: 
   - Select the cloud provider (AWS, GCP, Azure)
   - Choose a region close to your users or application for lower latency

3. **Cluster Size**:
   - For your RAG system, a small cluster is likely sufficient
   - Free tier: Good for testing with smaller datasets (thousands of vectors)
   - Production tier: For larger datasets or higher query volumes

4. **Network Access**:
   - Public: Accessible from anywhere (secured by API key)
   - Private: Restricted network access (more secure but requires VPC setup)

### Step 3: Get Connection Details

After creating the cluster, you'll receive:

1. **Cluster URL**: Looks like `https://your-cluster-name-xxxxx.qdrant.io`
2. **API Key**: Used for authentication

### Code 
```
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    host="xyz-example.eu-central.aws.cloud.qdrant.io",
    api_key="<your-api-key>",
)
```


## How to run qdrant  in docker
```
docker pull qdrant/qdrant
```

### Run
```
docker run -p 6333:6333 -p 6334:6334 -v "${PWD}/qdrant_storage:/qdrant/storage:z" qdrant/qdrant
```

## Ollama Set up
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
Run ollama.exe then cmd ollama
```
```
serve on 'http://127.0.0.1:11434'
```

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
