### Project Description

The "Diabetes Classification" project aims to build a machine learning model to classify patients based on various health metrics, focusing on diabetes diagnosis. The dataset includes features like age, gender, urea level, creatinine level, HbA1c level, cholesterol levels, triglycerides, high-density lipoprotein (HDL), low-density lipoprotein (LDL), very low-density lipoprotein (VLDL), and body mass index (BMI). The model is designed to help in predicting the likelihood of diabetes, aiding healthcare professionals in early detection and management.

### Project Function

The project involves several steps:

1. **Data Loading and Preprocessing**:
    
    - Load the dataset and handle missing values and duplicates.
    - Drop unnecessary columns (`ID` and `No_Pation`).
    - Correct any data inconsistencies, such as uniforming gender representation.
2. **Exploratory Data Analysis (EDA)**:
    
    - Analyze the distribution and unique values of categorical variables.
    - Visualize the distribution of various features using seaborn and matplotlib.
3. **Feature Selection and Engineering**:
    
    - Select relevant features for model training.
    - Apply transformations and scaling to the features.
4. **Model Training**:
    
    - Split the dataset into training and testing sets.
    - Use the SMOTE technique to handle class imbalances in the training set.
    - Train a Decision Tree Classifier using a pipeline that includes transformations and feature selection.
5. **Hyperparameter Tuning**:
    
    - Perform hyperparameter tuning using GridSearchCV with cross-validation to find the best parameters for the Decision Tree model.
6. **Model Evaluation**:
    
    - Evaluate the model's performance on training and testing sets using metrics such as recall and f1-score.
    - Save the best model using joblib for future use.
7. **Deployment**:
    
    - Provide a script to deploy the model using Streamlit for an interactive user interface.
