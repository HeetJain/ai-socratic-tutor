markdown
# 🎓 Luna: Multilingual Socratic AI Tutor

Luna is an AI-powered educational assistant designed to solve a core flaw in modern digital learning: directly providing answers harms critical thinking. Built using a Retrieval-Augmented Generation (RAG) architecture, Luna acts as a Socratic guide that references curriculum documents to prompt students with guiding questions, while equipping educators with actionable classroom analytics.

---

## 🌟 Key Features

* **Socratic Dialogue Engine:** Instead of handing out solutions, Luna asks structured follow-up questions to help students derive answers independently.
* **Curriculum-Grounded RAG:** Answers are anchored directly in uploaded chapter text to prevent hallucinations and off-syllabus drift.
* **Teacher Insights Dashboard:** Real-time visibility into classroom metrics, active student counts, and aggregated topic confusion trends.
* **Resilient Architecture:** Integrated error-handling, timeout controls, and structured API payloads to maintain interface stability.

---

## 🛠️ System Architecture

* **Frontend UI:** Streamlit (Python)
* **Orchestration & RAG Pipeline:** Dify.ai
* **LLM Engine:** Gemini 3.5 Flash lite
* **Vector Knowledge Base:** Chunked & embedded curriculum text

---

## 🚀 Quickstart & Local Setup

### Prerequisites
* Python 3.9+
* pip

### Installation

1. **Clone the repository:**
   bash
   git clone https://github.com/HeetJain/ai-socratic-tutor
   cd ai-socratic-tutor



2. **Install dependencies:**
bash
pip install -r requirements.txt




3. **Run the application:**
bash
streamlit run app.py





*(Note: API routing and knowledge retrieval are configured via the backend endpoint; no additional local environment variables are required to test the interface.)*
