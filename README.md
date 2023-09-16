# Personal Portfolio 📚
## S&P 500 Dashboard 📈💵
[link]

❓ **Question**: how can we make a tool to help beginners learn about the stock market?

🗃️ **Datasets**: 
- [S&P 500 Historical Data](https://www.kaggle.com/datasets/henryhan117/sp-500-historical-data)
- [S&P 500 Stock Price with Financial Statement](https://www.kaggle.com/datasets/hanseopark/sp-500-stocks-value-with-financial-statement)
- [Top Tech Companies Stock Price Dataset](https://www.kaggle.com/datasets/tomasmantero/top-tech-companies-stock-price?select=List+of+SP+500+companies.csv)

🛠️ **Method**: create a convenient and interactive dashboard that gives the user freedom to explore stock performance through different time frames and industries of their choice 
- utilized libraries such as Plotly, Dash, and Dash Bootstrap Components
- displayed bullet charts, candlestick graphs, accordian tables, and bullet charts with time and industry controls
- predicted industries such as Healthcare and Technology to flourish over time, while Real Estate may fluctuate with market recessions
- resulted in a multitude of industry-specific conclusions and visibility into the impact of COVID-19

<img src="https://i.ibb.co/S6RckBb/S-P-500-Dashboard-Snapshot-1.png">
<img src="https://i.ibb.co/FBLrLG0/S-P-500-Dashboard-Snapshot-2.png">

## Employee Attrition Machine Learning Project 🏃💼
https://github.com/avrilmauro/avrilmauro.github.io/blob/main/employee_attrition_project.ipynb

❓ **Question**: what drives an employee to leave a company?

🗃️ **Dataset**: [IBM HR Analytics Employee Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

🗂️ **Pre-Processing**: removed constant and arbitrary columns, encoded categorical variables, and ran scale-normalization.

🛠️ **Method**: use a `Random Forest Classifer` to predict if an employee will stay (attrition='No') or leave (attrition='Yes') and compute its cross-validated accuracy score
- *Model Issue*: the model was outputting many false negatives in the `confusion matrix`, this was hypothesized to be due to the dataset having significantly more attrition-yes entries than attrition-no entries, so the classifier fitting was unbalanced
- *Troubleshoot*: (1) compare the model's performance (accuracy, precision, and sensitivity scores) to a `K-Nearest Neighbors Classifier` and `Decision Tree Classifier`, and (2) change the `Random Forest Classifier`'s class_weights to 'balanced'
- *Outcome*: false negatives were slightly decreased, but still quite high in all models; however, the Random Forest classifier had the best scores overall, making it appropriate to analyze `feature importance` for

✅ **Results**: the top three features based on mean decreases in gini were overtime, age, and monthly income; after running the correlations of these features to attrition, we found that **an employee who is younger in age, earns a lower monthly income, and works overtime is likely to leave their company.**

## EMOZO Facial Coding Validation Project 🎭👩🏻‍💻
👤 **Client**: [EMOZO LABS](https://www.emozo.ai/)

❓ **Question**: how accurate is Emozo’s facial coding technology in measuring a person’s unconscious emotional response?

### 🗓️ Project Timeline
| Week(s)(2022) | Goal                                                                             | Deliverable                          |
|---------------|----------------------------------------------------------------------------------|--------------------------------------|
| 10/03 - 10/10 | Client Introduction and Proposal Draft                                           | N/A                                  |
| 10/10 - 10/24 | Literature Review (Research on Facial Coding Criticisms and Uses)                | [Literature Review](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_literature_review_facialcoding.pdf)                    |
| 10/24 - 11/14 | EMOZO Interface Onboarding, Experiment Design, Survey Design                     | [Project Proposal](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_project_proposal.docx.pdf)                     |
| 11/14 - 11/21 | Experiment Period (Data Collection)                                              | [Demographic Data](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_demographic_visualizations.ipynb)                     |
| 11/21 - 11/28 | Data Analysis + Visualizations                                                   | [Primary Analysis](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_primary_data_analysis.ipynb) & [Variance Analysis](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/emozo_variance_analysis.ipynb) |
| 11/28 - 12/05 | Client Presentation (Results and Recommendations)                                | [Slidedeck](https://github.com/avrilmauro/avrilmauro.github.io/blob/main/Emozo%20Client%20Presentation.pdf)                            |

