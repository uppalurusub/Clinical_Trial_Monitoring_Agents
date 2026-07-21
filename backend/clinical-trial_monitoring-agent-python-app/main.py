import sys
from contextlib import asynccontextmanager

from fastapi import (
    FastAPI,
    Request,
    status
)

from fastapi.responses import JSONResponse

from utils.logger import logger

from routers.monitoring_router import (
    router as monitoring_router
)
from fastapi.middleware.cors import CORSMiddleware


# =====================================================
# Configure Loguru
# =====================================================

logger.remove()

# Console Logger
logger.add(
    sys.stdout,
    colorize=True,
    level="INFO",
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level}</level> | "
        "<cyan>{name}</cyan>:"
        "<cyan>{function}</cyan>:"
        "<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )
)

# File Logger
logger.add(
    "logs/clinical_trial_monitoring.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="DEBUG",
    enqueue=True
)


# =====================================================
# Application Lifespan
# =====================================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info(
        "Starting Clinical Trial Monitoring Agent..."
    )

    logger.success(
        "Application startup completed."
    )

    yield

    logger.info(
        "Shutting down Clinical Trial Monitoring Agent..."
    )

    logger.success(
        "Application shutdown completed."
    )


# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="Clinical Trial Monitoring Agent",
    description="""
Clinical Trial Monitoring System using AutoGen 0.7.5

Features:

- Monitoring Agent
- Risk Agent
- Compliance Agent
- Risk-Based Monitoring (RBM)
- KRI Evaluation
- QTL Assessment
- Compliance Monitoring
- Audit Readiness
- CAPA Recommendations
- CTMS Integration
""",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================================
# Routers
# =====================================================

app.include_router(
    monitoring_router,
    prefix="/api/v1/monitoring",
    tags=["Clinical Trial Monitoring"]
)


# =====================================================
# Root Endpoint
# =====================================================

@app.get("/")
async def root():

    logger.info(
        "Root endpoint accessed."
    )

    return {
        "application":
            "Clinical Trial Monitoring Agent",

        "version":
            "1.0.0",

        "status":
            "running",

        "autogen_version":
            "0.7.5"
    }


# =====================================================
# Application Health Check
# =====================================================

@app.get("/health")
async def health_check():

    logger.info(
        "Application health check requested."
    )

    return {
        "status": "healthy",
        "application":
            "Clinical Trial Monitoring Agent"
    }


# =====================================================
# Global Exception Handler
# =====================================================

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(
        f"Unhandled Exception: {str(exc)}"
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": "Internal Server Error",
            "error": str(exc)
        }
    )


# =====================================================
# Startup Validation Endpoint
# =====================================================

@app.get("/startup-check")
async def startup_check():

    logger.info(
        "Startup validation requested."
    )

    return {
        "success": True,
        "message":
            "Clinical Trial Monitoring Agent is ready."
    }