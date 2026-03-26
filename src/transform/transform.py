"""
Transformation module for converting raw Pokémon API data into a structured
pandas DataFrame.

This module:
- Loads raw JSON from data/raw/
- Extracts relevant fields from the API response
- Outputs a tidy table to data/processed/
"""

import json
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)

RAW_PATH = Path("data/raw/pokemon_raw.json")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def load_raw(path: str) -> Dict[str, Any]:
    """
    Load raw JSON data from the specified path.

    Args:
        path (str): Full filesystem path to the raw JSON file.

    Returns:
        Dict[str, Any]: Parsed JSON content.
    """
    path = Path(path)

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def extract_records(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract simplified Pokémon records from the raw API response.

    Args:
        data (Dict[str, Any]): Raw JSON dictionary loaded from disk.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing Pokémon names
        and their corresponding API URLs.
    """
    results = data.get("results", [])
    return [
        {
            "name": item["name"],
            "url": item["url"],
        }
        for item in results
    ]


def save_processed(df: pd.DataFrame, path: str) -> str:
    """
    Save processed DataFrame to the specified path.

    Args:
        df (pd.DataFrame): DataFrame to save.
        path (str): Full filesystem path for the output CSV.

    Returns:
        str: Path to the saved file.
    """
    path = Path(path)

    # Ensure parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)
    return str(path)


def main() -> None:
    """
    Execute the transformation step.

    This function:
    - Loads raw JSON data from disk
    - Extracts relevant Pokémon fields
    - Converts the records into a pandas DataFrame
    - Saves the processed dataset to data/processed/
    """
    logger.info("Starting transformation step")
    raw = load_raw()
    records = extract_records(raw)
    df = pd.DataFrame(records)
    path = save_processed(df)
    logger.info(f"Transformation complete: saved to {path}")
