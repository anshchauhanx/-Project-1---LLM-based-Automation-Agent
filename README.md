# 🚀 LLM-Based Automation Agent

## 📌 Overview
This project is an **LLM-powered automation agent** designed for **DataWorks Solutions**. It processes large volumes of logs, reports, and code artifacts and integrates with a **Continuous Integration (CI) pipeline**. The agent can interpret **plain-English tasks**, process data, and generate verifiable outputs.

## 🛠️ Features
- ✅ **Task Execution via LLM**: Accepts plain-text instructions and executes tasks.
- ✅ **File Reading API**: Returns file contents for verification.
- ✅ **Operations Automation**: Handles tasks like formatting files, counting specific dates, and sorting JSON data.
- ✅ **Secure Data Handling**: Prevents unauthorized access and deletion.
- ✅ **Business Task Execution**: Fetch data from APIs, run SQL queries, transcribe audio, etc.
- ✅ **Docker Support**: Run the application in a **Docker container**.
- ✅ **IITM Proxy API Integration**: Uses **IITM's AI Proxy** for LLM-based processing.

---

## 🚀 Quick Start Guide

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-github-username/llm-automation-agent.git
cd llm-automation-agent
2️⃣ Install Dependencies
Ensure you have Python 3.10+ installed, then run:

sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up Environment Variables
Create a .env file in the root directory:

ini
Copy
Edit
AIPROXY_TOKEN=your_actual_proxy_token_here
4️⃣ Run the FastAPI Server
sh
Copy
Edit
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
✅ Server Running at: http://127.0.0.1:8000

📡 API Endpoints
1️⃣ Execute a Task
Endpoint: POST /run?task=<task description>
Example Request:
sh
Copy
Edit
Invoke-RestMethod -Uri "http://127.0.0.1:8000/run?task=count%20Wednesdays%20in%20/data/dates.txt" -Method Post
Example Response:
json
Copy
Edit
{"message": "Task executed successfully", "output": "Wednesdays count: 3"}
2️⃣ Read a File
Endpoint: GET /read?path=<file path>
Example Request:
sh
Copy
Edit
Invoke-RestMethod -Uri "http://127.0.0.1:8000/read?path=/data/dates-wednesdays.txt" -Method Get
Example Response:
json
Copy
Edit
{"content": "3"}
🐳 Running with Docker
1️⃣ Build the Docker Image
sh
Copy
Edit
docker build -t llm-agent .
2️⃣ Run the Docker Container
sh
Copy
Edit
docker run -p 8000:8000 llm-agent
✅ Now, access the API at: http://127.0.0.1:8000

🏗️ Project Structure
bash
Copy
Edit
llm-automation-agent/
│── app/
│   ├── main.py          # FastAPI entry point
│   ├── tasks.py         # Task execution logic
│   ├── llm.py           # LLM processing (IITM Proxy API)
│   ├── utils.py         # Utility functions
│── data/                # Task-related input/output files
│── requirements.txt     # Python dependencies
│── Dockerfile           # Docker container setup
│── .env                 # API keys & configurations
│── README.md            # Project documentation
⚙️ Configuration & Settings
The IITM Proxy API is used instead of OpenAI.
Modify .env file to configure API tokens.
Data files are stored in /data/ directory.
All outputs are written to /data/output/.
🛠️ Troubleshooting
🔴 Website Not Loading
Ensure FastAPI is running (uvicorn app.main:app --reload)
Try running on a different port (--port 8080)
Check for firewall or VPN restrictions
🔴 API Returning 400 Bad Request
Ensure IITM Proxy API Token is correct (.env file)
Test API manually:
sh
Copy
Edit
Invoke-RestMethod -Uri "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions" -Method Post
Check FastAPI logs for errors (uvicorn app.main:app --log-level debug)
🎯 Future Improvements
✅ Implement SQLite/DuckDB Support for database tasks
✅ Add advanced error handling
✅ Improve LLM task execution logic
🤝 Contributing
Fork the repository
Create a feature branch:
sh
Copy
Edit
git checkout -b feature-new-task
Commit changes & push to GitHub
Submit a Pull Request (PR)
📜 License
This project is open-source under the MIT License.

🌟 Acknowledgments
Developed for IITM TDS Project
Uses AI Proxy API by Sanand
Built with FastAPI & Python
🚀 Ready to Automate Tasks? Let's Go!

yaml
Copy
Edit

---

### **🚀 Next Steps**
✅ **Save this as `README.md` in your GitHub repo**  
✅ **Modify the `AIPROXY_TOKEN` section before publishing**  
✅ **Push the project to GitHub using**:
```sh
git add README.md
git commit -m "Added project documentation"
git push origin main
