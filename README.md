# URL Shortener (FastAPI)

A scalable URL Shortener similar to Bitly, built using FastAPI.
This application allows users to shorten long URLs, redirect them, track clicks, and includes features such as custom aliases, expiry, caching, and rate limiting.

---

## Live Demo

https://your-render-link.onrender.com/docs

---

## Features

### Core Features

* Shorten long URLs
* Redirect short URLs to original URLs
* Generate unique short codes

### Advanced Features

* Click tracking (analytics)
* Custom aliases for URLs
* Expiry-based links
* Redis caching for faster access
* Rate limiting to prevent abuse

---

## Tech Stack

* Backend: FastAPI (Python)
* Database: SQLite
* Caching: Redis
* Server: Uvicorn
* Version Control: Git and GitHub
* Deployment: Render

---

## Project Structure

```
app/
 ├── main.py              # Entry point
 ├── routes/              # API endpoints
 │     └── url_routes.py
 ├── services/            # Business logic
 │     └── url_service.py
 ├── utils/               # Helper functions
 │     └── helpers.py
 ├── core/                # Configuration (Redis, rate limiting)
 │     └── config.py
 ├── models.py            # Database models
 └── database.py          # Database connection
```

---

## Application Flow

```
User → POST /shorten → Store URL in database  
User → GET /{code} → Retrieve URL → Increment clicks → Redirect  
User → GET /stats/{code} → Retrieve analytics  
```

---

## API Endpoints

### Shorten URL

```
POST /shorten
```

Request:

```
{
  "url": "https://example.com",
  "custom_code": "optional",
  "expiry_minutes": 10
}
```

---

### Redirect

```
GET /{code}
```

---

### Get Statistics

```
GET /stats/{code}
```

Response:

```
{
  "original_url": "https://example.com",
  "clicks": 5
}
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   (Windows)
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Start Redis (Optional)

```
redis-server
```

### 5. Run Application

```
uvicorn app.main:app --reload
```

---

## Notes

* Redis is optional in deployment; fallback handling is implemented.
* SQLite is used for simplicity and can be replaced with PostgreSQL for scalability.

---

## Challenges Faced

* Resolving circular imports in modular architecture
* Managing database sessions correctly
* Handling cache and database consistency
* Managing Redis connection issues during deployment

---

## Future Improvements

* Add user authentication and dashboards
* Integrate PostgreSQL
* Build frontend interface (React)
* Enhance analytics (time-based and location-based tracking)
* Scale to distributed architecture

---

## Learning Outcomes

* Backend development using FastAPI
* Clean and modular architecture design
* Redis caching and rate limiting
* Debugging real-world backend issues
* API design and deployment practices

---

## Author


GitHub: https://github.com/nivi2604
