# LATAM Challenge

by: @sbsepul

## Introduction

This is a project for the LATAM Challenge. The goal is to measure the performance of differents queries in a tweet dataset. In this challenge I choose to use Google Cloud Platform (GCP) to store and process the data.  

The dataset is stored in a Google Cloud Storage bucket and processed using Google BigQuery. The queries are written in SQL and executed using the Google Cloud BigQuery Client Library in Python. The results are saved in the required format.

For the challenge, I have implemented two approaches for each problem: one optimized for time and the other optimized for memory. The time-optimized queries are designed to run faster by using indexes, partitions, and other optimizations. The memory-optimized queries are designed to use less memory by reducing the amount of data loaded into memory and using more efficient data structures.

## Credentials & Data files

To avoid share the credentials and upload the larges files in the repository, I have created a .gitignore file to exclude the files from the repository. The files are:

- `*.env`: File with credentials.
- `*.dat`: Memory profile files.
- `*.zip`: Dataset files.
- `*.csv`: Dataset files.
- `*.json`: Dataset files.

The credentials file is a .env file with the structure of `.env.example` file.

In the `env/` folder is recommended to save the credentials file.

## Requirements

The requirements are saved in the `requirements.txt` file. The file is created using the `pip-chill` package.

## Dependencies added

For the challenge:

- google-cloud-bigquery: To interact with BigQuery.
- google-cloud-storage: To interact with Google Cloud Storage.
- pandas: To work with dataframes.
- memory-profiler: To profile memory usage.
- py-spy: To profile time usage.

For clean the environment:
- ruff: To sort the imports, format the code and check for errors.
- isort: To sort the imports.
- pre-commit: To run the hooks before commit.

For requirements:
- pip-chill: To create the requirements file.

## Installation

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

With conda environment:

```bash
conda env create -f environment.yml
```

Is recommended to use a conda environment but install the dependencies with pip.

## Project Structure

The project has the following structure:

1. `q(i)_time.py`: Time-optimized query for problem i. The content file is the best solution for the problem.
2. `q(i)_memory.py`: Memory-optimized query for problem i. The content file is the best solution for the problem.
3. `q(i)_memory_large.py`: Memory query used for the original data.
4. `challenge.py`: Main file with the functions to run the queries.

The data is stored directly in `src/` folder.