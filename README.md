# Clinical Trial Monitoring Agent

## Overview

The **Clinical Trial Monitoring Agent** is an AI-powered clinical operations application built using **FastAPI**, **AutoGen 0.7.5**, and **Loguru** for intelligent monitoring of clinical trial sites.

The system automates Risk-Based Monitoring (RBM), compliance evaluation, site risk assessment, Quality Tolerance Limit (QTL) monitoring, Key Risk Indicator (KRI) analysis, audit readiness evaluation, and CAPA (Corrective and Preventive Action) recommendations.

It leverages multiple collaborating AI agents to assist Clinical Research Associates (CRAs), Clinical Trial Managers (CTMs), Sponsors, CROs, and Quality Assurance teams in making faster and more consistent monitoring decisions.

---

# Features

- Multi-Agent Clinical Trial Monitoring
- Risk-Based Monitoring (RBM)
- Site Risk Assessment
- KRI (Key Risk Indicator) Evaluation
- QTL (Quality Tolerance Limit) Monitoring
- Protocol Compliance Assessment
- Site Performance Monitoring
- Safety Monitoring
- Data Quality Monitoring
- Audit Readiness Assessment
- Monitoring Visit Planning
- CAPA Recommendations
- CTMS Integration Ready
- REST API
- Structured Logging using Loguru
- AutoGen 0.7.5 Agent Collaboration

---

# AI Agents

The application consists of three specialized AI agents.

## 1. Monitoring Agent

Responsible for:

- Site monitoring assessment
- Enrollment evaluation
- Data quality review
- Monitoring findings analysis
- Visit planning
- Operational monitoring summary

---

## 2. Risk Agent

Responsible for:

- Overall risk scoring
- Site risk assessment
- Safety risk
- Compliance risk
- Data quality risk
- KRI evaluation
- QTL breach assessment
- Risk categorization

---

## 3. Compliance Agent

Responsible for:

- Protocol compliance
- Informed consent compliance
- Training compliance
- Audit readiness
- Monitoring finding assessment
- CAPA recommendations

---

# Project Architecture

```
                    +----------------------+
                    |     REST API         |
                    |     FastAPI          |
                    +----------+-----------+
                               |
                               |
                +--------------+--------------+
                | Monitoring Service          |
                +--------------+--------------+
                               |
                +--------------+--------------+
                | Monitoring Implementation   |
                +--------------+--------------+
                               |
        +----------------------+----------------------+
        |                      |                      |
+---------------+      +---------------+     +---------------+
|MonitoringAgent|      |  Risk Agent   |     |ComplianceAgent|
+---------------+      +---------------+     +---------------+
        |                      |                      |
        +---------- AutoGen Multi-Agent --------------+
                               |
                        Final Assessment
```

---

# Project Structure

```
Clinical_Trial_Monitoring_Agent/
│
├── app/
│   ├── agents/
│   │      monitoring_agents.py
│   │
│   ├── config/
│   │      llm_config.py
│   │      llm_models_config.py
│   │
│   ├── implementation/
│   │      monitoring_impl.py
│   │
│   ├── memory/
│   │      coding_memory.py
│   │
│   ├── models/
│   │      request_model.py
│   │      response_model.py
│   │
│   ├── routers/
│   │      monitoring_router.py
│   │
│   ├── services/
│   │      monitoring_service.py
│   │
│   ├── utils/
│   │      logger.py
│   │      json_utils.py
│   │      prompt_templates.py
│   │
│   └── main.py
│
├── logs/
├── requirements.txt
├── monitoring_analyze_request.json
└── README.md
```

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python 3.11+ |
| REST API | FastAPI |
| AI Framework | AutoGen 0.7.5 |
| LLM | OpenAI Compatible Models |
| Logging | Loguru |
| Model Tracking | MLflow |
| Validation | Pydantic |
| API Documentation | Swagger UI |

---

# Clinical Monitoring Workflow

```
Clinical Site Metrics
        │
        ▼
Request Validation
        │
        ▼
Metric Calculation
        │
        ▼
Risk Score Calculation
        │
        ▼
Monitoring Agent
        │
        ▼
Risk Agent
        │
        ▼
Compliance Agent
        │
        ▼
Recommendation Engine
        │
        ▼
Final Monitoring Report
```

---

# Monitoring Metrics

The system calculates various operational metrics.

## Enrollment Metrics

- Enrollment Rate
- Screen Failure Rate
- Randomization Rate
- Dropout Rate

---

## Data Quality Metrics

- Missing Data Rate
- Protocol Deviation Rate
- Query Resolution Rate
- Open Query Count
- Overdue Queries

---

## Safety Metrics

- Adverse Event Rate
- Serious Adverse Event Rate
- SUSAR Rate

---

## Compliance Metrics

- Compliance Score
- Training Completion
- SDV Completion
- Informed Consent Compliance

---

## Monitoring Metrics

