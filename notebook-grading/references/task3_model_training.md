# Task 3: Model Training and Evaluation

## Task Description

Students must train classification models and evaluate their performance using appropriate metrics.

## Critical Requirement

**Students MUST implement BOTH classifiers:**
1. k-Nearest Neighbors (kNN)
2. Logistic Regression

If only one is present or wrong algorithm used → use key `3_Only_one_Classifier_used_or_wrong_classifier`

## Requirements

### Model Training
- Train k-Nearest Neighbors (kNN) classifier
- Train Logistic Regression classifier
- Use appropriate parameters and data splits

### Model Evaluation
- Calculate F1 score for both models
- Generate confusion matrix for both models
- Analyze model performance and errors
- Compare the two models

## Error Keys

| Key | Points | Description |
|-----|--------|-------------|
| `3_task_3_ok` | 0 | Task solved correctly |
| `3_Model_Training_incorrect_or_missing` | 1 | Classifier model training incorrect or missing |
| `3_Only_one_Classifier_used_or_wrong_classifier` | 1 | Students must train TWO classifiers (kNN AND Logistic Regression). Either only one was trained or wrong classifier used |
| `3_F1_score_missing_or_wrong` | 1 | F1 score not computed or wrong |
| `3_Confusion_Matrix_missing_or_wrong` | 1 | Confusion matrix is missing or wrong |
| `3_Model_performance_analysis_wrong_or_missing` | 2 | Analysis of model performance and model errors is missing, incomplete or wrong |

## What to Check

### Model Training
- [ ] kNN classifier is implemented and trained
- [ ] Logistic Regression classifier is implemented and trained
- [ ] Both models use appropriate data (features and labels)
- [ ] Training process executes without errors

### Evaluation Metrics
- [ ] F1 score calculated for both models
- [ ] F1 calculation is correct (using sklearn or manual implementation)
- [ ] Confusion matrix generated for both models
- [ ] Confusion matrix format is correct

### Performance Analysis
- [ ] Text analysis discussing model performance
- [ ] Comparison between kNN and Logistic Regression
- [ ] Discussion of model errors (misclassifications)
- [ ] Interpretation of confusion matrix
- [ ] Conclusions drawn from evaluation

## Common Issues

1. **Only one classifier**: Missing either kNN or Logistic Regression
2. **Wrong classifier**: Used neither kNN nor Logistic Regression
3. **Missing F1 score**: Didn't compute F1 metric
4. **Wrong F1 calculation**: Incorrect formula or usage
5. **Missing confusion matrix**: No confusion matrix generated
6. **Incomplete analysis**: Superficial or missing performance discussion
7. **No comparison**: Didn't compare the two models

## Evaluation Notes

- Students may use sklearn implementations or manual implementations
- Different parameter choices (k value, regularization) are acceptable
- Focus on whether both required classifiers are present and working
- Analysis depth should show understanding of model performance

## Error Propagation Consideration

- If upstream tasks (Task 1, Task 2) have errors, model performance may be affected
- Grade based on whether model training and evaluation logic is correct
- If models are properly trained but performance is poor due to upstream errors, mark Task 3 as correct
- Only penalize if the model training or evaluation implementation itself has errors
