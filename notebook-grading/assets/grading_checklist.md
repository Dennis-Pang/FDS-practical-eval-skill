# Grading Checklist (Per Team)

Use this checklist to ensure all grading steps are completed for each team.

## Pre-Grading Setup

- [ ] Confirm team number: `FDS-25-Txxx`
- [ ] Locate team folder: `/Users/dp/Desktop/TA agent/data/students/FDS-25-Txxx`
- [ ] Identify all `.ipynb` files in folder (may be 1-2 notebooks)

## Code Preparation

- [ ] Fix dataset paths in ALL notebooks
  - Search for dataset loading statements
  - Replace with absolute paths: `/Users/dp/Desktop/TA agent/data/teacher/practical1/[filename]`
  - Match filenames exactly (case-sensitive)
  - Do NOT modify any other code
- [ ] Execute notebooks to verify code works after path fixes

## Task Evaluation

### Task 1: Label Encoding
- [ ] Read task description in notebook
- [ ] Read student's implementation
- [ ] Execute code to verify output
- [ ] Evaluate implementation logic
- [ ] Assign error key from `error_keys.md`
- [ ] Add comment if needed

### Task 2: EDA and PCA
- [ ] Check for class imbalance analysis (plot or table)
- [ ] Check for PCA implementation
- [ ] Check for PCA visualization (scatter plot)
- [ ] Check for text analysis of PCA results
- [ ] Evaluate implementation logic
- [ ] Consider error propagation from Task 1
- [ ] Assign error key from `error_keys.md`
- [ ] Add comment if needed

### Task 3: Model Training
- [ ] Verify kNN classifier is implemented and trained
- [ ] Verify Logistic Regression classifier is implemented and trained
- [ ] Check for F1 score calculation
- [ ] Check for confusion matrix generation
- [ ] Check for model performance analysis
- [ ] Evaluate implementation logic
- [ ] Consider error propagation from Tasks 1-2
- [ ] Assign error key from `error_keys.md`
- [ ] Add comment if needed

### Task 4: Optional Advanced Task
- [ ] Determine if Task 4 was attempted
- **If NOT attempted:**
  - [ ] Assign key: `4_Optional_Part_not_done`
- **If attempted:**
  - [ ] Load test dataset: `df_test.pkl`
  - [ ] Replicate ALL preprocessing steps on test data
  - [ ] Apply fitted transformers (do NOT refit)
  - [ ] Generate predictions using student's trained model
  - [ ] Calculate F1 score on test set
  - [ ] Create testing record document: `GRADING_TASK4_TEST_RECORD.md`
  - [ ] Assign error key from `error_keys.md`
  - [ ] Add comment with F1 score (REQUIRED)

## Output Generation

- [ ] Create or update YAML file: `/Users/dp/Desktop/TA agent/data/teacher/practical1/grading_files/FDS-25-Txxx.yaml`
- [ ] Verify YAML format is correct (see `yaml_format.md`)
- [ ] Ensure each task has exactly one key
- [ ] Ensure Task 4 comment includes F1 score (if attempted)
- [ ] Verify no extra fields or keys

## F1 Score Recording

- [ ] Open file: `/Users/dp/Desktop/TA agent/data/teacher/practical1/f1.txt`
- [ ] Append team's F1 score:
  - Format: `FDS25-Txxx: 0.XXXX` (if Task 4 attempted)
  - Format: `FDS25-Txxx: N/A (Task 4 not attempted)` (if not attempted)
- [ ] Save file

## Final Verification

- [ ] All 4 tasks have been evaluated
- [ ] YAML file is properly formatted
- [ ] F1 score is recorded in f1.txt
- [ ] Testing record created (if Task 4 attempted)
- [ ] No execution errors remain unresolved

## Error Handling

If any of the following occur, STOP and ask user:
- [ ] Execution exceeds 10 minutes
- [ ] Errors not covered by error key table
- [ ] Completely different approach that's hard to evaluate
- [ ] Ambiguous implementation that could be correct or incorrect

## Notes

Record any important observations or issues encountered during grading:

```
[Your notes here]
```
