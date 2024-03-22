# CSI4142 - Project - Bank Customer Churn Analysis

The Bank Customer Churn project aims to carry out an extensive exploration of the customer churn data of the ABC Multistate Bank using various data science techniques and analytical tools.

The steps involved will range from developing a dimensional model to better display the data characteristics and analysis process, to building data marts and performing the ETL process. Online Analytical Processing (OLAP) will also be used to perform multi-dimensional data analysis, followed by the development of Business Intelligence (BI) dashboards for data visualization and trend identification.

Finally, we will use data mining techniques to discover hidden patterns, classify data, and develop a machine learning (ML) model to predict customer churn.

- [CSI4142 - Project - Bank Customer Churn Analysis](#csi4142---project---bank-customer-churn-analysis)
  - [End Goal](#end-goal)
  - [Setup](#setup)
  - [Data Loading](#data-loading)
  - [Data Staging](#data-staging)
    - [Parameters](#parameters)
    - [Staging Data](#staging-data)
  - [References](#references)
  - [Project Team](#project-team)

## End Goal

The results of this project could help enhance customer retention strategies, optimize business profitability, and improve overall customer satisfaction by identifying key factors leading to churn in the banking industry.

## Setup

If you wish to run the data loading and/or data staging process locally, you can follow the instructions below.

Please note, all commands are to be run from the **root** directory of the project, and only **Unix-based** (linux, macOS, etc.) systems are supported. You may need to adjust the commands & the program code for **Windows**.

We will need certain python libraries to run the loading and staging process. Before, installing the required libraries, you may activate a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To install the required libraries, you can run the following command:

```bash
pip install -r requirements.txt
```

Before, we can move onto staging the data, it is necessary to ensure you have PostreSQL installed and setup correctly.

To install PostgreSQL, you check the instructions [here](https://www.postgresql.org/download/).

## Data Loading

The data loading process involves the ingestion of the source CSV file for the creation a separate **CSV** format file for each of the dimensions. These files can be used to stage the data into the database as dimension tables.

The source CSV file and the dimension files have already been created and our located in the `phase2/data/` folder.

**Source CSV File**: `Customer-Churn-Records.csv`

If you wish to create the dimension files yourself, you can follow the instructions below.

To create CSV files for each of the dimension, you may run the appropriate python notebook from folder `phase2/notebooks/`.

Each of these notebooks create an output CSV file in the `phase2/data/` folder. These files can be used to stage the data into the database.

Please ensure you have the required libraries installed before running the notebooks. You can follow the instruction given [here](#setup).

## Data Staging

The data staging process involves the creation a separate **CSV** format file for each of the dimensions, and then staging of these files into the database as dimension tables. Once, all dimension tables have been staged, the fact table is created.

To do this locally, please follow the instructions below.

### Parameters

Before we can connect to the PostgreSQL server and create the database, please ensure you have the correct values in both of the following files:

1. `.env`: This file specifies the parameters required to connect to the PostgreSQL server.
2. `phase2/database/params.py`: This file specifies several parameters for the program, like the name of the database to be created, the location of CSV files, etc.

To run a fresh start of the program, i.e., create new database and tables, you can set the `fresh_start` parameter in `phase2/database/params.py` to `True`.

### Staging Data

To stage the CSV file data into database as tables, you can run the following python program from the **root** directory of the project.

```bash
python phase2/database/db.py
```

## References

Bank Customer Churn Dataset - https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data

## Project Team

**Group 51**

- Dhara Patel (300146860)
- Oleksander Turchyn (300174825)
- Pranav Kural (300241227)
