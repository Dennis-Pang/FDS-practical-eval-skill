# Quick Reference Guide - Practical 2 Grading

## Quick Start

**Grade a single team:**
```
Grade Practical 2 for Team 004
```

**Grade multiple teams:**
```
Grade Practical 2 for teams: 004, 011, 018, 025
```

---

## Components Checklist

Use this checklist to track what gets graded:

### Core Implementation (12 components)
- [ ] **General** - Code quality, matrix operations, unified NBC class
- [ ] **ContFeatureParam.estimate()** - Mean and std computation
- [ ] **ContFeatureParam.get_log_probability()** - Log probability calculation
- [ ] **BinFeatureParam.estimate()** - Theta computation with additive smoothing (alpha=0.0001)
- [ ] **BinFeatureParam.get_log_probability()** - Log probability calculation
- [ ] **CatFeatureParam.estimate()** - Multinoulli parameters (BONUS)
- [ ] **CatFeatureParam.get_log_probability()** - Log probability for categorical (BONUS)
- [ ] **FeatureParam_test** - Test cells for feature parameters
- [ ] **NBC.fit()** - Prior probabilities (pi) and theta_jc for all feature types
- [ ] **NBC.predict()** - Log probability summation and argmax
- [ ] **NBC_test** - Test cells for NBC implementation
- [ ] **compareNBCvsLR** - Train/test split, progressive training, error computation

### Experiments (3 components)
- [ ] **experiment_iris** - All continuous features
- [ ] **experiment_voting** - All binary features, handle missing data
- [ ] **experiment_cancer** - Mixed features (BONUS)

---

## Common Errors to Check

### Critical Parameters
- [ ] **ALPHA = 0.0001** (NOT 1.0) - for additive smoothing
- [ ] **Small value = 1e-6** - for zero variance handling
- [ ] **Train/test split = 80/20** - in compareNBCvsLR

### Implementation Requirements
- [ ] **Log probabilities** - NOT raw probabilities in get_log_probability()
- [ ] **Matrix operations** - NOT loops over data rows
- [ ] **Unified NBC class** - NOT separate classes for different feature types
- [ ] **No sklearn NBC** - Must implement from scratch

### Experiment-Specific
- [ ] **IRIS** - feature_types=['r', 'r', 'r', 'r']
- [ ] **Voting** - feature_types=['b'] * 16, drop NA, encode text to 0/1
- [ ] **Cancer** - Handle ordinal, categorical, and binary features

---

## Error Propagation Rules

**Golden Rule: Errors DO NOT cascade**

### Example 1: Upstream error doesn't penalize downstream
```
❌ BinFeatureParam.estimate() - Wrong additive smoothing (4 points)
✅ NBC.fit() - Correctly calls estimate() for each feature (0 points)
```
Result: Mark BinFeatureParam as incorrect, NBC.fit as correct

### Example 2: Tests failing due to upstream errors
```
❌ ContFeatureParam.estimate() - Wrong std calculation (3 points)
✅ FeatureParam_test - Test logic is correct (0 points, use *_due_to_previous_mistake)
```
Result: Mark ContFeatureParam as incorrect, test as "incorrect_due_to_previous_mistake"

---

## YAML Structure Quick Guide

```yaml
# For correct implementations - NO comment
General:
    - key: 2_general_ok

# For errors - WITH comment
BinFeatureParam_estimate:
    - key: 2_BinFeatureParam_estimate_incorrect_additive_smoothing
      comment: Used ALPHA=1.0 instead of 0.0001

# For test failures due to upstream - NO comment
FeatureParam_test:
    - key: 2_FeatureParam_test_binary_incorrect_due_to_previous_mistake
```

**Rules:**
- ✅ ONE key per component (never multiple)
- ✅ Comment ONLY when error key is used (not *_ok keys)
- ✅ Comments should explain WHAT is wrong, not HOW to fix
- ❌ NO comments for correct implementations

---

## Point Values Quick Reference

### High-Value Components (10-12 points)
- Missing NBC.fit() or NBC.predict() → **12 points**
- Missing compareNBCvsLR() → **10 points**
- Missing experiments (IRIS, Voting) → **10 points each**

### Medium-Value Components (8 points)
- Missing/incorrect FeatureParam methods → **8 points**

### Low-Value Components (1-4 points)
- General code quality issues → **4 points**
- Log vs raw probability → **4 points**
- Additive smoothing errors → **1-4 points**
- Individual parameter errors → **1-3 points**

### Bonus Components (0.5-5 points)
- Cancer experiment errors → **1-5 points**
- CatFeatureParam errors → **0.5-1.5 points**

---

## Team Numbers

Available teams to grade:
```
004, 011, 018, 025, 032, 039, 046, 053, 060, 067,
074, 081, 088, 095, 102, 109, 116, 123, 130
```

---

## File Paths Cheat Sheet

**Student notebooks:**
```
/Users/dp/Desktop/TA agent/data/students/FDS25-T[XXX]/practical2/
```

**Reference solution:**
```
/Users/dp/Desktop/TA agent/data/teacher/practical2/Practical2_skeleton_solution.ipynb
```

**Output YAML files:**
```
/Users/dp/Desktop/TA agent/data/teacher/practical2/grading_files/FDS25-T[XXX].yaml
```

**Datasets:**
```
/Users/dp/Desktop/TA agent/data/teacher/practical2/
├── voting.csv
├── breast-cancer.csv
├── binary_test.csv
└── categorical_test.csv
```

---

## Troubleshooting

### Issue: Execution takes too long
- **Threshold:** 10 minutes
- **Action:** Stop and report to user

### Issue: Undefined error not in key table
- **Action:** Stop and ask user for guidance

### Issue: Student notebook has errors
- **Action:** Record specific error key, continue grading other components

### Issue: Dataset path errors
- **Action:** Automatically fixed by skill before execution

---

## Sub-Agent Usage

The skill automatically creates sub-agents for each team:
```python
Task(
  subagent_type="general-purpose",
  description="Grade Team XXX Practical 2",
  prompt="..."
)
```

**Benefits:**
- ✅ Parallel processing
- ✅ Better resource management
- ✅ Isolated execution per team
- ✅ Cleaner organization

**You don't need to create sub-agents manually** - just ask Claude to grade teams!

---

## Grading Philosophy Summary

1. **Implementation Flexibility** - Students can use different approaches
2. **No Error Propagation** - Only penalize the FIRST occurrence of an error
3. **Logic over Output** - Grade the methodology, not just the results
4. **Strict Key Enforcement** - Use ONLY predefined error keys
5. **Comments for Errors Only** - No comments for correct implementations

---

## Need More Details?

- **Full documentation:** See `SKILL.md`
- **Example output:** See `example-output.yaml`
- **Installation guide:** See `README.md`
