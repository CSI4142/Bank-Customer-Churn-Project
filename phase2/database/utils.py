import shutil
from params import params

def copy_dim_files_to_tmp():
    """ Copy the dimension files to temporary directory """
    print("Copying dimension files to temporary directory")
    # copy files one by one to the temporary directory
    for file in params.files_to_copy:
        shutil.copy(params.data_dir + file, params.tmp_dir)
    print("Files copied successfully")