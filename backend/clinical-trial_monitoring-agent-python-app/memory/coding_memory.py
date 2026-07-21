from typing import Dict, List, Optional
from datetime import datetime
from utils.logger import logger


class CodingMemory:
    """
    In-Memory Storage for Medical Coding Assistant

    Stores:
    - Coding Requests
    - ICD Recommendations
    - Validation Results
    - Audit Results
    """

    def __init__(self):
        self._coding_history: List[Dict] = []

        logger.info(
            "Medical Coding Memory Initialized"
        )

    def save_coding_result(
        self,
        coding_result: Dict
    ) -> None:
        """
        Save coding result
        """

        try:

            record = {
                "timestamp": datetime.utcnow().isoformat(),
                "data": coding_result
            }

            self._coding_history.append(record)

            logger.success(
                f"Coding Result Saved | "
                f"Patient ID: "
                f"{coding_result.get('patient_id')}"
            )

        except Exception as ex:

            logger.exception(
                f"Error Saving Coding Result: {str(ex)}"
            )

    def get_all_results(self) -> List[Dict]:
        """
        Retrieve all coding history
        """

        logger.info(
            f"Retrieving "
            f"{len(self._coding_history)} "
            f"Coding Records"
        )

        return self._coding_history

    def get_patient_history(
        self,
        patient_id: str
    ) -> List[Dict]:
        """
        Retrieve coding history by patient
        """

        try:

            history = [
                record
                for record in self._coding_history
                if record["data"].get(
                    "patient_id"
                ) == patient_id
            ]

            logger.info(
                f"Found {len(history)} "
                f"records for Patient "
                f"{patient_id}"
            )

            return history

        except Exception as ex:

            logger.exception(
                f"Patient History Error: {str(ex)}"
            )

            return []

    def get_latest_result(
        self,
        patient_id: str
    ) -> Optional[Dict]:
        """
        Retrieve latest coding result
        """

        try:

            patient_records = self.get_patient_history(
                patient_id
            )

            if not patient_records:

                logger.warning(
                    f"No records found for "
                    f"Patient {patient_id}"
                )

                return None

            latest = sorted(
                patient_records,
                key=lambda x: x["timestamp"],
                reverse=True
            )[0]

            logger.info(
                f"Latest record retrieved "
                f"for Patient {patient_id}"
            )

            return latest

        except Exception as ex:

            logger.exception(
                f"Latest Result Error: {str(ex)}"
            )

            return None

    def get_total_coding_requests(
        self
    ) -> int:
        """
        Total coding requests processed
        """

        count = len(self._coding_history)

        logger.info(
            f"Total Coding Requests: {count}"
        )

        return count

    def get_average_confidence_score(
        self
    ) -> float:
        """
        Average ICD coding confidence
        """

        try:

            scores = []

            for record in self._coding_history:

                codes = (
                    record["data"]
                    .get("icd_codes", [])
                )

                for code in codes:

                    score = code.get(
                        "confidence_score",
                        0
                    )

                    scores.append(score)

            if not scores:

                return 0.0

            avg_score = round(
                sum(scores) / len(scores),
                4
            )

            logger.info(
                f"Average Confidence "
                f"Score: {avg_score}"
            )

            return avg_score

        except Exception as ex:

            logger.exception(
                f"Confidence Score Error: "
                f"{str(ex)}"
            )

            return 0.0

    def clear_memory(self) -> None:
        """
        Clear all memory
        """

        count = len(self._coding_history)

        self._coding_history.clear()

        logger.warning(
            f"Memory Cleared. "
            f"Removed {count} Records"
        )


coding_memory = CodingMemory()