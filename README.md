# 📈 Stock Market Multi-Agent Trading Bot

A sophisticated AI-powered trading bot that uses LangGraph and LangChain to provide intelligent responses to stock market queries. The system combines document retrieval (RAG), real-time web search, and financial data APIs to deliver comprehensive market insights.

## 🌟 Features

- **Multi-Agent Architecture**: Built with LangGraph for orchestrating multiple AI agents
- **RAG System**: Upload and query your own stock market documents (PDF, DOCX)
- **Real-time Web Search**: Integration with Tavily for current market information
- **Financial Data**: Access to Polygon.io for stock financials and market data
- **Vector Database**: Pinecone-powered semantic search over your documents
- **FastAPI Backend**: High-performance REST API
- **Streamlit UI**: User-friendly web interface

## 🏗️ Architecture

```
├── agents/                 # LangGraph workflow and agent orchestration
├── data_ingestion/         # Document loading and vector DB ingestion
├── toolkit/                # Tool definitions for agents
├── utils/                  # Model loaders and configuration
├── data_models/            # Pydantic schemas
├── exception/              # Custom exception handling
├── config/                 # YAML configuration files
└── main.py                 # FastAPI application entry point
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- API Keys for:
  - Google Gemini API
  - Groq API (optional)
  - Tavily Search API
  - Polygon.io API
  - Pinecone Vector Database

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd multi_agent_trading_bot
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
POLYGON_API_KEY=your_polygon_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

### Configuration

Edit `config/config.yaml` to customize:
- Vector database index name
- Retriever settings (top_k, score_threshold)
- LLM model selection
- Tool parameters

```yaml
vector_db:
  index_name: "trading-bot"

retriever:
  top_k: 3
  score_threshold: 0.5

llm:
  google:
    model_name: "gemini-1.5-pro"
```

## 🎯 Usage

### Starting the Backend

```bash
uvicorn main:app --reload --port 8001
```

The API will be available at `http://localhost:8001`

### Starting the Streamlit UI

```bash
streamlit run streamlit_ui.py
```

The UI will open in your browser at `http://localhost:8501`

### API Endpoints

#### Upload Documents
```bash
POST /upload
Content-Type: multipart/form-data

# Upload PDF or DOCX files
curl -X POST "http://localhost:8001/upload" \
  -F "files=@document1.pdf" \
  -F "files=@document2.docx"
```

#### Query Chatbot
```bash
POST /query
Content-Type: application/json

{
  "question": "What are the financials of Apple Inc?"
}
```

Example with curl:
```bash
curl -X POST "http://localhost:8001/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the financials of Apple Inc?"}'
```

## 🛠️ Available Tools

The bot has access to three main tools:

1. **Retriever Tool**: Searches uploaded documents using semantic similarity
2. **Tavily Search**: Real-time web search for current market information
3. **Polygon Financials**: Access to company financials and stock data

## 📊 How It Works

1. **Document Ingestion**: Upload PDFs/DOCX files containing market research, reports, or analyses
2. **Vector Storage**: Documents are chunked and embedded into Pinecone
3. **Agent Workflow**: When you ask a question:
   - The LangGraph agent analyzes the query
   - Decides which tools to use (retriever, search, or financials)
   - Combines information from multiple sources
   - Generates a comprehensive response

## 🔧 Development

### Project Structure

- `agents/workflow.py`: LangGraph state graph and agent logic
- `data_ingestion/ingestion_pipeline.py`: Document processing pipeline
- `toolkit/tools.py`: Tool definitions for the agent
- `utils/model_loaders.py`: LLM and embedding model initialization
- `main.py`: FastAPI routes and application logic

### Adding New Tools

1. Define your tool in `toolkit/tools.py`:
```python
@tool
def your_custom_tool(query: str):
    """Description of what your tool does"""
    # Your implementation
    return result
```

2. Add it to the tools list in `agents/workflow.py`:
```python
self.tools = [retriever_tool, financials_tool, tavilytool, your_custom_tool]
```

### Custom Exception Handling

The project uses custom exception handling. All exceptions are wrapped in `TradingBotException` for better debugging:

```python
from exception.exceptions import TradingBotException
import sys

try:
    # Your code
except Exception as e:
    raise TradingBotException(e, sys)
```

## 📦 Dependencies

Core dependencies:
- `langchain` - LLM framework
- `langgraph` - Multi-agent workflows
- `langchain-pinecone` - Vector database integration
- `langchain-google-genai` - Google Gemini integration
- `fastapi` - Web framework
- `streamlit` - UI framework
- `tavily-python` - Web search
- `polygon` - Financial data API

## ⚠️ Important Notes

- **API Costs**: Be mindful of API usage costs (Google Gemini, Tavily, Polygon)
- **Rate Limits**: Respect API rate limits for external services
- **Security**: Never commit your `.env` file (it's in `.gitignore`)
- **Pinecone Index**: The index is created automatically on first run

## 🐛 Troubleshooting

### Common Issues

**Issue**: `Pinecone index not found`
- Solution: The index is auto-created. Ensure your API key is correct and you have permissions

**Issue**: `Environment variables not loaded`
- Solution: Ensure `.env` file is in the project root and contains all required keys

**Issue**: `Model not loading`
- Solution: Check `config/config.yaml` for correct model names and ensure API keys are valid

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or support, contact: thangamani1128@gmail.com

---

**Built with** ❤️ **using LangChain, LangGraph, and FastAPI**
