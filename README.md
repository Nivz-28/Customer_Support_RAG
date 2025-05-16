# Customer_Support_RAG
# 📦 Customer Support RAG

A Retrieval-Augmented Generation (RAG) system for customer service chatbots, powered by a hybrid stack of open-source NLP tools and a high-quality support dataset.

This project allows you to:

* Embed real customer queries and answers
* Search semantically similar support responses using FAISS
* Generate grounded and helpful answers using an LLM backend

---

## ✅ Current Features & Progress

### ✔️ Step 1: Dataset Preparation

* ✅ Loaded [Bitext Customer Support LLM Dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset)
* ✅ Extracted key fields: `instruction`, `response`, `category`, `intent`
* ✅ Cleaned templates (e.g., removed placeholders like `{{Order Number}}`)
* ✅ Deduplicated Q\&A pairs
* ✅ Saved as `rag_support_clean.csv`

### 🚧 Upcoming (Next Steps)

* [ ] Build a RAG pipeline to retrieve top-k similar questions + use LLM to answer
* [ ] Optionally support intent recognition or flagging

---

## 🧪 Dataset Sample

A single entry from the cleaned dataset:

```
Instruction: I need to cancel my order
Response: I understood that you need assistance with canceling your order. I'm here to help you through the process.
Category: ORDER
Intent: cancel_order
```

---

## 🧰 Tech Stack

* 🤗 Hugging Face Datasets
* 🧭 FAISS (vector search)
* 🧪 Pandas
* 📊 (Upcoming) LangChain or FastAPI for RAG orchestration
* 🌐 (Optional) Streamlit for chatbot UI

---

## 🗂 File Structure

```
Customer_support_RAG/
├── dataset_loader.py           # Loads and cleans dataset
├── rag_support_clean.csv       # Cleaned support data
├── README.md                   # Project overview
└── app.py                      # (Coming soon)FastAPI app
```

---

## 🤖 Contributors

* Project Lead: \Nivedita
* Dataset: Bitext via Hugging Face
* Tools: Hugging Face, FAISS, MiniLM

---

## 📬 License

MIT License. Dataset terms as per Hugging Face dataset source.

