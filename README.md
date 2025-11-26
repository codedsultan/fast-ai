# ⭐ **AICONTENT – Modular FastAPI AI Service Starter**

A fully structured, production-ready FastAPI + Celery microservice template for AI-powered workloads.
This project provides a scalable foundation for LLM content generation, background processing, SEO analysis, image suggestion, and calibration pipelines.

Designed for **containerized deployments**, **GitHub Actions**, and **Ansible orchestration**.

---

# 📌 **Features**

* **FastAPI** application boilerplate with modular architecture
* **Celery Worker** for async/long-running tasks
* **Redis** as broker/cache
* **Pydantic v2** + `pydantic-settings` for clean environment handling
* **Structured Logging with Loguru**
* **Ruff + Black + isort + Pre-commit** enforcing code quality
* **Dockerized API + Worker images**
* **GitHub Actions CI/CD** with GHCR deployment
* Built-in folder structure for:

  * LLM providers
  * Content generation modules
  * SEO tools
  * Image suggestion
  * Calibration + personalization
  * Shared utilities
  * Prompt versioning and testing

---

# 📂 **Project Structure**

```
aicontent/
├── config/                     # App configuration
│   ├── settings.py             # Pydantic v2 Settings
│   ├── model_config.yaml
│   ├── prompt_templates.yaml
│   └── logging_config.yaml
│
├── src/                        # Source code
│   ├── main.py                 # FastAPI entry
│   ├── celery_app.py           # Celery config
│   ├── llm/                    # LLM provider abstraction
│   ├── content/                # Content generation routes + services
│   ├── images/                 # Image suggestion module
│   ├── seo/                    # SEO analysis tools
│   ├── calibration/            # Tone/style matching module
│   ├── utils/                  # Logging, rate limiting, config loader
│   └── handlers/               # Global error handlers
│
├── docker/
│   ├── Dockerfile.api          # API image
│   ├── Dockerfile.worker       # Celery worker image
│   └── docker-compose.yml      # Dev environment
│
├── tests/                      # Pytest test suite
│
├── scripts/                    # Utility scripts
│
├── .github/workflows/          # CI/CD pipelines
│
├── requirements.txt
├── requirements-dev.txt
├── README.md
└── CHANGELOG.md
```

---

# ⚙️ **Installed Packages & Why**

### 🔵 **FastAPI**

Modern async API framework for performance and developer experience.

### 🔵 **Uvicorn + uvloop**

High-performance async server with event loop acceleration.

### 🔵 **Pydantic v2**

Used for data validation & modeling.

### 🔵 **pydantic-settings**

Pydantic v2 moved `BaseSettings` into this separate package.
Used for loading environment variables from `.env`.

### 🔵 **python-dotenv**

Enables `.env` support outside Pydantic if needed.

### 🔵 **PyYAML**

Loads YAML prompt templates, model configs, and other structured configs.

### 🔵 **Celery**

Handles long-running async tasks (content generation, SEO processing, etc).

### 🔵 **Redis**

Message broker + optional caching layer.

### 🔵 **httpx + requests**

For async/sync HTTP calls to LLM APIs and partner services.

### 🔵 **loguru**

Modern structured logging with better formatting and lower overhead than Python stdlib logging.

### 🔵 **python-multipart**

Required by FastAPI for file uploads.

### 🔵 **orjson**

Ultra-fast JSON parser used internally by FastAPI when available.

### 🧪 **pytest + pytest-asyncio**

Included for robust unit + async testing.

---

# 🚀 **Getting Started (Local Development)**

### 1. Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. Run API locally

```bash
uvicorn src.main:app --reload
```

### 3. Start Celery worker

```bash
celery -A src.celery_app worker --loglevel=INFO
```

### 4. Run tests

```bash
pytest -q
```

---

# 🐳 **Docker Usage**

### Build API

```bash
docker build -t aicontent-api -f docker/Dockerfile.api .
```

### Build Worker

```bash
docker build -t aicontent-worker -f docker/Dockerfile.worker .
```

### Run with Docker Compose

```bash
docker compose up --build
```

---

# 🔄 **CI/CD (GitHub Actions + GHCR)**

This repo ships with:

### ✔ Build API Image

### ✔ Build Worker Image

### ✔ Push to GitHub Container Registry

### ✔ Automated Tests

### ✔ Automated Formatting + Linting

### ✔ Deploy with Ansible

The workflow files are located in:

```
.github/workflows/
├── build.yml
├── test.yml
└── deploy.yml
```

---

# 🔎 **Pre-commit Hooks (Code Quality Automation)**

Installed hooks:

* **Black** – Auto-formatting
* **Ruff** – Lint + autofix
* **Isort** – Import sorting
* **Trailing whitespace fixer**
* **EOF fixer**
* **YAML/JSON validators**

Install locally:

```bash
pre-commit install
pre-commit run --all-files
```

---

# 🌐 **Production Deployment**

This project is designed to be deployed with:

* **Docker images from GHCR**
* **Ansible deployment automation**
* **Caddy reverse proxy configuration**

API and Worker run as independent containers for scalability.

---

# 🧠 **Environment Configuration**

Environment variables are loaded automatically from `.env`:

```
APP_NAME=Starter AI Service
LOG_LEVEL=info
REDIS_URL=redis://redis:6379/0
OPENAI_API_KEY=...
```

Using the Pydantic Settings system:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    LOG_LEVEL: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }
```

---

# 📝 **Future Enhancements**

* Automatic prompt versioning
* Background job scheduler container
* WebSocket support
* OpenTelemetry tracing
* API gateway integration

---

# 🎉 **Summary**

You now have a **clean, modular, production-ready AI microservice**, complete with:

* API + Worker separation
* Full dockerization
* Automated testing
* Automated formatting & linting
* CI/CD + deployment
* Extensible architecture for LLMs, SEO, image tools, prompts, and more
