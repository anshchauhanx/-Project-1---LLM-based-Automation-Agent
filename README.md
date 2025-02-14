# LLM-based Automation Agent

## 🚀 Project Overview
This project is an **LLM-based Automation Agent** that can execute various operational and business tasks using a **FastAPI**-based REST API. The agent takes plain-English tasks, processes them using an **LLM (via IITM Proxy API)**, and performs multi-step automation.

## 📌 Features
- ✅ **Execute English-language tasks** using `/run?task=...`
- ✅ **Read output files** using `/read?path=...`
- ✅ **Supports various automation tasks** (file operations, API requests, database queries, and more)
- ✅ **Runs inside a Docker container** and can be deployed with **Podman**

## 🛠️ Tech Stack
- **Python 3.11**
- **FastAPI** (REST API framework)
- **SQLite3** (Database operations)
- **OpenAI API via IITM Proxy** (for task processing)
- **Docker & Podman** (for containerization)

---

## 📂 Project Structure
```
llm-automation-agent/
│-- app/
│   ├── main.py       # FastAPI entry point
│   ├── tasks.py      # Handles task execution
│   ├── llm.py        # Communicates with IITM Proxy API
│-- data/             # Folder for generated output files
│-- create_db.py      # Script to initialize SQLite database
│-- Dockerfile        # Container setup
│-- .env              # API key configuration
│-- requirements.txt  # Python dependencies
│-- README.md         # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/anshchauhanx/-Project-1---LLM-based-Automation-Agent.git
cd llm-automation-agent
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file and add your **IITM Proxy API key**:
```
AIPROXY_TOKEN=your_iitm_proxy_api_key
```

### 4️⃣ Run the FastAPI Server
```sh
uvicorn app.main:app --reload
```
✅ API will be available at: **http://127.0.0.1:8000**

### 5️⃣ Test API Endpoints
#### **Run a Task**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/run?task=count%20Wednesdays%20in%20/data/dates.txt" -Method Post
```
#### **Read a File**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/read?path=/data/dates-wednesdays.txt" -Method Get
```

---

## 🐳 Docker Deployment
### 1️⃣ Build the Docker Image
```sh
docker build -t anshchauhanx/llm-automation-agent .
```

### 2️⃣ Push to Docker Hub
```sh
docker login
docker tag anshchauhanx/llm-automation-agent anshchauhanx/llm-automation-agent:latest
docker push anshchauhanx/llm-automation-agent:latest
```

### 3️⃣ Run the Image with Podman
```sh
podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 docker.io/anshchauhanx/llm-automation-agent:latest
```
✅ **API will be available at:** `http://localhost:8000`

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

🚀 **Happy Coding!** 🎉
