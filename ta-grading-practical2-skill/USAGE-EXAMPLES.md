# Usage Examples - Practical 2 Grading Skill

This file contains example conversations showing how to use the Practical 2 grading skill.

---

## Example 1: Grade a Single Team

**User Input:**
```
Grade Practical 2 for Team 004
```

**Claude's Response:**
```
I'll grade Team 004's Practical 2 assignment using a sub-agent.

[Creates Task with subagent_type="general-purpose"]

Grading Results for FDS25-T004:
- General: ✓ OK
- ContFeatureParam: ✓ Both methods correct
- BinFeatureParam: ✗ Incorrect additive smoothing (used alpha=1.0 instead of 0.0001)
- CatFeatureParam: ✓ Both methods correct
- FeatureParam Tests: Binary test failed due to upstream smoothing error
- NBC: ✓ Both fit() and predict() correct
- NBC Tests: ✓ OK
- compareNBCvsLR: ✓ OK
- Experiments: ✓ IRIS OK, ✓ Voting OK, ✓ Cancer OK

YAML file updated: /Users/dp/Desktop/TA agent/data/teacher/practical2/grading_files/FDS25-T004.yaml

Total deductions: 4 points (additive smoothing error)
```

---

## Example 2: Grade Multiple Teams in Parallel

**User Input:**
```
Grade Practical 2 for teams 004, 011, 018, and 025
```

**Claude's Response:**
```
I'll grade all 4 teams in parallel using separate sub-agents.

[Creates 4 Task instances simultaneously]

Team 004: Completed ✓
Team 011: Completed ✓
Team 018: Completed ✓
Team 025: Completed ✓

Summary:
- FDS25-T004: 4 points deducted (additive smoothing)
- FDS25-T011: 0 points deducted (perfect implementation)
- FDS25-T018: 12 points deducted (NBC.predict missing)
- FDS25-T025: 8 points deducted (ContFeatureParam.estimate incorrect)

All YAML files updated successfully.
```

---

## Example 3: Understanding Error Propagation

**Scenario:** Student has wrong variance calculation in ContFeatureParam, but correct NBC implementation.

**User Input:**
```
Grade Team 032's Practical 2
```

**Claude's Response:**
```
Grading FDS25-T032...

Issues found:
1. ContFeatureParam.estimate() - Incorrect standard deviation calculation
   - Used np.var() instead of np.std()
   - Key: 2_ContFeatureParam_estimate_incorrect_std (3 points)

2. FeatureParam_test - Continuous test failed
   - BUT failure is due to upstream error #1
   - Key: 2_FeatureParam_test_cont_incorrect_due_to_previous_mistake (0 points)

3. NBC.fit() - Implementation logic is CORRECT
   - Correctly calls theta_jc.estimate(X_jc) for each feature
   - Even though parameters are wrong due to #1, the fit() logic is sound
   - Key: 2_NBC_fit_ok (0 points)

4. NBC Tests - Failed due to upstream error #1
   - Key: 2_NBC_test_cont_incorrect_due_to_previous_mistake (0 points)

Total deductions: 3 points (only the original ContFeatureParam error)

Note: Student was NOT penalized for downstream effects of the upstream error.
```

---

## Example 4: Handling Missing Components

**User Input:**
```
Grade Team 046's Practical 2
```

**Claude's Response:**
```
Grading FDS25-T046...

Critical issues:
1. NBC.predict() is completely missing
   - Key: 2_NBC_predict_missing (12 points)

2. NBC_test cannot run
   - Tests failed because predict() is missing
   - Key: 2_NBC_test_missing (3 points)

3. compareNBCvsLR cannot run properly
   - Function tries to call nbc.predict() which doesn't exist
   - Key: 2_compareNBCvsLR_missing (10 points)

4. All experiments failed
   - experiment_iris: 2_experiment_iris_missing (10 points)
   - experiment_voting: 2_experiment_voting_missing (10 points)
   - experiment_cancer: 2_experiment_cancer_missing (5 points)

Other components were correct:
✓ General code quality
✓ ContFeatureParam (both methods)
✓ BinFeatureParam (both methods)
✓ CatFeatureParam (both methods)
✓ NBC.fit()

Total deductions: 50 points

YAML updated with all component statuses.
```

---

## Example 5: Checking Specific Component

**User Input:**
```
For Team 053, just check if they used the correct alpha value for additive smoothing
```

**Claude's Response:**
```
Checking additive smoothing for FDS25-T053...

Found in BinFeatureParam.estimate():
```python
theta = (np.sum(X) + ALPHA) / (len(X) + 2 * ALPHA)
```

Where ALPHA is defined as:
```python
ALPHA = 1.0  # for additive smoothing
```

❌ Issue found: Using ALPHA = 1.0
✓ Required: ALPHA = 0.0001

This is a common error. The assignment specifies alpha should be 0.0001, not 1.0 (Laplace smoothing).

Error key: 2_BinFeatureParam_estimate_incorrect_additive_smoothing (4 points)

Would you like me to complete the full grading for this team?
```

---

## Example 6: Bonus Task Evaluation

**User Input:**
```
Grade Team 109's Practical 2, pay special attention to the cancer experiment
```

