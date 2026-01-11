# End-to-End ML + MLOps Project – Laptop Price Prediction

## 📌 Project Overview
This project is a complete end-to-end Machine Learning and MLOps system
designed to predict laptop prices based on hardware and configuration
features.

The main goal of this project is not only model accuracy, but building a
production-ready ML system that follows real-world industry practices.



## 🎯 Problem Statement
Build a scalable and production-ready Machine Learning system that:
- Trains a price prediction model
- Exposes predictions via a REST API
- Uses Docker for containerization
- Uses Kubernetes for deployment
- Uses CI pipelines for automation



## 🧠 Solution Overview
The system follows the complete ML lifecycle:

1. Data analysis and preprocessing
2. Model training and retraining
3. Model serialization
4. API-based inference using FastAPI
5. Containerization using Docker
6. CI pipeline using GitHub Actions
7. Kubernetes deployment for scalability



## 🛠️ Tech Stack
- **Language:** Python  
- **Data Processing:** Pandas  
- **Machine Learning:** Scikit-learn  
- **API:** FastAPI  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions  
- **Orchestration:** Kubernetes (Docker Desktop)



## 🏗️ Project Architecture
Raw Data
   ↓
Data Cleaning & Feature Engineering
   ↓
Model Training & Evaluation
   ↓
Saved Model (.pkl)
   ↓
FastAPI Inference Service
   ↓
Docker Container
   ↓
Kubernetes Deployment



## 📁 Project Structure
end-to-end-ml-mlops/
│
├── api/                 # FastAPI application
├── data/                # Raw and processed datasets
├── models/              # Trained ML models
├── notebooks/           # EDA & training notebooks
├── k8s/                 # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
├── .github/workflows/   # CI pipeline
│   └── ci.yml
├── Dockerfile
├── .gitignore
└── README.md



## 🚀 How to Run Locally (Using Docker)

### Step 1: Build Docker Image
docker build -t laptop-price-api .


### Step 2: Run Docker Container
docker run -p 8000:8000 laptop-price-api


### Step 3: Open API Docs
Open your browser and go to:
[text](http://localhost:8000/docs)



## 🔌 API Usage Example

### Endpoint
POST /predict


### Sample Request
{
"Company": "Dell",
"TypeName": "Ultrabook",
"Inches": 13.3,
"ScreenResolution": "Full HD 1920x1080",
"Cpu": "Intel Core i5",
"Ram": "8GB",
"Memory": "256GB SSD",
"Gpu": "Intel HD Graphics",
"OpSys": "Windows 10",
"Weight": 1.37
}


### Sample Response
{
"predicted_price": 93743.44
}



## 🔄 CI Pipeline
This project uses GitHub Actions to:
- Set up Python environment
- Install dependencies
- Run basic import tests
- Ensure code stability on every push



## ☸️ Kubernetes Deployment
- Docker image is deployed using Kubernetes
- Deployment and Service YAML files are located in the `k8s/` directory
- Enables scalability and production-like orchestration



## 📌 Key Learnings
- End-to-end ML pipeline design
- Production-ready ML system development
- API-based inference
- Docker & Kubernetes basics
- CI automation with GitHub Actions



## 📈 Future Improvements
- Add monitoring (Prometheus / Grafana)
- Add model versioning (MLflow)
- Cloud deployment (AWS / GCP / Azure)
- Automated retraining pipeline



## 👤 Author
**Ajeet Sherkar**



## ⭐ If you like this project
Give it a ⭐ on GitHub and feel free to fork or improve it!