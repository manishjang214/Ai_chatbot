AI Chatbot

Production-ready AI chatbot built using FastAPI, LangChain, and LLMs.
This project supports context memory, API integrations, scalable architecture, and modern AI workflow management.


Features--->

    FastAPI backend
    LangChain integration
    LLM support
    Context memory handling
    Environment variable management
    Scalable project structure
    Virtual environment setup with uv


Tech Stack--->
    Python
    FastAPI
    LangChain
    LangGraph
    Groq API
    Uvicorn
    Python Dotenv    


Installation & Setup
1. Install UV Package Manager
    ---> using cmd --- pip install uv

2. Initialize UV Project
    ---> using cmd --- uv init

3. Create Virtual Environment        
    ---> using cmd --- uv venv

4. Activate Virtual Environment
    ---> using cmd --- .venv\Scripts\activate


Install Dependencies
1. Create requirements.txt
    Add the following packages:
      -  langchain
      -  langgraph
      -  langchain-groq
      -  python-dotenv
      -  ipykernel
      -  fastapi
      -  uvicorn


Install Requirements
----->  uv add -r requirements.txt


Install IPykernel
----->  uv pip install ipykernel


Project Structure--->

AI_Chatbot/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   └── utils/
│
├── requirements.txt
├── .env
├── README.md
└── .gitignore


Run the Project:----->
   ----> uvicorn app.main:app --reload



Future Improvements
Authentication system
Chat history database
Streaming responses
Multi-model support
Docker deployment
Frontend integration   