**Claude's Response:**
```
Grading FDS25-T109 with focus on cancer experiment...

Cancer Experiment Analysis:
✓ Missing data handled correctly (dropped NA)
✓ Ordinal features encoded properly (age, menopause, tumor-size, inv-nodes)
✓ Unordered categorical features use one-hot encoding (breast-quad)
✓ Binary features encoded to 0/1 (node-caps, irradiat, breast)
✓ Continuous feature treated correctly (deg-malig)
✓ NBC initialized with correct feature types: ['c', 'c', 'c', 'c', 'b', 'r', 'b', 'b', 'b', 'b', 'b', 'b']
✓ Plot generated and shows comparison
✗ Minor issue: Processed unordered breast-quad as ordinal initially, but corrected with one-hot

Key: 2_experiment_cancer_process_unordered_as_ordinal (1 point)
But then corrected, so: 2_experiment_cancer_ok (0 points)

Other components:
✓ All FeatureParam classes correct
✓ NBC implementation correct
✓ IRIS and Voting experiments correct

Total deductions: 0 points (excellent work, including bonus!)

Student successfully completed all bonus tasks.
```

---

## Example 7: Handling Execution Timeouts

**User Input:**
```
Grade Team 067's Practical 2
```

**Claude's Response:**
```
Grading FDS25-T067...

Evaluating components:
✓ General, ContFeatureParam, BinFeatureParam, CatFeatureParam - All OK
✓ NBC.fit() and NBC.predict() - Both OK

Now testing compareNBCvsLR on IRIS dataset...
Running 200 iterations with 10 splits...

⚠️ Execution Warning: compareNBCvsLR has been running for 8 minutes.
The num_runs parameter is set to 2000 (instead of recommended 200).
This is causing extended execution time.

Options:
1. Wait for completion (may take 15+ minutes)
2. Stop execution and mark as incorrect implementation
3. Reduce num_runs and re-evaluate

What would you like me to do?
```

---

## Example 8: Verifying YAML Output

**User Input:**
```
Show me the YAML output for Team 011
```

**Claude's Response:**
```
YAML file for FDS25-T011:
/Users/dp/Desktop/TA agent/data/teacher/practical2/grading_files/FDS25-T011.yaml

Content:
```yaml
General:
    - key: 2_general_ok
ContFeatureParam_estimate:
    - key: 2_ContFeatureParam_estimate_ok
ContFeatureParam_get_log_probability:
    - key: 2_ContFeatureParam_get_log_probability_ok
BinFeatureParam_estimate:
    - key: 2_BinFeatureParam_estimate_ok
BinFeatureParam_get_log_probability:
    - key: 2_BinFeatureParam_get_log_probability_ok
CatFeatureParam_estimate:
    - key: 2_CatFeatureParam_estimate_ok
CatFeatureParam_get_log_probability:
    - key: 2_CatFeatureParam_get_log_probability_ok
FeatureParam_test:
    - key: 2_FeatureParam_test_ok
NBC_fit:
    - key: 2_NBC_fit_ok
NBC_predict:
    - key: 2_NBC_predict_ok
NBC_test:
    - key: 2_NBC_test_ok
compareNBCvsLR:
    - key: 2_compareNBCvsLR_ok
experiment_iris:
    - key: 2_experiment_iris_ok
experiment_voting:
    - key: 2_experiment_voting_ok
experiment_cancer:
    - key: 2_experiment_cancer_ok
```

Perfect implementation - all components correct, including bonus tasks!
Total: 0 points deducted.
```

---

## Example 9: Batch Processing All Teams

**User Input:**
```
Grade all teams for Practical 2
```

**Claude's Response:**
```
I'll grade all 19 teams in parallel using sub-agents...

Teams: 004, 011, 018, 025, 032, 039, 046, 053, 060, 067, 074, 081, 088, 095, 102, 109, 116, 123, 130

Creating 19 sub-agents for parallel processing...

[Progress updates as each team completes]

Completed: 19/19 teams ✓

Summary Statistics:
- Perfect implementations (0 points): 3 teams
- Minor errors (1-5 points): 8 teams
- Moderate errors (6-15 points): 5 teams
- Major errors (16+ points): 3 teams

Most common errors:
1. Incorrect additive smoothing (ALPHA=1.0 instead of 0.0001): 7 teams
2. Missing cancer experiment: 6 teams
3. Voting experiment data handling issues: 4 teams
4. NBC using loops instead of matrix operations: 2 teams

All YAML files generated successfully.
```

---

## Example 10: Troubleshooting Undefined Error

**User Input:**
```
Grade Team 130's Practical 2
```

**Claude's Response:**
```
Grading FDS25-T130...

Issue encountered:
Student implemented NBC using a completely different approach - they created a graphical model with factor graphs and belief propagation instead of the standard conditional probability approach.

This approach is:
- Theoretically valid for NBC
- Significantly more complex than required
- Not covered by our error key definitions

The implementation appears to work, but I cannot classify this under existing error keys:
- Not "missing" (it exists)
- Not "incorrect" (mathematically valid)
- Not "external_class" (implemented from scratch)
- Not covered by any specific error pattern

Recommendation needed:
1. Should this be accepted as correct (2_NBC_fit_ok)?
2. Should there be a deduction for using overly complex approach?
3. Should we request the student simplify to standard approach?

Please advise how to grade this case.
```

---

## Tips for Effective Usage

1. **Start with single teams** to verify the skill is working correctly
2. **Use parallel processing** for batch grading (Claude handles this automatically)
3. **Review error propagation** carefully - make sure downstream components aren't penalized twice
4. **Check YAML format** after grading to ensure proper structure
5. **Document unusual cases** that don't fit standard error keys

---

For more information, see:
- `SKILL.md` - Complete skill documentation
- `QUICK-REFERENCE.md` - Quick reference guide
- `README.md` - Installation and setup
