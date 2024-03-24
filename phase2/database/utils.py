import shutil
from params import params

def copy_dim_files_to_tmp():
    """ Copy the dimension files to temporary directory """
    print("Copying dimension files to temporary directory")
    files_to_copy = [
        params.banking_profile_dim_csv,
        params.location_dim_csv,
        params.customer_profile_dim_csv,
        params.credit_profile_dim_csv
    ]
    # source directory
    source_dir = params.data_dir
    # copy files one by one to the temporary directory
    for file in files_to_copy:
        shutil.copy(source_dir + file, params.tmp_dir)
    print("Files copied successfully")