- Monitoring Findings
- Critical Findings
- Major Findings
- Minor Findings
- Days Since Last Visit

---

# Risk Assessment

The implementation generates an overall risk score based on monitoring metrics.

Typical risk categories include:

| Risk Score | Level |
|------------|---------|
| 0–25 | Low |
| 26–50 | Moderate |
| 51–75 | High |
| 76–100 | Critical |

The assessment considers:

- Enrollment performance
- Protocol deviations
- Missing data
- Open queries
- Safety events
- Compliance score
- Monitoring findings
- KRI triggers
- QTL breaches

---

# Compliance Assessment

The compliance agent evaluates:

- Protocol adherence
- Training completion
- Informed consent
- SDV completion
- Audit readiness
- Monitoring findings

---

# Monitoring Visit Planning

The system recommends:

- Remote Monitoring
- On-site Monitoring
- Triggered Visit
- Routine Visit
- Immediate Visit

It also determines:

- Visit priority
- Visit window
- Monitoring strategy

---

# API Endpoints

## Root

```
GET /
```

Returns application information.

---

## Health

```
GET /health
```

Returns application health.

---

## Startup Validation

```
GET /startup-check
```

Checks application readiness.

---

## Monitoring Service Health

```
GET /api/v1/monitoring/health
```

---

## Service Information

```
GET /api/v1/monitoring/info
```

Returns:

- Framework
- AutoGen version
- Agents
- Capabilities

---

## Clinical Trial Monitoring

```
POST /api/v1/monitoring/analyze
```

Performs complete monitoring analysis.

---

# Sample Request

```json
{
  "study_id": "STUDY-001",
  "study_name": "Phase III Diabetes Trial",
  "site_id": "SITE-101",
  "site_name": "Apollo Research Center",
  "investigator_name": "Dr. John Smith",
  "country": "India",

  "screened_subjects": 150,
  "enrolled_subjects": 120,
  "randomized_subjects": 110,
  "dropout_subjects": 8,

  "protocol_deviations": 5,
  "major_protocol_deviations": 1,
  "minor_protocol_deviations": 4,

  "missing_data_points": 12,
  "open_queries": 15,
  "overdue_queries": 3,

  "adverse_events": 20,
  "serious_adverse_events": 2,
  "suspected_unexpected_serious_adverse_reactions": 1,

  "compliance_score": 94,
  "training_completion_rate": 98,
  "informed_consent_compliance": 100,
  "source_data_verification_rate": 97,

  "last_monitoring_visit_date": "2026-06-01",
  "days_since_last_visit": 24,

  "monitoring_findings": 7,
  "critical_findings": 0,
  "major_findings": 1,
  "minor_findings": 6,

  "risk_indicator_score": 32,
  "quality_tolerance_limit_breaches": 1,
  "key_risk_indicators_triggered": 2
}
```

---

# Sample Response

```json
{
  "success": true,
  "study_id": "STUDY-001",
  "site_id": "SITE-101",
  "site_name": "Apollo Research Center",
  "monitoring_status": "Completed",

  "monitoring_metrics": {
    "enrollment_rate": 80,
    "dropout_rate": 6.7,
    "protocol_deviation_rate": 4.2,
    "missing_data_rate": 10,
    "query_resolution_rate": 80,
    "compliance_score": 94
  },

  "risk_assessment": {
    "risk_score": 34,
    "risk_level": "Moderate"
  },

  "compliance_assessment": {
    "compliance_status": "Compliant",
    "audit_readiness_status": "Ready"
  },

  "monitoring_visit_plan": {
    "recommended_visit_type": "Remote Monitoring",
    "recommended_visit_within_days": 30
  },

  "recommendations": [
    {
      "category": "Data Quality",
      "priority": "Medium",
      "recommendation": "Resolve overdue data queries."
    }
  ]
}
```

---

# Installation

Clone the repository.

```bash
git clone <repository-url>

cd Clinical_Trial_Monitoring_Agent
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
uvicorn app.main:app --reload
```

Application URL

```
http://localhost:8000
```

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Logging

The application uses **Loguru**.

Generated logs include:

```
logs/
    clinical_trial_monitoring.log
```

Features:

- Console logging
- File logging
- Rotation (10 MB)
- Retention (30 Days)
- Compression
- Exception tracking

---

# Future Enhancements

- Real CTMS integration
- EDC integration
- RBQM dashboards
- Predictive site risk models
- Centralized monitoring
- Remote SDV support
- Sponsor dashboard
- Site benchmarking
- Monitoring analytics
- ML-based risk prediction
- Power BI integration
- Email notifications
- CAPA workflow automation

---

# Version

**Current Version**

```
1.0.0
```

---

# Author

Clinical Trial Monitoring Agent

Built using:

- FastAPI
- AutoGen 0.7.5
- OpenAI Compatible LLMs
- Loguru
- MLflow

Designed for modern AI-assisted clinical trial monitoring, enabling proactive risk identification, compliance management, and intelligent monitoring decisions.