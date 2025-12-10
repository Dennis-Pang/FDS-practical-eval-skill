# Task 4: Optional Advanced Task - Test Set Evaluation

## Overview

**This task is optional but requires special evaluation if attempted.**

Task 4 involves evaluating the trained models on a held-out test dataset that students did NOT use during training.

## Critical Context

- Students trained their models on the **training dataset** (NOT test dataset)
- Students did NOT load or use the test dataset in their notebooks
- **YOU must load the test dataset and apply their entire pipeline to evaluate performance**

## If Task 4 is NOT Attempted

- Assign key: `4_Optional_Part_not_done`
- No further evaluation needed

## If Task 4 IS Attempted - REQUIRED TESTING PROCEDURE

### Step 1: Load Test Dataset

```python
import pandas as pd
df_test = pd.read_pickle('/Users/dp/Desktop/TA agent/data/teacher/practical1/df_test.pkl')
```

**File path:** `/Users/dp/Desktop/TA agent/data/teacher/practical1/df_test.pkl`

### Step 2: Replicate Student's ENTIRE Pipeline on Test Data

You must apply ALL steps from their notebook, but using `df_test` instead of training data:

#### A. Preprocessing
- Label encoding (match their encoding scheme)
- Feature engineering (same features they created)
- Data cleaning (same steps they used)
- Feature scaling/normalization (if they used it)

#### B. Feature Transformation
- PCA or dimensionality reduction (if they used it)
- Use the SAME parameters/fitted transformers from training
- **Important:** Use `.transform()` NOT `.fit_transform()` on test data

#### C. Model Application
- Use their trained model (already fitted on training data)
- Generate predictions on the processed test data

#### D. Evaluation
- Calculate F1 score on test predictions
- Use their F1 implementation or standard sklearn F1

### Step 3: Record Results in YAML Comment

- Document the F1 score achieved on test set
- Include any relevant implementation details
- Note their approach/methodology

## Example YAML Output

```yaml
Task 4:
    - key: 4_task_4_ok
      comment: "Replicated full pipeline on df_test.pkl. F1 Score on test set: 0.87. Used custom confidence_weighted_f1 with trained Logistic Regression model."
```

## Step-by-Step Testing Example

```python
# 1. Load test data
df_test = pd.read_pickle('/Users/dp/Desktop/TA agent/data/teacher/practical1/df_test.pkl')

# 2. Apply student's preprocessing (example)
# - If they did: df_train['encoded_label'] = label_encoder.fit_transform(df_train['label'])
# - Then do: df_test['encoded_label'] = label_encoder.transform(df_test['label'])

# 3. Apply student's feature engineering (example)
# - If they created: df_train['feature_X'] = some_transformation(df_train['col'])
# - Then do: df_test['feature_X'] = some_transformation(df_test['col'])

# 4. Apply student's transformations (example)
# - If they did: X_train_pca = pca.fit_transform(X_train)
# - Then do: X_test_pca = pca.transform(X_test)  # Use already fitted PCA

# 5. Get predictions from student's trained model
# predictions = student_model.predict(X_test_processed)

# 6. Calculate F1 score
# from sklearn.metrics import f1_score
# f1 = f1_score(y_test, predictions, average='weighted')
```

## Important Testing Notes

- Students did NOT use test data during training - you are introducing it for evaluation
- **DO NOT modify** student's model or preprocessing logic
- **USE their fitted transformers/encoders** (already trained on training data)
- **APPLY these fitted transformers** to test data (do NOT refit)
- **RECORD actual F1 score** achieved on test set
- If testing takes >10 minutes, stop and ask user
- If implementation fails on test data, document the error

## Required Documentation

After testing Task 4, you MUST create a testing record document:

**File location:** `/Users/dp/Desktop/TA agent/data/students/FDS-25-Txxx/GRADING_TASK4_TEST_RECORD.md`

See `assets/task4_testing_template.md` for the required template.

### Why Documentation is Required

- Provides audit trail that code was actually executed
- User can verify you didn't just make up numbers
- Allows reproducibility of testing
- Documents any issues encountered during testing

## Error Keys

| Key | Points | Description |
|-----|--------|-------------|
| `4_task_4_ok` | 0 | Task solved correctly |
| `4_Optional_Part_not_done` | 10 | Optional part was not done |

## Evaluation Checklist

- [ ] Confirmed Task 4 is attempted (look for test evaluation in notebook)
- [ ] Loaded test dataset from correct path
- [ ] Replicated ALL preprocessing steps on test data
- [ ] Applied fitted transformers (not refitting)
- [ ] Generated predictions using student's trained model
- [ ] Calculated F1 score on test predictions
- [ ] Recorded F1 score in YAML comment
- [ ] Created testing record document
- [ ] Appended F1 score to f1.txt file
