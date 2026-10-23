# Rizqona - A Campus Application for Universiti Malaya students

**Summary:**

- To bring together Fragmented activities in our campus life to one platform. 

**Live:** https://rizqona.icyisland-5de26c98.southeastasia.azurecontainerapps.io

**What It Does:**

- Browse Restaurants and Menus
- Separate Authentication for students (UM Email Validation) and Restaurant Owner using JWT
- Search and Filter : By Cuisine, Price & availability
- Adding to Cart, Place Order and restaurant owner order management
- Content-Based Filtering using (TF-IDF + Cosine Similarity)
- A Natural Language Query Assistant - Replies real menu data understand semantics using RAG + LLM

**Tech Stack**

| Layer | Technology |
|-------|------------|
| API | FastAPI |
| Database | PostgreSQL (Neon) + pgvector |
| ML | scikit-learn (TF-IDF, cosine similarity) |
| AI | sentence-transformers, pgvector, Groq LLM |
| Deployment | Docker + Azure Container Apps |
| Auth | JWT + bcrypt |

**Architecture**

```
Student Request
      ↓
FastAPI (REST API)
      ↓
PostgreSQL (Neon)
  ├── menu_items, restaurants, orders, events
  └── menu_item_embeddings (pgvector)
      ↓
ML Engine (recommendations)
AI Engine (RAG pipeline → Groq LLM)
      ↓
Azure Container Apps
```

**Local Setup**

```
git clone https://github.com/touhidulai/Rizqona
cd Rizqona
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

**Structure of .env File**

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=rizqona
DB_USER=user
DB_PASSWORD=password
DB_SSLMODE=disable
GROQ_API_KEY=your_groq_api_key

```
**Finally**

```
python3 -m uvicorn main:app --reload
```

