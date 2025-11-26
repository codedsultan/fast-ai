Here is a **clean, simple, ready-to-ship README.md** for your current FastAPI starter app + Docker + GitHub Actions workflow.

It is written to be copy-paste ready and works perfectly with your current folder structure & pipeline.

---

# 📘 FastAPI Starter App (Docker + GitHub Actions CI/CD)

This is a minimal FastAPI application packaged with Docker and automatically built/published using GitHub Actions.

Perfect for microservices, quick experiments, and CI/CD testing.

---

## 🚀 Features

* FastAPI application (Python 3.11)
* Lightweight Docker build (multi-stage)
* Non-root user for security
* GitHub Actions CI/CD workflow
* Auto-build & auto-push to GitHub Container Registry (GHCR)
* Tagged images for branches, releases, and commits

---

## 📁 Project Structure

```
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   └── main.py
└── requirements.txt
```

---

## ▶️ Running Locally (Without Docker)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Visit:

```
http://localhost:8000
```

---

## 🐳 Running with Docker

### **1. Build the Docker image**

```bash
docker build -t fastapi-starter .
```

### **2. Run the container**

```bash
docker run -p 8000:8000 fastapi-starter
```

Now visit:

```
http://localhost:8000
```

---

## 🔧 Dockerfile Overview

* **Stage 1** installs dependencies
* **Stage 2** copies runtime packages + app code
* Runs under a safe non-root `appuser`
* Uses Uvicorn to serve FastAPI

---

## 🚦 GitHub Actions: Automatic Docker Builds

The pipeline is located at:

```
.github/workflows/build.yml
```

What it does:

* Builds a Docker image for every push and PR
* Tags images automatically (branch, semver, SHA)
* Pushes images to **GitHub Container Registry (GHCR)**

Your image will be available at:

```
ghcr.io/codedsultan/fastapi-starter:<tag>
```

Examples:

```
ghcr.io/codedsultan/fastapi-starter:latest
ghcr.io/codedsultan/fastapi-starter:develop
ghcr.io/codedsultan/fastapi-starter:sha-abcdef
```

---

## 🧪 Test the API

After running:

```bash
curl http://localhost:8000/
```

Expected response:

```json
{"message": "FastAPI app running in Docker!"}
```

---

## 📦 Pushing a Release Tag

If you create a git tag like:

```
git tag v1.0.0
git push origin v1.0.0
```

The workflow will build and publish an image tagged:

```
ghcr.io/codedsultan/fastapi-starter:1.0.0
ghcr.io/codedsultan/fastapi-starter:v1.0.0
ghcr.io/codedsultan/fastapi-starter:1.0
```

---

## 📄 License

MIT

---

If you want, I can generate:

✅ A docker-compose file
✅ A production version (gunicorn + uvicorn workers)
✅ A Kubernetes manifest
✅ A Makefile for common commands
Just tell me.
