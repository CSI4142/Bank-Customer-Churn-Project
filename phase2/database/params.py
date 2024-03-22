# Parameters to control the program
class params:
  # if true, will create tables and take other steps before running the program
  fresh_start = True,
  # if true, will drop all tables
  reset = False
  # database name
  db_name = "bank_customer_churn"
  # base path to the CSV files
  data_dir = "phase2/data/"
  tmp_dir = "/tmp/"
  banking_profile_dim_csv = "banking_profile_dim.csv"
  location_dim_csv = "location_dim.csv"
  customer_profile_dim_csv = "customer_profile_dim.csv"
  churn_fact_table_csv = "churn_fact_table.csv"
  # files to copy to the temporary directory
  # required for staging data to PostgreSQL
  files_to_copy = [
    banking_profile_dim_csv,
    location_dim_csv,
    customer_profile_dim_csv,
    churn_fact_table_csv
  ]