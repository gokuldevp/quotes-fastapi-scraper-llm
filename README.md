# Quotes Scraper & FastAPI Service

## Overview

This project is a Python automation solution that:

* Logs into https://quotes.toscrape.com using Selenium
* Scrapes quotes from the first page after login
* Stores scraped data in JSON format
* Exposes a local **FastAPI** server to:

  * Check service health
  * Trigger a fresh scrape
  * Retrieve a random quote from cache
---

## Tech Stack

* **Python 3**
* **Selenium**
* **FastAPI**
* **Pydantic**
* **JSON file storage**
* **In-memory cache**
---

## Project Structure

```
quotes-fastapi-scraper/
├── app/
│   ├── api/
│   │   ├── health.py  
│   │   ├── quote.py      
│   │   └── refresh.py    
│   ├── core/
│   │   ├── cache.py       
│   │   ├── config.py      
│   │   ├── exceptions.py  
│   │   ├── logger.py       
│   │   └── screenshot.py  
│   ├── models/
│   │   └── quote.py        
│   ├── pages/
│   │   ├── base_page.py    
│   │   ├── login_page.py   
│   │   └── quotes_page.py  
│   ├── services/
│   │   ├── browser_manager.py  
│   │   ├── login_service.py    
│   │   ├── quote_scraper.py    
│   │   └── storage_service.py  
│   └── main.py            
├── data/
│   └── quotes.json               
├── logs/   
│   └── app.log                
├── screenshots/            
├── .env          
├── .gitignore
├── requirements.txt
└── README.md
```
---

## Setup

### Prerequisites

- Python 3.10+
- Google Chrome browser

---
## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/gokuldevp/quotes-fastapi-scraper.git
cd <the_cloned folder>
```

---

### 2. Create & Activate Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```
---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
---

### 4. Configure Environment Variables

Create a `.env` file in the project root and add the details in the `.env.example`

---

### 5. Start the API Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

### Interactive Swagger UI.

Once running, open:

```
http://127.0.0.1:8000/docs
```
---

## API Endpoints

### GET `/health`

Health check endpoint.

**Response**

```json
{ "status": "ok" }
```

---

### POST `/refresh`

Triggers a fresh automation run:

* Opens a browser using Selenium
* Logs in to the site
* Scrapes quotes from the first page
* Updates the in-memory cache and JSON file

**Response**

```json
{ "count": 10, "source": "scraped" }
```

---

### GET `/quote/random`

Returns a random quote from the current cache.

**Response**

```json
{
  "quote": "...",
  "author": "...",
  "tags": ["..."],
  "cached_at": "2026-01-17T10:00:00Z"
}
```

**If no cache exists:**

* Returns HTTP **503** with error message "No cached quotes available. Trigger /refresh first."

---

## Design Decisions

### 1. Object-Oriented Architecture

The solution is split into focused classes:

* **BrowserManager** – manages Selenium browser lifecycle
* **LoginService** – handles authentication logic
* **QuoteScraper** – extracts quotes from the page
* **StorageService** – persists data to JSON
---

### 2. Page Object Model (POM)

All selectors and page-level logic are isolated in the `pages/` directory.
This minimizes the impact of DOM changes and keeps scraping logic clean.

---

### 3. Caching Strategy

* **In-memory cache** for fast API responses
* **JSON file** for persistence and inspection
* Cache is refreshed only via the `/refresh` endpoint

---

### 4. Reliability & Failure Handling

* Login is retried up to **3 times**
* If scraping fails:

  * The error is logged
  * A screenshot is captured for debugging
* Browser cleanup is guaranteed using `try/catch`

---

## Security & Configuration

* Credentials are saved in `.env`
* Loaded via environment variables
* In production, secrets should be stored in a secure secrets manager never committed to source control.

---

## What I Would Improve for Long-Running Production Use

If this system ran continuously for months:

1. Replace JSON storage with a database 
2. Add rate limiting, retries, and backoff strategies
3. Add Alerts for failures or abnormal scrape times.
---

## Challenges in Real-World Web Automation

Automating real websites is challenging due to:

* Bot detection
* CAPTCHAs and IP blocking
* Frequently changing DOM structures
* Authentication complexity
* Network instability
* Legal and ethical constraints
* Complex website ui (eg. Shadow dom)
---

