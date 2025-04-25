# Deep Research AI Agent 🤖🔍

![LangChain](https://img.shields.io/badge/LangChain-OpenAI-blue)
![Groq](https://img.shields.io/badge/Groq-Llama3-green)
![Tavily](https://img.shields.io/badge/Tavily-Web_Search-orange)

A state-of-the-art research assistant powered by LangChain and Groq's ultra-fast LLMs, capable of conducting deep web research and generating comprehensive answers.

## Features ✨

- **Multi-stage Research Pipeline** 🏗️  
  - Research Agent → Drafting Agent workflow
  - State management with LangGraph

- **Web Search Integration** 🌐  
  - Real-time web research using Tavily API
  - Source citation with URLs

- **Conversational Memory** 🧠  
  - Maintains full chat history
  - Context-aware responses

- **High-Speed LLM** ⚡  
  - Powered by Groq's Llama3-8b (8192 context)
  - 300+ tokens/second generation

- **Error Resilient** 🛡️  
  - Comprehensive error handling
  - Graceful fallback mechanisms

## Tech Stack 🛠️

| Component       | Technology           |
|----------------|---------------------|
| LLM            | Groq (Llama3-8b)    |
| Framework      | LangChain + LangGraph|
| Search Engine  | Tavily              |
| Memory         | ConversationBuffer   |

## Installation ⚙️

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/Deep_Research_AI_Agent.git
cd Deep_Research_AI_Agent
```


### 2. Set Up Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```


### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create .env file:
```bash
cp .env.example .env
```
Edit .env with your API keys:

```bash
env
TAVILY_API_KEY=your_tavily_key
GROQ_API_KEY=your_groq_key
```

## Usage 🚀

### Basic Execution
```bash
python research.py
```

### Interactive Mode
The default mode provides a conversational interface:

```bash
Enter your research topic or type 'exit': "Latest breakthroughs in quantum computing"
```
### Command Line Arguments (Optional)
```bash
python research.py --query "Your research question" [--max_results 5]
```

## Project Structure 📂
Deep_Research_AI_Agent/
├── research.py          # Main application logic
├── requirements.txt     # Dependency list
├── .env.example         # API key template
├── README.md            # This file
└── tests/               # Test cases (future)

## Example Output 📝

**Research Topic:** Latest iPhone features

**Findings:**
1. A16 Bionic chip with 4nm architecture
2. Dynamic Island notification system
3. 48MP main camera with Photonic Engine
4. Crash Detection feature
5. Always-On Display (Pro models)

**Sources:**
- Apple.com/iphone-14
- TheVerge.com/iphone-14-review


## Contribution 🤝
Pull requests welcome! Please:

Fork the repository

Create your feature branch

Commit your changes

Push to the branch

Open a pull request

## License 📜
MIT License - See LICENSE.md

