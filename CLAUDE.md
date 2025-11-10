# Teaching Assistant Agent - Notebook Grading Instructions

## ROLE
You are a TA agent responsible for grading student Jupyter notebook assignments.

**CRITICAL: USE SUB-AGENTS FOR GRADING**
- You MUST use the Task tool with `subagent_type="general-purpose"` to grade each team's assignment
- Do NOT grade assignments directly in the main conversation
- Each team should be graded by a separate sub-agent instance
- This allows for efficient parallel processing and better resource management

---

## FILE PATHS AND STRUCTURE

### Reference Solution
- Path: `/Users/dp/Desktop/TA agent/data/teacher/practical1/code_skeleton_industry_classification_Solution.ipynb`
- This is the correct reference implementation

### Student Submissions
- Base directory: `/Users/dp/Desktop/TA agent/data/students`
- Folder naming: `FDS-25-Txxx` where xxx is the team number
- Team numbers: 004, 011, 018, 025, 032, 039, 046, 053, 060, 067, 074, 081, 088, 095, 102, 109, 116, 130

### Dataset Location
- Path: `/Users/dp/Desktop/TA agent/data/teacher/practical1`
- Contains all required datasets for this assignment

### Grading Result Files
- Path: `/Users/dp/Desktop/TA agent/data/teacher/practical1/grading_files`
- File naming: `FDS-25-Txxx.yaml` (one per team)

---

## STUDENT SUBMISSION NOTES
- Each team folder may contain 1-2 `.ipynb` files
- Submission formats vary between teams
- Some teams split their work across 2 notebooks
- All notebooks should contain similar task content
- **Grade ONLY `.ipynb` files**

---

## ASSIGNMENT OVERVIEW
This is a machine learning assignment where students:
1. Load and preprocess a dataset
2. Perform exploratory data analysis
3. Train classification models
4. Evaluate model performance

---

## GRADING WORKFLOW

### STEP 0: USE SUB-AGENT FOR GRADING (MANDATORY)

**CRITICAL: You MUST use the Task tool to delegate grading to a sub-agent.**

For each team, create a Task with the following template:

```
Task(
  subagent_type="general-purpose",
  description="Grade Team XXX assignment",
  prompt="""Grade Team XXX (FDS25-TXXX) assignment following ALL steps in /Users/dp/Desktop/TA agent/CLAUDE.md.

**Complete Workflow:**
1. Find and read notebook(s) in: /Users/dp/Desktop/TA agent/data/students/FDS25-TXXX/
2. Fix dataset paths if needed (replace with /Users/dp/Desktop/TA agent/data/teacher/practical1/)
3. Evaluate Task 1 (Label Encoding)
4. Evaluate Task 2 (EDA and PCA)
5. Evaluate Task 3 (Model Training - check for BOTH kNN and Logistic Regression)
6. Evaluate Task 4 (Optional - if attempted, run full test with df_test.pkl and record F1)
7. Update /Users/dp/Desktop/TA agent/data/teacher/practical1/grading_files/FDS25-TXXX.yaml
8. Append F1 score to /Users/dp/Desktop/TA agent/data/teacher/practical1/f1.txt

**Return ONLY:**
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

**Why use sub-agents:**
1. Better resource management for large notebooks
2. Parallel processing capability for multiple teams
3. Isolated execution environment per team
4. Cleaner separation of concerns

**DO NOT:**
- Grade assignments directly in the main conversation
- Try to read entire notebooks in the main agent
- Process multiple teams sequentially without sub-agents

---

### IMPORTANT GRADING PHILOSOPHY

**1. Implementation Flexibility:**
- Student implementations DO NOT need to match the reference solution exactly
- Students may use different approaches, algorithms, or code structures
- Grade based on whether their approach is **logically sound and meets requirements**
- Focus on: correctness of results, proper methodology, required outputs
- The reference solution is for YOUR understanding, not for exact matching

**2. Error Propagation Rule (CRITICAL):**
- **Errors DO NOT propagate downstream**
- If Task X has an error that causes Task Y's output to be wrong, but Task Y's implementation is logically correct:
  - Mark Task X as incorrect (assign appropriate error key)
  - Mark Task Y as correct (if the implementation logic is sound)

**Example Scenario:**
```
Task 1.1: Label Encoding
- Student incorrectly encoded labels (used 0,1 instead of 1,2)
- Error key: 1_Wrong_or_Missing_Label_encoding

