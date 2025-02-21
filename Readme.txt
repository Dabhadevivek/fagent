
---

# 📊 Multi-Agent AI Financial & Web Search Assistant  

This project integrates **AI-powered agents** to assist with **financial analysis** and **web searches**, leveraging **Groq Llama3**, **DuckDuckGo**, and **Yahoo Finance tools** to provide **real-time insights**.  

## 🚀 Features  

✔️ **Web Search Agent** – Searches the web for relevant information and always includes sources.  
✔️ **Finance AI Agent** – Fetches stock prices, analyst recommendations, fundamentals, and latest company news.  
✔️ **Multi-Agent Collaboration** – Both agents work together to provide **comprehensive** responses.  
✔️ **Markdown Support** – Responses are well-structured and easy to read.  
✔️ **Table-Based Outputs** – Financial data is displayed in tables for better clarity.  

## 🏗️ Tech Stack  

- **Python** – Main programming language  
- **Groq Llama3** – AI model for processing queries  
- **DuckDuckGo** – Web search tool  
- **Yahoo Finance (YFinance)** – Retrieves financial data  
- **dotenv** – Manages API keys securely  

## 🔧 Installation  

1️⃣ **Clone the repository:**  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
  
2️⃣ **Create a virtual environment & install dependencies:**  
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```

3️⃣ **Set up environment variables:**  
Create a `.env` file and add:  
```ini
OPENAI_API_KEY=your_openai_api_key
PHI_API_KEY=your_phi_api_key
```

## 🏃‍♂️ Usage  

Run the app using:  
```bash
python main.py
```
Example query:  
```python
multi_ai_agent.print_response(
    "Summarize analyst recommendation and share the latest news for NVDA", 
    stream=True
)
```

## 📈 Output Example  

✅ Web Search Agent fetches the latest stock news.  
✅ Finance AI Agent retrieves **real-time stock prices & analyst insights**.  
✅ **Well-formatted response** with **tables & sources**.  

## 🤝 Contribution  

🔹 Fork the repo & create a feature branch  
🔹 Open a pull request with improvements  
🔹 Report bugs or suggest features via issues  

