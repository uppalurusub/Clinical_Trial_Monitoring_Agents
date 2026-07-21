# Clinical Trial Monitoring Agent

> AI-Powered Clinical Trial Monitoring System using **FastAPI**, **AutoGen**, **OpenAI**, and **React TypeScript**.

---

# Overview

Clinical Trial Monitoring Agent is an intelligent healthcare application that automates clinical trial monitoring activities using multiple AI agents.

The system evaluates clinical trial monitoring data and generates:

- Monitoring Assessment
- Risk Assessment
- Compliance Assessment
- Key Risk Indicators (KRIs)
- Quality Tolerance Limits (QTLs)
- Risk-Based Monitoring (RBM)
- CAPA Recommendations
- Audit Readiness
- Monitoring Visit Plans

The application consists of:

- FastAPI Backend
- React TypeScript Frontend
- AutoGen Multi-Agent Framework
- OpenAI LLM Integration

---

# System Architecture

```
                 React Frontend
                       │
                Axios REST API
                       │
               FastAPI Backend
                       │
        ┌──────────────┼───────────────┐
        │              │               │
    Router          Service      Implementation
                                       │
                              AutoGen Agent Layer
                                       │
      ┌─────────────┬────────────┬─────────────┐
      │             │            │
 Monitoring     Risk Agent   Compliance Agent
      │             │            │
      └─────────────┴────────────┘
                    │
             OpenAI GPT Models
```

---

# Project Structure

```
Clinical_Trial_Monitoring_Agent/

│
├── backend/
│   ├── clinical-trial_monitoring-agent-python-app/
│   │
│   ├── agents/
│   ├── config/
│   ├── implementation/
│   ├── memory/
│   ├── models/
│   ├── routers/
│   ├── services/
│   ├── utils/
│   ├── logs/
│   ├── main.py
│   └── requirements.txt
│
└── ui/
    └── reactjs/
        └── clinical-trial_monitoring-agent-reactjs-app/
            ├── src/
            │   ├── api/
            │   ├── components/
            │   ├── models/
            │   ├── App.tsx
            │   └── main.tsx
            ├── package.json
            └── vite.config.ts
```

---

# Features

## AI Multi-Agent Monitoring

- Monitoring Agent
- Risk Agent
- Compliance Agent

---

## Clinical Monitoring

- Site Monitoring
- Study Monitoring
- Protocol Compliance
- Monitoring Visit Planning
- Monitoring Summary

---

## Risk Assessment

- Risk-Based Monitoring (RBM)
- Site Risk Evaluation
- Critical Finding Detection
- Quality Risk Analysis
- Risk Recommendations

---

## Compliance Monitoring

- Protocol Compliance
- GCP Compliance
- Regulatory Assessment
- Audit Readiness
- CAPA Recommendations

---

## Healthcare Features

- Key Risk Indicators (KRIs)
- Quality Tolerance Limits (QTLs)
- Clinical Site Performance
- Monitoring Visit Scheduling
- AI Generated Recommendations

---

# Technology Stack

## Backend

- Python
- FastAPI
- AutoGen 0.7.5
- OpenAI
- Loguru
- Uvicorn
- MLflow
- Python Dotenv

---

## Frontend

- React 19
- TypeScript
- Vite
- Axios
- React Markdown
- Lucide React

---

# Backend Installation

## Clone Repository

```bash
git clone <repository-url>

cd Clinical_Trial_Monitoring_Agent/backend
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example

```text
OPENAI_API_KEY=your_api_key
MODEL_NAME=gpt-4o-mini
```

---

## Run Backend

```bash
cd clinical-trial_monitoring-agent-python-app

uvicorn main:app --reload
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Frontend Installation

Navigate to the React application.

```bash
cd ui/reactjs/clinical-trial_monitoring-agent-reactjs-app
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# API Endpoints

## Root

```
GET /
```

Returns application information.

---

## Monitoring Analysis

```
POST /api/v1/monitoring/analyze
```

Performs AI-powered clinical trial monitoring analysis.

---

## Health Check

```
GET /api/v1/monitoring/health
```

Returns application health status.

---

## Service Information

```
GET /api/v1/monitoring/info
```

Returns application metadata.

---

# Sample Request

```json
{
  "study_id": "STUDY-001",
  "site_id": "SITE-001",
  "monitoring_data": {
    "protocol_deviations": 2,
    "missing_documents": 1,
    "open_queries": 6
  }
}
```

---

# Sample Response

```json
{
  "monitoring_assessment": "...",
  "risk_assessment": "...",
  "compliance_assessment": "...",
  "visit_plan": "...",
  "recommendations": "..."
}
```

---

# Logging

Application logs are stored in

```
logs/
```

Including

- clinical_trial_monitoring.log
- healthcare.log
- error.log

---

# Layered Architecture

```
Router

↓

Service

↓

Implementation

↓

AutoGen Agents

↓

OpenAI

↓

Response Models
```

---

# Frontend Components

- Monitoring Form
- Monitoring Results
- JSON Viewer
- Status Banner
- Service Information Panel

---

# Backend Modules

- Agents
- Configuration
- Router
- Service
- Implementation
- Models
- Utilities
- Memory
- Logging

---

# Security

- Environment Variable Configuration
- CORS Enabled
- Request Validation using Pydantic
- Structured Exception Handling
- Centralized Logging

---

# Future Enhancements

- CTMS Integration
- EDC Integration
- eTMF Integration
- Risk Dashboard
- Site Performance Analytics
- Monitoring Trend Visualization
- Email Notifications
- Role-Based Authentication
- Docker Support
- Kubernetes Deployment
- Azure OpenAI Support

---

# Use Cases

- Clinical Trial Monitoring
- Site Risk Assessment
- Regulatory Compliance
- Audit Preparation
- Quality Oversight
- Risk-Based Monitoring
- Clinical Operations
- CRO Monitoring
- Sponsor Oversight

---

# Author

Clinical Trial Monitoring Agent

Built using:

- FastAPI
- AutoGen
- OpenAI
- React
- TypeScript
- Vite

---

# License

This project is intended for educational, research, and healthcare AI demonstration purposes.