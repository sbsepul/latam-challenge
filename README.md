# LATAM Challenge

by: @sbsepul

## Introduction

This is a project for the LATAM Challenge. The goal is to measure the performance of differents queries in a tweet dataset. In this challenge I choose to use Google Cloud Platform (GCP) to store and process the data.  

The dataset is stored in a Google Cloud Storage bucket and processed using Google BigQuery. The queries are written in SQL and executed using the Google Cloud BigQuery Client Library in Python. The results are saved in the required format.

For the challenge, I have implemented two approaches for each problem: one optimized for time and the other optimized for memory. The time-optimized queries are designed to run faster by using indexes, partitions, and other optimizations. The memory-optimized queries are designed to use less memory by reducing the amount of data loaded into memory and using more efficient data structures.

## Credentials & Data files

To avoid share the credentials and upload the larges files in the repository, I have created a .gitignore file to exclude the files from the repository. The files are:

- `env/`: Folder with credentials.
- `*.csv`: Dataset files.
- `*.json`: Dataset files.

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

1. **Set Up the Environment**: 
    - Create a new project in the Google Cloud Platform (GCP) console.
    - Enable the necessary APIs: Google Cloud Storage, BigQuery.
    - Install the Google Cloud SDK on your local machine and authenticate your account.
    
2. **Data Storage**:
    - Create a Google Cloud Storage bucket to store the tweet dataset.
    - Upload the dataset to the bucket.

3. **Data Processing**:
    - Use Google BigQuery for data processing.
    - Create a new BigQuery dataset and table.
    - Load the tweet dataset from Google Cloud Storage into the BigQuery table.

4. **Querying Data**:
    - Write SQL queries in BigQuery to solve the problems mentioned in the challenge.
    - For each problem, create separate queries to optimize for time and memory.

5. **Python Scripts**:
    - Write Python scripts to execute the BigQuery SQL queries using the Google Cloud BigQuery Client Library.
    - Save the results in the required format.

6. **Jupyter Notebook**:
    - Create a Jupyter Notebook to document and explain the code.
    - Include markdown cells to describe each step and provide insights into the solutions.

7. **Deployment**:
    - Use Google Compute Engine to create a virtual machine for running the Python scripts and Jupyter Notebook if necessary.
    - Ensure the environment is properly configured with all dependencies.

8. **Testing and Validation**:
    - Test the scripts to ensure they run correctly and produce the expected results.
    - Validate the output against sample data to confirm accuracy.