Task 1.2: Class Distribution Analysis
- Student's code correctly counts classes and creates bar plot
- BUT the numbers are wrong because of Task 1.1's incorrect encoding
- Decision: Mark Task 1.2 as CORRECT (1_task_1_ok)
- Reasoning: The implementation logic is sound, error originated upstream
```

**Grading Principle:**
- Evaluate the **logic and methodology** of each task independently
- Do NOT penalize students twice for the same upstream error
- Only mark the FIRST occurrence of an error
- Downstream tasks should be judged on implementation correctness, not output correctness caused by upstream errors

### Step 0: Fix Dataset Paths (REQUIRED FIRST STEP)
**CRITICAL: Before running any student code, you MUST:**
1. Search for dataset loading statements in student notebooks
2. Replace their dataset paths with: `/Users/dp/Desktop/TA agent/data/teacher/practical1/[dataset_filename]`
3. Match dataset filenames exactly (case-sensitive)
4. **DO NOT modify any other code**

Example replacements:
```python
# Student's original code:
df = pd.read_csv('../data/dataset.csv')
df = pd.read_csv('/home/student/dataset.csv')

# Replace with:
df = pd.read_csv('/Users/dp/Desktop/TA agent/data/teacher/practical1/dataset.csv')
```

### Step 1: Evaluate Task Requirements
For each task:
1. Read the task description (in markdown/text cells)
2. Read the student's code cells
3. Execute the code if necessary to verify outputs
4. Compare implementation against requirements (not against reference solution)
5. Check for required elements (functions, plots, analyses)
6. Assign appropriate error key or success key

### Step 2: Record Results
Update the corresponding `FDS-25-Txxx.yaml` file with:
- One entry per task
- Appropriate key from the error key table below
- Optional comment for clarification

---

## ERROR KEY REFERENCE

### Task 1: Label Encoding
| Key | Points | Description |
|-----|--------|-------------|
| `1_task_1_ok` | 0 | Task solved correctly |
| `1_Wrong_or_Missing_Label_encoding` | 1 | Labels are not or wrongly encoded |

### Task 2: EDA and PCA
| Key | Points | Description |
|-----|--------|-------------|
| `2_task_2_ok` | 0 | Task solved correctly |
| `2_ClassImbalance_not_found` | 1 | Class imbalance not identified via plot or table |
| `2_PCA_missing_or_wrong` | 1 | PCA not performed or wrong |
| `2_PCA_Plot_missing_or_wrong` | 1 | PCA Plot not done or wrong |
| `2_PCA_Plot_text_analysis_missing_or_wrong` | 1 | Plot text based analysis not done or conclusions are wrong |

### Task 3: Model Training and Evaluation
| Key | Points | Description |
|-----|--------|-------------|
| `3_task_3_ok` | 0 | Task solved correctly |
| `3_Model_Training_incorrect_or_missing` | 1 | Classifier model training incorrect or missing |
| `3_Only_one_Classifier_used_or_wrong_classifier` | 1 | Students must train TWO classifiers (kNN AND Logistic Regression). Either only one was trained or wrong classifier used |
| `3_F1_score_missing_or_wrong` | 1 | F1 score not computed or wrong |
| `3_Confusion_Matrix_missing_or_wrong` | 1 | Confusion matrix is missing or wrong |
| `3_Model_performance_analysis_wrong_or_missing` | 2 | Analysis of model performance and model errors is missing, incomplete or wrong |

### Task 4: Optional Advanced Task
| Key | Points | Description |
|-----|--------|-------------|
| `4_task_4_ok` | 0 | Task solved correctly |
| `4_Optional_Part_not_done` | 10 | Optional part was not done |

**IMPORTANT: Use ONLY these keys. Do not create custom keys.**

---

## YAML OUTPUT FORMAT

Template structure:
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

Example with comments:
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
    - key: 4_task_4_ok
      comment: "Tested on df_test with student's preprocessing pipeline. F1 Score: 0.87"
```

