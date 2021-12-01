# NOTE: For windows user-
# This file must be created in the root of the project
# where Training and Prediction batch file as are present

import os
from glob import glob


data_dirs = ["Training_Batch_Files","Prediction_Batch_files","Prediction_Output_File"]
# data_dirs=['Prediction_Output_File']
for data_dir in data_dirs:
    files = glob(data_dir + r"/*.csv")
    for filePath in files:
        # print(f"dvc add {os.path.join((filePath))}")
        # print(files)
        os.system(f"git rm -r --cached {filePath}")
        os.system(f"dvc add {filePath}")

        # print("Success")


print("\n #### all files added to dvc ####")
# D:\Full Stack Data Science\ML Projects\Heroku Deployment\MLOPS\WaferFaultDetection\DvcAddData.py