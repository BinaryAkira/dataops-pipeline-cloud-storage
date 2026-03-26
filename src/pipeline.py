"""
Defines the pipeline workflow (ingest → transform → validate).

This module:
- Coordinates the execution of all pipeline stages
- Provides a single entry point for running the full workflow
- Handles top‑level logging, configuration loading, and error reporting
"""

from src.ingest.ingest_main import run_ingest
from src.transform.transform_main import run_transform
from src.validate.validate_main import run_validate
from src.utils.logger import get_logger
from src.utils.config_loader import load_config

logger = get_logger(__name__)


def run_pipeline() -> None:
    """
    Run the full data pipeline with top‑level error handling.

    This function:
    - Loads the pipeline configuration
    - Executes ingestion, transformation, and validation in sequence
    - Logs the start and end of the pipeline run
    - Captures and logs any unexpected exceptions

    Raises
    ------
    Exception
        Propagates any unhandled exception after logging it.
    """
    logger.info("Pipeline run started")

    try:
        config = load_config()

        run_ingest(config)
        run_transform(config)
        run_validate(config)

        logger.info("Pipeline run completed successfully")

    except Exception as exc:
        logger.error(f"Pipeline run failed: {exc}", exc_info=True)
        raise