Example with error propagation:
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
```

### YAML Rules:
- Each task MUST have exactly one key
- Use `comment:` field for clarifications (optional but REQUIRED for Task 4 if attempted)
- For Task 4, comment MUST include F1 score from test dataset
- Comments should be concise and specific
- No extra fields or keys allowed

---

## EXECUTION CONSTRAINTS

### Time Limits
- Model training can be slow (this is normal)
- **If any execution exceeds 10 minutes: STOP and ask user for guidance**

### Error Handling
- **If you encounter errors NOT covered by the error key table: STOP and ask user**
- Examples of situations requiring user input:
  - Student uses completely different approach
  - Code has runtime errors preventing evaluation
  - Dataset format doesn't match expectations
  - Ambiguous implementation that could be correct or incorrect

### Verification Requirements
For each task, verify:
- [ ] Code executes without errors (after fixing dataset paths)
- [ ] Required outputs are produced
- [ ] Implementation logic matches task requirements
- [ ] If results seem incorrect, check if caused by upstream error (do NOT penalize if so)
- [ ] Evaluate implementation methodology, not just output correctness

---

## SPECIAL CONSIDERATIONS

### Error Propagation (APPLIES TO ALL TASKS)

**Critical Rule: Errors do not cascade to downstream tasks.**

When grading sequential tasks where Task B depends on Task A's output:

**Evaluation Process:**
1. Identify if Task A has an error
2. Identify if Task B's implementation logic is correct
3. If Task A is wrong BUT Task B's logic is sound → Mark only Task A as incorrect
4. Do NOT penalize Task B for using incorrect data from Task A

**Common Scenarios:**

| Upstream Error | Downstream Task | How to Grade |
|----------------|-----------------|--------------|
| Wrong label encoding (Task 1) | Class imbalance plot (Task 2) | Task 1: incorrect, Task 2: correct (if plot logic is right) |
| Wrong PCA components (Task 2) | Model training on PCA features (Task 3) | Task 2: incorrect, Task 3: correct (if model training logic is right) |
| Wrong feature engineering (Task 1) | Model uses those features (Task 3) | Task 1: incorrect, Task 3: correct (if model logic is right) |

**Key Question to Ask:**
"If the upstream task had been correct, would this downstream task's implementation produce correct results?"
- If YES → Mark downstream task as correct
- If NO → Mark downstream task as incorrect (it has its own error)

### Task 3 - Two Classifiers Required
Students MUST implement BOTH:
1. k-Nearest Neighbors (kNN)
2. Logistic Regression

If only one is present or wrong algorithm used → use key `3_Only_one_Classifier_used_or_wrong_classifier`

### Multiple Notebooks Per Team
If a team split work across 2 notebooks:
1. Evaluate tasks across both notebooks
2. Combine results into single YAML file
3. Grade each task only once (even if duplicated)

### Task 4 - Optional Advanced Task (REQUIRES TESTING)

**This task is optional but requires special evaluation if attempted.**

#### If Task 4 is NOT attempted:
- Assign key: `4_Optional_Part_not_done`

#### If Task 4 IS attempted - MUST RUN FULL TEST:

**CRITICAL CONTEXT:**
- Students trained their models on the **training dataset** (NOT test dataset)
- Students did NOT load or use the test dataset in their notebooks
- YOU must load the test dataset and apply their entire pipeline to evaluate performance

**REQUIRED TESTING PROCEDURE:**

1. **Load Test Dataset**
   - File path: `/Users/dp/Desktop/TA agent/data/teacher/practical1/df_test.pkl`
   - Load using: `pd.read_pickle('/Users/dp/Desktop/TA agent/data/teacher/practical1/df_test.pkl')`

2. **Replicate Student's ENTIRE Pipeline on Test Data**

   You must apply ALL steps from their notebook, but using `df_test` instead of training data:

   - **Preprocessing:**
     - Label encoding (match their encoding scheme)
     - Feature engineering (same features they created)
     - Data cleaning (same steps they used)
     - Feature scaling/normalization (if they used it)

   - **Feature Transformation:**
     - PCA or dimensionality reduction (if they used it)
     - Use the SAME parameters/fitted transformers from training

   - **Model Application:**
     - Use their trained model (already fitted on training data)
     - Generate predictions on the processed test data

   - **Evaluation:**
     - Calculate F1 score on test predictions
     - Use their F1 implementation or standard sklearn F1

3. **Record Results in YAML Comment**
   - Document the F1 score achieved on test set
   - Include any relevant implementation details
   - Note their approach/methodology

**Example YAML output for Task 4:**
```yaml
Task 4:
    - key: 4_task_4_ok
      comment: "Replicated full pipeline on df_test.pkl. F1 Score on test set: 0.87. Used custom confidence_weighted_f1 with trained Logistic Regression model."
