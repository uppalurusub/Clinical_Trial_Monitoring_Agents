from fastapi import (
    APIRouter,
    HTTPException,
    status
)

from utils.logger import logger

from services.monitoring_service import (
    MonitoringService
)

from models.request_model import (
    MonitoringRequest
)

from models.response_model import (
    MonitoringResponse
)

router = APIRouter()

monitoring_service = MonitoringService()


@router.post(
    "/analyze",
    response_model=MonitoringResponse,
    summary="Clinical Trial Monitoring Analysis",
    description="""
    Analyze clinical trial site monitoring data using:

    - Monitoring Agent
    - Risk Agent
    - Compliance Agent

    Provides:
    - Monitoring Assessment
    - Risk Assessment
    - Compliance Assessment
    - Monitoring Visit Plan
    - Recommendations
    """
)
async def analyze_monitoring(
    request: MonitoringRequest
):
    """
    Clinical Trial Monitoring Analysis
    """

    try:

        logger.info(
            f"Received monitoring request "
            f"for Study={request.study_id}, "
            f"Site={request.site_id}"
        )

        response = (
            await monitoring_service
            .analyze_monitoring(request)
        )

        logger.success(
            f"Monitoring analysis completed "
            f"for Site={request.site_id}"
        )

        return response

    except ValueError as ex:

        logger.error(
            f"Validation Error: {str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex)
        )

    except Exception as ex:

        logger.exception(
            f"Monitoring analysis failed: {str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get(
    "/health",
    summary="Monitoring Service Health Check"
)
async def health_check():
    """
    Health Check Endpoint
    """

    try:

        logger.info(
            "Health check request received."
        )

        response = (
            await monitoring_service
            .health_check()
        )

        logger.success(
            "Health check completed."
        )

        return response

    except Exception as ex:

        logger.exception(
            f"Health check failed: {str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )


@router.get(
    "/info",
    summary="Monitoring Service Information"
)
async def service_info():
    """
    Service Metadata
    """

    try:

        logger.info(
            "Service info requested."
        )

        return {
            "application":
                "Clinical Trial Monitoring Agent",

            "version":
                "1.0.0",

            "framework":
                "FastAPI",

            "autogen_version":
                "0.7.5",

            "agents": [
                "Monitoring Agent",
                "Risk Agent",
                "Compliance Agent"
            ],

            "capabilities": [
                "Risk-Based Monitoring",
                "Site Monitoring",
                "Protocol Compliance",
                "Audit Readiness",
                "KRI Assessment",
                "QTL Assessment",
                "CAPA Recommendations"
            ]
        }

    except Exception as ex:

        logger.exception(
            f"Service info failed: {str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )