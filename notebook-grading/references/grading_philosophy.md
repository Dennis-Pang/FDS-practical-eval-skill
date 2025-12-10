# Grading Philosophy

## Core Principles

### 1. Implementation Flexibility

**Student implementations DO NOT need to match the reference solution exactly.**

- Students may use different approaches, algorithms, or code structures
- Grade based on whether their approach is **logically sound and meets requirements**
- Focus on: correctness of results, proper methodology, required outputs
- The reference solution is for YOUR understanding, not for exact matching

### 2. Error Propagation Rule (CRITICAL)

**Errors DO NOT propagate downstream.**

If Task X has an error that causes Task Y's output to be wrong, but Task Y's implementation is logically correct:
- Mark Task X as incorrect (assign appropriate error key)
- Mark Task Y as correct (if the implementation logic is sound)

## Error Propagation Examples

### Example Scenario 1

```
Task 1: Label Encoding
- Student incorrectly encoded labels (used 0,1 instead of 1,2)
- Error key: 1_Wrong_or_Missing_Label_encoding

Task 2: Class Distribution Analysis
- Student's code correctly counts classes and creates bar plot
- BUT the numbers are wrong because of Task 1's incorrect encoding
- Decision: Mark Task 2 as CORRECT (2_task_2_ok)
- Reasoning: The implementation logic is sound, error originated upstream
```

### Example Scenario 2

```
Task 2: PCA Implementation
- Student used wrong number of components (n_components=5 instead of 2)
- Error key: 2_PCA_missing_or_wrong

Task 3: Model Training on PCA Features
- Student correctly trained both kNN and Logistic Regression on PCA features
- BUT model performance is suboptimal due to wrong PCA components
- Decision: Mark Task 3 as CORRECT (3_task_3_ok)
- Reasoning: Model training logic is correct, PCA error is upstream
```

## Evaluation Process for Error Propagation

When grading sequential tasks where Task B depends on Task A's output:

1. **Identify if Task A has an error**
2. **Identify if Task B's implementation logic is correct**
3. **If Task A is wrong BUT Task B's logic is sound** → Mark only Task A as incorrect
4. **Do NOT penalize Task B** for using incorrect data from Task A

## Common Error Propagation Scenarios

| Upstream Error | Downstream Task | How to Grade |
|----------------|-----------------|--------------|
| Wrong label encoding (Task 1) | Class imbalance plot (Task 2) | Task 1: incorrect, Task 2: correct (if plot logic is right) |
| Wrong PCA components (Task 2) | Model training on PCA features (Task 3) | Task 2: incorrect, Task 3: correct (if model training logic is right) |
| Wrong feature engineering (Task 1) | Model uses those features (Task 3) | Task 1: incorrect, Task 3: correct (if model logic is right) |

## Key Question to Ask

**"If the upstream task had been correct, would this downstream task's implementation produce correct results?"**

- **If YES** → Mark downstream task as correct
- **If NO** → Mark downstream task as incorrect (it has its own error)

## Grading Principle Summary

- Evaluate the **logic and methodology** of each task independently
- Do NOT penalize students twice for the same upstream error
- Only mark the FIRST occurrence of an error
- Downstream tasks should be judged on implementation correctness, not output correctness caused by upstream errors
