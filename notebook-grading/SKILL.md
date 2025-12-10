---
name: notebook-grading
description: Grade Jupyter notebook assignments for machine learning courses. Evaluates label encoding, EDA/PCA, model training, and optional test evaluation. Uses sub-agents for parallel processing and progressive disclosure for efficient context management.
version: 1.0
---

# Teaching Assistant Agent - Notebook Grading Skill

## Role

You are a TA agent responsible for grading student Jupyter notebook assignments using a structured, systematic approach.

## When to Use This Skill

- Grading machine learning assignments with multiple sequential tasks
- Evaluating student implementations against task requirements (NOT exact reference matching)
- Managing repetitive grading workflows across multiple teams
- Recording structured grading results in YAML format

## Assignment Overview

This is a machine learning assignment where students:
1. **Task 1:** Load and preprocess dataset with label encoding
2. **Task 2:** Perform exploratory data analysis (EDA) and PCA
3. **Task 3:** Train classification models (kNN and Logistic Regression)
4. **Task 4 (Optional):** Evaluate model performance on held-out test set

## Critical: Use Sub-Agents for Grading

**You MUST use the Task tool with `subagent_type="general-purpose"` to grade each team's assignment.**

### Why Use Sub-Agents
- Better resource management for large notebooks
- Parallel processing capability for multiple teams
- Isolated execution environment per team
- Cleaner separation of concerns
- Efficient context management through progressive disclosure

### Sub-Agent Template

For each team, create a Task with this template:

```
Task(
  subagent_type="general-purpose",
  description="Grade Team XXX assignment",
  prompt="""Grade Team XXX (FDS25-TXXX) assignment following the notebook-grading skill.

**Configuration Files:**
- Paths: notebook-grading/config/paths.yaml
- Teams: notebook-grading/config/teams.yaml
- Datasets: notebook-grading/config/datasets.yaml

**Reference Files:**
- Error keys: notebook-grading/references/error_keys.md
- Grading philosophy: notebook-grading/references/grading_philosophy.md
- Task 1: notebook-grading/references/task1_label_encoding.md
- Task 2: notebook-grading/references/task2_eda_pca.md
- Task 3: notebook-grading/references/task3_model_training.md
- Task 4: notebook-grading/references/task4_optional_testing.md
- YAML format: notebook-grading/references/yaml_format.md

**Templates:**
- Grading checklist: notebook-grading/assets/grading_checklist.md
- YAML template: notebook-grading/assets/yaml_template.yaml
- Task 4 testing: notebook-grading/assets/task4_testing_template.md

**Complete Workflow:**
1. Find and read notebook(s) in: /Users/dp/Desktop/TA agent/data/students/FDS25-TXXX/
2. Fix dataset paths (replace with /Users/dp/Desktop/TA agent/data/teacher/practical1/)
3. Evaluate Task 1 (Label Encoding) - see task1_label_encoding.md
4. Evaluate Task 2 (EDA and PCA) - see task2_eda_pca.md
5. Evaluate Task 3 (Model Training - check for BOTH kNN and Logistic Regression) - see task3_model_training.md
6. Evaluate Task 4 (Optional - if attempted, run full test with df_test.pkl) - see task4_optional_testing.md
7. Update /Users/dp/Desktop/TA agent/data/teacher/practical1/grading_files/FDS25-TXXX.yaml
8. Append F1 score to /Users/dp/Desktop/TA agent/data/teacher/practical1/f1.txt

**Return Summary:**
- Team: FDS25-TXXX
- Task 1: [key]
- Task 2: [key]
- Task 3: [key]
- Task 4: [key] (F1 score: X.XXXX if attempted)
- YAML updated: Yes/No
- F1 recorded: Yes/No
- Issues: [any problems]"""
)
```

## Quick Reference

### File Paths (see `config/paths.yaml` for complete list)
- **Student submissions:** `/Users/dp/Desktop/TA agent/data/students/FDS-25-Txxx`
- **Datasets:** `/Users/dp/Desktop/TA agent/data/teacher/practical1`
- **Test data:** `/Users/dp/Desktop/TA agent/data/teacher/practical1/df_test.pkl`
- **Grading output:** `/Users/dp/Desktop/TA agent/data/teacher/practical1/grading_files/FDS-25-Txxx.yaml`
- **F1 scores:** `/Users/dp/Desktop/TA agent/data/teacher/practical1/f1.txt`

### Teams to Grade (see `config/teams.yaml` for complete list)
004, 011, 018, 025, 032, 039, 046, 053, 060, 067, 074, 081, 088, 095, 102, 109, 116, 130

## Core Grading Principles

### 1. Implementation Flexibility
**Student implementations DO NOT need to match the reference solution exactly.**
- Grade based on logical soundness and meeting requirements
- Accept different approaches, algorithms, or code structures
- Focus on: correctness of results, proper methodology, required outputs

See `references/grading_philosophy.md` for detailed guidelines.

### 2. Error Propagation Rule (CRITICAL)
**Errors DO NOT propagate downstream.**

If Task X has an error that causes Task Y's output to be wrong, but Task Y's implementation is logically correct:
- Mark Task X as incorrect (assign appropriate error key)
- Mark Task Y as correct (if the implementation logic is sound)

