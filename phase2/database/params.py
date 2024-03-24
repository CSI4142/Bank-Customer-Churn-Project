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
  location_dim_csv = "location_dimension_table.csv"
  customer_profile_dim_csv = "customer_profile_dim.csv"
  credit_profile_dim_csv = "credit_profile_dim.csv"