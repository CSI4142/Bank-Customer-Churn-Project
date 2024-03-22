# CSI4142 - Project - Bank Customer Churn Analysis

The Bank Customer Churn project aims to carry out an extensive exploration of the customer churn data of the ABC Multistate Bank using various data science techniques and analytical tools.

The steps involved will range from developing a dimensional model to better display the data characteristics and analysis process, to building data marts and performing the ETL process. Online Analytical Processing (OLAP) will also be used to perform multi-dimensional data analysis, followed by the development of Business Intelligence (BI) dashboards for data visualization and trend identification.

Finally, we will use data mining techniques to discover hidden patterns, classify data, and develop a machine learning (ML) model to predict customer churn.

## End Goal

The results of this project could help enhance customer retention strategies, optimize business profitability, and improve overall customer satisfaction by identifying key factors leading to churn in the banking industry.

## Data Staging

Before you can upload CSV file data into tables, you need to copy the CSV files into the "temp" folder on your device.

For MacOS or Linux:

```bash
cp <path_to_csv_file> /tmp/
```

For Windows:

```cmd
copy <path_to_csv_file> C:\Temp\
```

After this is done, you can run the program:

```bash
python phase2/database/db.py
```

You may activate a virtual environment before running the above command.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Please ensure you have the required libraries installed. If not, you can install them using the following command:

```bash
pip install -r requirements.txt
```

## References

Bank Customer Churn Dataset - https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data

## Project Team

**Group 51**

- Dhara Patel (300146860)
- Oleksander Turchyn (300174825)
- Pranav Kural (300241227)
