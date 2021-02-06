*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Heart Failure Prediction

The Machine Learning models were trained using Kaggle's Heart Failure Clinical [Datset](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data). The models were trained using Azure AutoML as well as Hyperdrive. One of the best performing model was then deployed to Azure Container Instance as a Web Service.

## Project Set Up and Installation

  1. Create compute instance and compute cluster in Azure
      ![Cluster](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/cluster.png "Created compute cluster configuration")
         
  2. Download the Heart Failure Clinical [Datset](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) and upload it in Azure
      ![Dataset registered](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/dataset_create.PNG "Uloading dataset from local to Azure")
      
  3. Import the Dataset into the Notebooks
  
  4. Import the dependencies and run all the cells

## Dataset

### Overview
The Heart Failure Dataset used in this project can be found in [Kaggle](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data). The Heart failure dataset has total 13 columns which are age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure,	platelets, serum_creatinine,	serum_sodium, sex,	smoking,	time and	DEATH_EVENT. The dependent vaiable is DEATH_EVENT.


### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.
The task of this project is classification. The trained ML model aims to determine value of DEATH_EVENT.


### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
