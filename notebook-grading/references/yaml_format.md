# YAML Output Format

## Template Structure

```yaml
Task 1:
    - key: [error_key_here]
      comment: [optional explanation]
Task 2:
    - key: [error_key_here]
      comment: [optional explanation]
Task 3:
    - key: [error_key_here]
      comment: [optional explanation]
Task 4:
    - key: [error_key_here]
      comment: [optional explanation]
```

## YAML Rules

1. **Each task MUST have exactly one key**
2. **Use `comment:` field for clarifications** (optional but REQUIRED for Task 4 if attempted)
3. **For Task 4, comment MUST include F1 score** from test dataset
4. **Comments should be concise and specific**
5. **No extra fields or keys allowed**

## Example: All Tasks Correct

```yaml
Task 1:
    - key: 1_task_1_ok
Task 2:
    - key: 2_task_2_ok
Task 3:
    - key: 3_task_3_ok
Task 4:
    - key: 4_task_4_ok
      comment: "Tested on df_test with student's preprocessing pipeline. F1 Score: 0.87"
```

## Example: With Errors and Comments

```yaml
Task 1:
    - key: 1_task_1_ok
Task 2:
    - key: 2_PCA_Plot_missing_or_wrong
      comment: PCA plot exists but axis labels are missing
Task 3:
    - key: 3_Only_one_Classifier_used_or_wrong_classifier
      comment: Only trained kNN, Logistic Regression is missing
Task 4:
    - key: 4_Optional_Part_not_done
```

## Example: With Error Propagation

This example demonstrates how to handle upstream errors that affect downstream tasks:

```yaml
Task 1:
    - key: 1_Wrong_or_Missing_Label_encoding
      comment: Labels encoded as 0,1 instead of required format
Task 2:
    - key: 2_task_2_ok
      comment: Class imbalance analysis logic is correct. Output values affected by Task 1 encoding error, but methodology is sound.
Task 3:
    - key: 3_task_3_ok
      comment: Both classifiers trained correctly. Model performance affected by upstream encoding error, but implementation is correct.
Task 4:
    - key: 4_task_4_ok
      comment: "Full pipeline tested on df_test.pkl. F1 Score: 0.65. Lower score due to Task 1 encoding error, but implementation logic is correct."
```

## Example: Task 4 Not Attempted

```yaml
Task 1:
    - key: 1_task_1_ok
Task 2:
    - key: 2_task_2_ok
Task 3:
    - key: 3_task_3_ok
Task 4:
    - key: 4_Optional_Part_not_done
```

## Example: Multiple Errors in One Task

When a task has multiple issues, use the MOST SEVERE or MOST RELEVANT error key:

```yaml
Task 3:
    - key: 3_Model_Training_incorrect_or_missing
      comment: Both classifiers missing - no kNN or Logistic Regression found
```

or prioritize based on the specific issue:

```yaml
Task 3:
    - key: 3_Only_one_Classifier_used_or_wrong_classifier
      comment: Only kNN implemented. Additionally, F1 score and confusion matrix are missing.
```

## Comment Writing Guidelines

### Good Comments
- Concise and specific
- Explain what's wrong or what was done
- Include relevant details (F1 scores, implementation notes)
- Help student understand the grading decision

### Examples of Good Comments

```yaml
Task 2:
    - key: 2_PCA_Plot_missing_or_wrong
      comment: PCA performed correctly but scatter plot is missing
```

```yaml
Task 3:
    - key: 3_Model_performance_analysis_wrong_or_missing
      comment: F1 scores and confusion matrices present, but no text analysis comparing the two models
```

```yaml
Task 4:
    - key: 4_task_4_ok
      comment: "Successfully evaluated on test set. Preprocessing pipeline replicated correctly. Weighted F1: 0.8234, Confidence-weighted F1: 0.8456"
```

### Avoid Poor Comments
- Too vague: "Something is wrong"
- Too long: Multi-paragraph explanations
- Redundant: Repeating the error key description
- Empty: No comment when clarification would help

## File Naming Convention

YAML files should be named according to the team:

**Pattern:** `FDS-25-Txxx.yaml`

**Examples:**
- `FDS-25-T004.yaml`
- `FDS-25-T109.yaml`
- `FDS-25-T130.yaml`

## File Location

All YAML grading files should be saved to:

`/Users/dp/Desktop/TA agent/data/teacher/practical1/grading_files/`
