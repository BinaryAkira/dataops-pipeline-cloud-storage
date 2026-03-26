# DataOps Pipeline

## Overview

This repository demonstrates a simple data engineering pipeline using Python. It is designed for beginners and shows how raw data can be ingested, transformed, validated, and saved in a structured way.

## What is a Data Pipeline?

A data pipeline is a series of steps that move and process data from one place to another. In this project, the pipeline:
- Loads raw data (e.g., Pokémon information)
- Cleans and transforms the data into a usable format
- Validates the processed data for quality
- Saves the final dataset for further analysis

## Project Structure

- `data/`: Contains raw and processed data files.
  - `raw/`: Where the original data (e.g., JSON files) is stored.
  - `processed/`: Where cleaned and transformed data (e.g., CSV files) is saved.
- `src/`: Source code for the pipeline.
  - `ingest/`: Code to load raw data.
  - `transform/`: Code to clean and reshape the data.
  - `validate/`: Code to check data quality.
  - `utils/`: Helper functions (like logging).
  - `pipeline.py`: Orchestrates the entire pipeline.
- `main.py`: Entry point to run the pipeline.
- `requirements.txt`: Lists Python packages needed.
- `logs/`: Stores logs about pipeline execution.

## How the Pipeline Works

1. **Ingest**: Loads raw data from disk.
2. **Transform**: Cleans and restructures the data (e.g., extracts relevant fields, converts formats).
3. **Validate**: Checks the processed data for errors or inconsistencies.
4. **Save**: Writes the final, clean dataset to disk.

## Setting Up a Virtual Environment (venv)

A virtual environment helps keep your project’s dependencies isolated from other Python projects. Here’s how to create and activate one:

1. Open a terminal or command prompt in your project folder.
2. Create a virtual environment:
   ```
   python -m venv pipeline-venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     pipeline-venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source pipeline-venv/bin/activate
     ```

Once activated, your terminal will show the environment name (e.g., `(pipeline-venv)`). Now you can install packages and run your code safely.

## Getting Started

1. Activate your virtual environment (see above).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the pipeline:
   ```
   python main.py
   ```

## Testing: What, Why, and How

### What Are Tests?
Tests are small programs that check if your code works as expected. They help catch mistakes early and ensure your pipeline produces correct results.

### Why Use Tests?
- Find bugs before they affect your data
- Make changes confidently, knowing tests will catch errors
- Improve code quality and reliability

### Where Are Tests?
- The `tests/` folder contains test files for different parts of the pipeline.
- Each test checks a specific function or module.

### How to Run Tests
1. Make sure your virtual environment is activated.
2. Install test dependencies (already listed in `requirements.txt`, e.g., `pytest`):
   ```
   pip install -r requirements.txt
   ```
3. Run all tests with:
   ```
   pytest
   ```

### Best Practices: Project Structure
- Keeping code organized in folders (`src/`, `tests/`, `data/`) makes it easier to maintain and scale.
- Separating tests from main code helps you focus on development and quality independently.
- Using a clear structure is a standard in professional projects and helps others understand your code quickly.

By following these practices, your pipeline is easier to debug, extend, and share with others.

## Why Use a Pipeline?

- Makes data processing repeatable and reliable.
- Helps organize code and data for easy maintenance.
- Ensures data quality before analysis.
