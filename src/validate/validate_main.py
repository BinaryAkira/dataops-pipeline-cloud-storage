"""
Runner module for the validation stage of the data pipeline.

This module:
- Loads processed data
- Applies validation rules
- Logs results and status

It exposes a single public function: run_validate().
"""

from src.validate.validate import load_processed, validate
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run_validate(config: dict) -> None:
    """
    Execute the validation step.

    This function:
    - Loads the processed dataset
    - Runs validation checks
    - Logs success or failure
    """
    logger.info("Starting validation step")

    processed_path = config["local"]["output_path"]

    df = load_processed(processed_path)
    validate(df)

    logger.info("Validation complete")