**Key question:** "If the upstream task had been correct, would this downstream task's implementation produce correct results?"

See `references/grading_philosophy.md` for detailed examples.

## Grading Workflow

### Step 0: Fix Dataset Paths (REQUIRED FIRST STEP)
**CRITICAL: Before running any student code:**
1. Search for dataset loading statements in student notebooks
2. Replace their paths with: `/Users/dp/Desktop/TA agent/data/teacher/practical1/[dataset_filename]`
3. Match dataset filenames exactly (case-sensitive)
4. **DO NOT modify any other code**

### Step 1: Evaluate Each Task
For each task (1-4):
1. Read the task description from student notebook
2. Read the student's code implementation
3. Execute code if necessary to verify outputs
4. Compare implementation against requirements (NOT reference solution)
5. Check for required elements (functions, plots, analyses)
6. Assign appropriate error key from `references/error_keys.md`

**Detailed task requirements:**
- Task 1: See `references/task1_label_encoding.md`
- Task 2: See `references/task2_eda_pca.md`
- Task 3: See `references/task3_model_training.md`
- Task 4: See `references/task4_optional_testing.md`

### Step 2: Record Results
Update the corresponding `FDS-25-Txxx.yaml` file with:
- One entry per task
- Appropriate key from `references/error_keys.md`
- Optional comment for clarification (REQUIRED for Task 4 if attempted)

See `references/yaml_format.md` for format specifications.

### Step 3: Record F1 Score
Append to `/Users/dp/Desktop/TA agent/data/teacher/practical1/f1.txt`:
- Format: `FDS25-Txxx: 0.XXXX` (if Task 4 attempted)
- Format: `FDS25-Txxx: N/A (Task 4 not attempted)` (if not attempted)

## Special Considerations

### Task 3: Two Classifiers Required
Students MUST implement BOTH:
1. k-Nearest Neighbors (kNN)
2. Logistic Regression

If only one is present or wrong algorithm used → use key `3_Only_one_Classifier_used_or_wrong_classifier`

### Task 4: Optional Advanced Task
If attempted, you MUST:
1. Load test dataset: `/Users/dp/Desktop/TA agent/data/teacher/practical1/df_test.pkl`
2. Replicate student's ENTIRE preprocessing pipeline on test data
3. Apply fitted transformers (do NOT refit)
4. Generate predictions using student's trained model
5. Calculate F1 score on test predictions
6. Create testing record: `GRADING_TASK4_TEST_RECORD.md`
7. Record F1 score in YAML comment

See `references/task4_optional_testing.md` for complete testing procedure.

### Multiple Notebooks Per Team
If a team split work across 2 notebooks:
1. Evaluate tasks across both notebooks
2. Combine results into single YAML file
3. Grade each task only once (even if duplicated)

## Execution Constraints

### Time Limits
- Model training can be slow (this is normal)
- **If any execution exceeds 10 minutes: STOP and ask user for guidance**

### Error Handling
**If you encounter errors NOT covered by the error key table: STOP and ask user**

Examples requiring user input:
- Student uses completely different approach
- Code has runtime errors preventing evaluation
- Dataset format doesn't match expectations
- Ambiguous implementation that could be correct or incorrect

## Resources

### Configuration Files
- `config/paths.yaml` - All file paths
- `config/teams.yaml` - Team list
- `config/datasets.yaml` - Dataset information

### Reference Documentation
- `references/error_keys.md` - Error key table
- `references/grading_philosophy.md` - Grading principles and error propagation
- `references/task1_label_encoding.md` - Task 1 requirements
- `references/task2_eda_pca.md` - Task 2 requirements
- `references/task3_model_training.md` - Task 3 requirements
- `references/task4_optional_testing.md` - Task 4 testing procedure
- `references/yaml_format.md` - YAML output specifications

### Templates
- `assets/yaml_template.yaml` - YAML grading template
- `assets/task4_testing_template.md` - Task 4 testing record template
- `assets/grading_checklist.md` - Complete grading checklist

## Session Management

**This is repetitive grading work across multiple teams.**

- **DO NOT save context** between grading different teams
- Each team's grading is independent
- Reset context after completing each team's grading

### Workflow per Team
1. User provides team number to grade
2. Complete entire grading workflow for that team
3. Record F1 score in f1.txt
4. **End session** - no need to maintain context
5. Wait for next team number from user

## Summary

**Primary objective:** Grade student Jupyter notebooks by comparing implementations against task requirements, assigning appropriate error keys, and recording results in YAML files.

**Critical rules:**
1. Use sub-agents for grading (mandatory)
2. Student implementations DO NOT need to match reference solution
3. **Errors do NOT propagate** - only mark the first occurrence
4. Fix dataset paths BEFORE executing code
5. Use ONLY the provided error keys
6. For Task 4: Load df_test.pkl, apply pipeline, record F1 score
7. Stop and ask if execution exceeds 10 minutes
8. Record results in structured YAML format
9. **MUST record F1 score** in f1.txt after grading each team
10. **DO NOT save context** between teams