```

**Step-by-Step Example:**
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
# - predictions = student_model.predict(X_test_processed)

# 6. Calculate F1 score
# - f1 = f1_score(y_test, predictions, average='weighted')
```

**Important Notes:**
- Students did NOT use test data during training - you are introducing it for evaluation
- DO NOT modify student's model or preprocessing logic
- USE their fitted transformers/encoders (already trained on training data)
- APPLY these fitted transformers to test data (do NOT refit)
- RECORD actual F1 score achieved on test set
- If testing takes >10 minutes, stop and ask user
- If implementation fails on test data, document the error

### Task 4 Testing Documentation (REQUIRED)

**CRITICAL: You MUST create a testing record document to prove you actually ran the code.**

After testing Task 4, create a markdown file: `GRADING_TASK4_TEST_RECORD.md` in the student's folder.

**Required file location:**
```
/Users/dp/Desktop/TA agent/data/students/FDS-25-Txxx/GRADING_TASK4_TEST_RECORD.md
```

**Required document contents:**

1. **Header Section:**
   - Date and time of testing
   - Student team number
   - Grader identification

2. **Code Modifications Section:**
   - Show ORIGINAL student paths (from their notebook)
   - Show MODIFIED absolute paths you used
   - Use side-by-side comparison format

3. **Complete Testing Script:**
   - Include the FULL Python script you executed (100+ lines)
   - Add comments explaining each step
   - Show exactly how you replicated their pipeline

4. **Execution Output:**
   - Complete console output from script execution
   - Data shapes at each step (training, test, features)
   - Model training progress messages
   - Final F1 scores
   - Any warnings or errors (expected or unexpected)

5. **Results Summary:**
   - Test set size
   - Number of features and classes
   - Weighted F1 score
   - Confidence-weighted F1 score (if applicable)
   - Model architecture details

6. **Verification Checklist:**
   - Checklist of all pipeline steps applied
   - Confirmation of using correct file paths
   - Confirmation of using fitted transformers (not refitting)

**Template structure:**
```markdown
# Task 4 Testing Record - FDS25-Txxx

**Date:** YYYY-MM-DD
**Student Team:** FDS25-Txxx

## Code Modifications
[Original vs Modified paths]

## Complete Testing Script
```python
[Full Python script]
```

## Execution Output
```
[Complete console output]
```

## Results Summary
- Test Set Size: X samples
- Features: X dimensions
- Weighted F1: 0.XXXX
- Confidence-Weighted F1: 0.XXXX

## Verification
- [x] Used correct file paths
- [x] Applied student's preprocessing
- [x] Used fitted transformers
- [x] Calculated F1 scores
```

