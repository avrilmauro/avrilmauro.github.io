# Personal Portfolio π

## Employee Attrition Machine Learning Project ππΌ
https://github.com/avrilmauro/avrilmauro.github.io/blob/main/employee_attrition_project.ipynb

β **Question**: what drives an employee to leave a company?

ποΈ **Dataset**: [IBM HR Analytics Employee Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

ποΈ **Pre-Processing**: removed constant and arbitrary columns, encoded categorical variables, and ran scale-normalization.

π οΈ **Method**: use a `Random Forest Classifer` to predict if an employee will stay (attrition='No') or leave (attrition='Yes') and compute its cross-validated accuracy score.
- β οΈ *Problems*: the model was outputting many false negatives in the `confusion matrix`.
- π­ *Hypothesis*: our dataset has significantly more entries from employees who stayed rather than left, so the the fitting of the classifier is unbalanced.
- π *Troubleshoot*: (1) compare the model's performance (accuracy, precision, and sensitivity scores) to a `K-Nearest Neighbors Classifier` and `Decision Tree Classifier`, and (2) change the `Random Forest Classifier`'s class_weights to 'balanced'.
- π‘ *Outcome*: false negatives were slightly decreased, but still quite high in all models; however, the Random Forest classifier had the best scores overall, making it appropriate to analyze `feature importance` for.

β **Results**: the top three features based on mean decreases in gini were overtime, age, and monthly income; after running the correlations of these features to attrition, we found that **an employee who is younger in age, earns a lower monthly income, and works overtime is likely to leave their company.**

## EMOZO Facial Coding Validation Project π­π©π»βπ»
π€ **Client**: [EMOZO LABS](https://www.emozo.ai/)

β **Question**: how accurate is Emozoβs facial coding technology in measuring a personβs unconscious emotional response?

### ποΈ Project Timeline
| Week(s)(2022) | Goal                                                                             | Deliverable                          |
|---------------|----------------------------------------------------------------------------------|--------------------------------------|
| 10/03 - 10/10 | Client Introduction and Proposal Draft                                           | N/A                                  |
| 10/10 - 10/24 | Literature Review (Research on Facial Coding Criticisms and Uses)                | [Literature Review](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_literature_review_facialcoding.pdf)                    |
| 10/24 - 11/14 | EMOZO Interface Onboarding, Experiment Design, Survey Design                     | [Project Proposal](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_project_proposal.docx.pdf)                     |
| 11/14 - 11/21 | Experiment Period (Data Collection)                                              | [Demographic Data](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_demographic_visualizations.ipynb)                     |
| 11/21 - 11/28 | Data Analysis + Visualizations                                                   | [Primary Analysis](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_primary_data_analysis.ipynb) & [Variance Analysis](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_variance_analysis.ipynb) |
| 11/28 - 12/05 | Client Presentation (Results and Recommendations)                                | [Slidedeck](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/Emozo%20Client%20Presentation.pdf)                            |

