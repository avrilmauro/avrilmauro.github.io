# Personal Portfolio 📚

## Employee Attrition Machine Learning Project 🏃💼
https://github.com/avrilmauro/avrilmauro.github.io/blob/main/employee_attrition_project.ipynb
- **Question**: what drives an employee to leave a company?
- **Dataset**: [IBM HR Analytics Employee Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **Pre-Processing**: removed constant and arbitrary columns, encoded categorical variables, and ran scale-normalization.
- **Method**: use a `Random Forest Classifer` to predict if an employee will stay (attrition='No') or leave (attrition='Yes') and compute its cross-validated accuracy score
    - *Problems*: the model was outputting many false negatives in the confusion matrix
    - *Hypothesis*: our dataset has significantly more entries from employees who stayed rather than left, so the the fitting of the classifier is unbalanced
    - *Troubleshoot*: (1) compare the model's performance (accuracy, precision, and sensitivity scores) to a K-Nearest Neighbors Classifier and Decision Tree Classifier, and (2) change the Random Forest Classifier's class_weights to 'balanced'
    - *Outcome*: false negatives were slightly decreased, but still quite high in all models; however, the Random Forest classifier had the best scores overall, making it appropriate to analyze feature importance for.
- **Results**: the top three features based on mean decreases in gini were overtime, age, and monthly income; after running the correlations of these features to attrition, we found that an employee who is younger in age, earns a lower monthly income, and works overtime is likely to leave their company.
   

## EMOZO Facial Coding Validation Project 🎭👩🏻‍💻
- Overview
- Description goes here