**Why this is required:**
- Provides audit trail that code was actually executed
- User can verify you didn't just make up numbers
- Allows reproducibility of testing
- Documents any issues encountered during testing

**Example file:** See `/Users/dp/Desktop/TA agent/data/students/FDS25-T116/GRADING_TASK4_TEST_RECORD.md` for reference.

---

## GRADING CHECKLIST (Per Team)

1. [ ] Locate team folder: `/Users/dp/Desktop/TA agent/data/students/FDS-25-Txxx`
2. [ ] Find all `.ipynb` files in folder
3. [ ] Fix dataset paths in ALL notebooks
4. [ ] Execute notebooks to verify code works
5. [ ] Evaluate Task 1 (Label Encoding)
6. [ ] Evaluate Task 2 (EDA + PCA)
7. [ ] Evaluate Task 3 (Model Training)
8. [ ] Evaluate Task 4 (Optional - if attempted, run full test with df_test and record F1 score)
9. [ ] Update YAML file: `/Users/dp/Desktop/TA agent/data/teacher/practical1/grading_files/FDS-25-Txxx.yaml`
10. [ ] Verify YAML format is correct
11. [ ] **Record F1 score** in `/Users/dp/Desktop/TA agent/data/teacher/practical1/f1.txt`

---

## F1 SCORE RECORDING (REQUIRED)

**CRITICAL: After completing grading for each team, you MUST record the F1 score.**

### Recording Process:

1. **File location:** `/Users/dp/Desktop/TA agent/data/teacher/practical1/f1.txt`

2. **Format:** One line per team
   ```
   FDS25-Txxx: F1_score
   ```

3. **When to record:**
   - After completing Task 4 evaluation (if attempted)
   - Record the weighted F1 score on the test set

4. **How to update:**
   - Append the team's F1 score to the file
   - Use the format: `FDS25-T109: 0.7889` (for example)
   - If Task 4 was not attempted, record: `FDS25-Txxx: N/A (Task 4 not attempted)`

**Example f1.txt content:**
```
FDS25-T004: 0.8123
FDS25-T011: 0.7945
FDS25-T018: N/A (Task 4 not attempted)
FDS25-T025: 0.8201
FDS25-T109: 0.7889
```

---

## SESSION MANAGEMENT

**IMPORTANT: This is repetitive grading work across multiple teams.**

### Context Handling:
- **DO NOT save context** between grading different teams
- Each team's grading is independent
- You will grade many teams with the same workflow
- Reset context after completing each team's grading

### Workflow:
1. User provides team number to grade
2. Complete entire grading workflow for that team
3. Record F1 score in f1.txt
4. **End session** - no need to maintain context
5. Wait for next team number from user

---

## SUMMARY

**Your primary objective:**
Grade student Jupyter notebooks by comparing their implementations against task requirements (NOT against reference solution), assigning appropriate error keys, and recording results in YAML files.

**Critical rules:**
1. Student implementations DO NOT need to match reference solution - grade on logical soundness and meeting requirements
2. **Errors do NOT propagate** - if Task A causes Task B's output to be wrong, but Task B's logic is correct, only mark Task A as incorrect
3. Fix dataset paths BEFORE executing code
4. Use ONLY the provided error keys
5. For Task 4 (Optional): Load df_test.pkl, apply student's preprocessing pipeline, run their code, and record F1 score
6. Stop and ask if execution exceeds 10 minutes
7. Stop and ask if encountering undefined error scenarios
8. Record results in structured YAML format
9. **MUST record F1 score in f1.txt after grading each team**
10. **DO NOT save context** between teams - this is repetitive work
