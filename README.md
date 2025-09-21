
# Youtube Transcript Rag System

A **ChatGPT-style conversational AI** that answers questions from **YouTube video transcripts** using a **Retrieval-Augmented Generation (RAG)** pipeline.  



## Features 💻

- ✨ ChatGPT-like **UI** with **anime.js animations**  
- 📝 Answers **formatted with paragraphs & bullet points**  
- 🎯 **Conversational context** preserved for each video  
- 🌐 Single `/home` endpoint for **pipeline building + Q&A**  
- 🔒 API key managed through `.env`  


## Tech Stack 🛠

- **Python 3.11**, **FastAPI**  
- **Frontend:** HTML, CSS, JavaScript, anime.js  
- **Chat Models:** ChatGroq (`openai/gpt-oss-20b`
- **Embedding Model**: HuggingFace `all-MiniLM-L6-v2` 
- **Vector Store:** FAISS  
- **Transcript API:** youtube-transcript-api  


## Installation 🌟

Clone the repo

```bash
git clone https://github.com/<your-username>/YouTube-Transcript-RAG.git
cd YouTube-Transcript-RAG
```
Create Virtual Environments

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate # Windows
```
Install depenedencies
```
pip install -r requirements.txt
```
Create .env file and add your API key
```
GROQ_API_KEY=your_api_key_here
```
Run backend server
```
uvicorn app:app --reload
```
Run frontend in Live server
```
Open index.html in a browser
```
## What I learned from this Project ✨

During this project, I learned:

- How to build a RAG pipeline with video transcripts
- Vector embeddings and FAISS for efficient retrieval
- Usage of Retreivals and chains
- Designing a conversational frontend with animations
- Handling conversational state and history per video
💡 This project strengthened both my AI/ML understanding and full-stack development skills!


