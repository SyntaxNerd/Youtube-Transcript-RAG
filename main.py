# Youtube transcript RAG system
import os
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# load api key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# global variable
qa_system = None

# variables
video_rag_system = {}
video_chat_history = {}

# pipeline function
def rag_pipeline(video_id: str):
    global qa_system

    # fetch transcripts
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)

    # single string
    full_text = " ".join(t.text for t in transcript)

    # text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 200,
        chunk_overlap = 50
    )
    chunks = splitter.split_text(full_text) # chunk size = 50

    # embeddings and vector store
    embedding_model = HuggingFaceEmbeddings(
        model_name = "all-MiniLM-L6-v2"
    )
    faiss_store = FAISS.from_texts(chunks, embedding_model) # 50 dim

    # initialize model
    llm = ChatGroq(
        model = "openai/gpt-oss-20b",
        temperature = 0.5,
        max_tokens = None
    )

    # retreival system
    conv_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = faiss_store.as_retriever(search_kwargs = {"k": 3}),
        return_source_documents = True
    )
    
    video_rag_system[video_id] = conv_chain
    video_chat_history[video_id] = []

    return f"RAG pipeline built for {video_id}"

# question function
def ask_question(video_id: str, query: str):
    if video_id not in video_rag_system:
        return "Error: Unable to build RAG pipeline for this video"
    
    conv_chain = video_rag_system[video_id]
    history = video_chat_history[video_id]

    result = conv_chain({
        "question": query,
        "chat_history": history
    })

    history.append((query, result["answer"]))
    return result["answer"]