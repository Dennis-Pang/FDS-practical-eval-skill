---
name: ta-grading-practical2
description: Grade Practical 2 (Naive Bayes Classifier) Jupyter notebook assignments. Use when grading NBC assignments, Practical 2, or FDS25-T team submissions for the second practical. Evaluates feature parameter classes, NBC implementation, and experiments on IRIS/Voting/Cancer datasets.
---

# Practical 2 Grading Skill

Grade student Naive Bayes Classifier implementations.

## Assignment Overview

Students implement:
1. **Feature Parameter Classes**: ContFeatureParam, BinFeatureParam, CatFeatureParam (bonus)
2. **NBC Class**: `fit()` and `predict()` methods
3. **Comparison Function**: `compareNBCvsLR()`
4. **Experiments**: IRIS, Voting, Cancer (bonus)

## File Paths

| Resource | Path |
|----------|------|
| Reference Solution | `/Users/dp/Desktop/TA agent/data/teacher/practical2/Practical2_skeleton_solution.ipynb` |
| Student Submissions | `/Users/dp/Desktop/TA agent/data/students/FDS25-Txxx/practical2/` |
| Datasets | `/Users/dp/Desktop/TA agent/data/teacher/practical2/` |
| Grading Output | `/Users/dp/Desktop/TA agent/data/teacher/practical2/grading_files/FDS25-Txxx.yaml` |

**Teams:** 004, 011, 018, 025, 032, 039, 046, 053, 060, 067, 074, 081, 088, 095, 102, 109, 116, 123, 130

## Grading Workflow

**CRITICAL: Use sub-agents for grading each team.**

```
Task(
  subagent_type="general-purpose",
  description="Grade Team XXX Practical 2",
  prompt="""Grade FDS25-TXXX Practical 2.

Read skill references:
- references/error_keys.md - All error keys
- references/grading_philosophy.md - Error propagation rules
- references/yaml_format.md - Output format
- references/implementation_requirements.md - NBC requirements

Workflow:
1. Find notebooks in: /Users/dp/Desktop/TA agent/data/students/FDS25-TXXX/practical2/
2. Fix dataset paths → /Users/dp/Desktop/TA agent/data/teacher/practical2/
3. Evaluate all 15 components (see error_keys.md)
4. Update /Users/dp/Desktop/TA agent/data/teacher/practical2/grading_files/FDS25-TXXX.yaml

Return: Team, errors per section, YAML updated, issues."""
)
```

## Core Grading Principles

### 1. Implementation Flexibility
Student implementations DO NOT need to match reference exactly. Grade on logical soundness.

### 2. Error Non-Propagation (CRITICAL)
**Errors do NOT cascade downstream.** If upstream component is wrong but downstream logic is correct, only mark upstream as incorrect.

See `references/grading_philosophy.md` for examples.

## Components to Evaluate

| Component | Reference |
|-----------|-----------|
| General Code Quality | `references/error_keys.md` |
| ContFeatureParam (estimate, get_log_probability) | `references/error_keys.md` |
| BinFeatureParam (estimate, get_log_probability) | `references/error_keys.md` |
| CatFeatureParam (bonus) | `references/error_keys.md` |
| FeatureParam Tests | `references/error_keys.md` |
| NBC fit() | `references/error_keys.md` |
| NBC predict() | `references/error_keys.md` |
| NBC Tests | `references/error_keys.md` |
| compareNBCvsLR | `references/error_keys.md` |
| Experiments (IRIS, Voting, Cancer) | `references/error_keys.md` |

## Critical Checks

1. **Additive Smoothing**: Must use `alpha = 0.0001` (NOT 1.0)
2. **Log Probabilities**: `get_log_probability()` must return log values
3. **Matrix Operations**: No loops over data rows
4. **Single NBC Class**: One class for all feature types

See `references/implementation_requirements.md` for details.

## Output Format

Use YAML format with one key per component. Comments only for errors.

See `references/yaml_format.md` for template and examples.

## Execution Constraints

- Fix dataset paths BEFORE executing code
- If execution exceeds 10 minutes → STOP and ask user
- If error not in key table → STOP and ask user
- DO NOT save context between teams

## Resources

- `references/error_keys.md` - Complete error key reference
- `references/grading_philosophy.md` - Error propagation rules
- `references/yaml_format.md` - YAML output format
- `references/implementation_requirements.md` - NBC implementation requirements
