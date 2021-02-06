from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Dataset
import joblib
from azureml.core.workspace import Workspace

try:
    ws = Workspace(subscription_id = "a24a24d5-8d87-4c8a-99b6-91ed2d2df51f", resource_group = "aml-quickstarts-137382", workspace_name = "quick-starts-ws-137382")
    # write the details of the workspace to a configuration file to the notebook library
    ws.write_config()
    print("Workspace configuration succeeded. Skip the workspace creation steps below")
except:
    print("Workspace not accessible. Change your parameters or create a new workspace below")

run = Run.get_context()

def clean_data(data):
    y_df = data['DEATH_EVENT']
    x_df = data.drop(['DEATH_EVENT'], axis=1)
    return x_df, y_df

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()
    
    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))
    
    # Importing the dataset
    ds = Dataset.get_by_name(ws, name='heart-failure-sayed')
    data = ds.to_pandas_dataframe()
    
    # preparing the dataset
    x, y = clean_data(data)
    
    #Spliting the dataset into train and test sets.
    x_train, x_test = train_test_split(x, test_size=0.2, random_state=111)
    y_train, y_test = train_test_split(y, test_size=0.2, random_state=111)
    
    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)
    
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/mymodel.joblib')
    
    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()
