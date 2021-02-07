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
  ![Dataset ](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/database_excel.PNG "Heart Failure Dataset")

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.
The task of this project is classification. The trained ML model aims to determine value of DEATH_EVENT based on the other 12 features. 


### Access

First i downloaded the dataset from kaggle then uploaded and registered the dataset into Azure ML Studio as "heart-failure-sayed".
![Dataset registered](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/dataset_overview.png "Dataset")

Screenshot below shows accessing the dataset in automl python notebook and train python script using Dataset.get_by_name()
![Dataset registered](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/dataset_access_automl.PNG "Accessing dataset in notebook")


## Automated ML

I have specified following settings and configuration for AutoML 
   * task: 'classification' 
        * The aim is to find if a ptient will die or survive. Hence it's a classification task
   * primary_metric: 'Accuracy' 
        * Based on Accuracy metric the AutoML will optimize for model selection. 
   * n_cross_validations: 5
        * It indicates the number of cross validations to be performed. It helps to detect overfitting
   * training_data: my_training_ds 
        * Data to be used for training the model. my_training_ds is a TabularDataset
   * max_concurrent_iterations: 4
        * Rrefers to the maximum number of iterations executed in parallel. I set it to 4 to limit the resource consumption.
   * enable_early_stopping: True
        * It will early terminate if the score does not improve further and save the resource. 
   * label_column_name: 'DEATH_EVENT'
        * label of column that will be predicted by the model.
   * max_cores_per_iteration: -1
        * Refers to The maximum number of threads to be used for training iteration
   * experiment_timeout_minutes: 30
        * Indicates maximum amount of time that all iterations combined can take before the experiment terminates
   
   The screenshot below shows the settings and configuration for AutoML in the Notebook
   ![AutoML config](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/automl_config_settings.PNG "Settings and Config for AutoML")

### Results

Among the trained models through AutoML VotingEnsamble outperformed all other models. The Accuracy of AutoML was 86%. The model can be further improved by enriching the dataset with more data, applying more feature engineering, choosing AUC matrics instead accuracy.

  The screenshot below shows some of the models with higest accuracy
  ![AutoML models](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/automl_models.png "Trained Models through AutoML")
  
  The screenshot below shows All the matrices of the VotingEnsamble model
  ![AutoML](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/best_model_automl_mterics.png "Best Model metrics")
  
  VotingEnsamble model ensambled a number of classifiers to derive the prediction result such as XBoosClassifier, RandomForest, LightGBM, GradientBoosting.
  ![VotingEnsamble](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/tags_bestmodel_automl.PNG "VotingEnsamble Model Detail")
  
  The screenshot below shows AutoML ongoing RunDetails widget
  ![AutoML](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/rundetail_running.png "AutoML RunDetails Running")
  
  The screenshot below shows AutoML RunDetails widget after a successful completion
  ![AutoML](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/runwidget_automl.png "AutoML RunDetails Completed")
  
  The screenshot below shows AutoML completion status with detail information
  ![AutoML](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/automl_completed.png "AutoML Completed")
  
  ![AutoML](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/accuracy_plot_automl.png "AutoML Run Accuracy Plot")
  
  The screenshot below shows registration of the best performing AutoML model. 
  ![AutoML](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/registering_automl.PNG "AutoML Run Accuracy Plot")
  

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search

I chose LogisticRegression model to predict the value of the dependent variable. As it is a classification problem so LogisticRegression can perform better in this regard. 
Among the parameter sampling methods i chose random sampling method where hyperparameter values are randomly selected from the defined search space. It also supports early termination of low-performance runs. Furthermore,for the early stopping policy i chose Bandit policy with slack factor of 0.1, which will terminate runs where the primary metric is not within the specified slack factor compared to the best performing run.

The 2 parameters that i tuned using hyperdrive these are described below:
  * '--C': choice(0.01,5,20,100,500)
       * This parameter is an inverse of regularization strength. Larger values cause weaker and smaller values cause stronger regularization. I chose 0.01,5,20,100,500 and the best model had inverse of regularization strength of 0.01, 500 and 100.
  * '--max_iter': choice(10,50,100,150,200)
       * The discrete values chosen for Max iteration were 10,50,100,150,200. the best model had Max iteration of 100, 150, 50.
          
  ![AutoML](https://github.com/sayed6201/capstone_ML_Azure_nano_degree_/blob/master/screenshots/ps.PNG "Specifying parameter sampler")
          
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
