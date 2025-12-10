# Error Key Reference

**IMPORTANT: Use ONLY these keys. Do not create custom keys.**

## Task 1: Label Encoding

| Key | Points | Description |
|-----|--------|-------------|
| `1_task_1_ok` | 0 | Task solved correctly |
| `1_Wrong_or_Missing_Label_encoding` | 1 | Labels are not or wrongly encoded |

## Task 2: EDA and PCA

| Key | Points | Description |
|-----|--------|-------------|
| `2_task_2_ok` | 0 | Task solved correctly |
| `2_ClassImbalance_not_found` | 1 | Class imbalance not identified via plot or table |
| `2_PCA_missing_or_wrong` | 1 | PCA not performed or wrong |
| `2_PCA_Plot_missing_or_wrong` | 1 | PCA Plot not done or wrong |
| `2_PCA_Plot_text_analysis_missing_or_wrong` | 1 | Plot text based analysis not done or conclusions are wrong |

## Task 3: Model Training and Evaluation

| Key | Points | Description |
|-----|--------|-------------|
| `3_task_3_ok` | 0 | Task solved correctly |
| `3_Model_Training_incorrect_or_missing` | 1 | Classifier model training incorrect or missing |
| `3_Only_one_Classifier_used_or_wrong_classifier` | 1 | Students must train TWO classifiers (kNN AND Logistic Regression). Either only one was trained or wrong classifier used |
| `3_F1_score_missing_or_wrong` | 1 | F1 score not computed or wrong |
| `3_Confusion_Matrix_missing_or_wrong` | 1 | Confusion matrix is missing or wrong |
| `3_Model_performance_analysis_wrong_or_missing` | 2 | Analysis of model performance and model errors is missing, incomplete or wrong |

## Task 4: Optional Advanced Task

| Key | Points | Description |
|-----|--------|-------------|
| `4_task_4_ok` | 0 | Task solved correctly |
| `4_Optional_Part_not_done` | 10 | Optional part was not done |

## Usage Notes

- Each task must be assigned exactly ONE key
- Keys determine point deductions (0 = correct, >0 = incorrect)
- Use the `comment` field in YAML for additional clarification
- For Task 4, comment MUST include F1 score if task was attempted
