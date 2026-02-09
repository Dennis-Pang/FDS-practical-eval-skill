# YAML Output Format

## Template Structure

```yaml
General:
    - key: [error_key_here]
      comment: [only if error - explain what went wrong]
ContFeatureParam_estimate:
    - key: [error_key_here]
      comment: [only if error]
ContFeatureParam_get_log_probability:
    - key: [error_key_here]
      comment: [only if error]
BinFeatureParam_estimate:
    - key: [error_key_here]
      comment: [only if error]
BinFeatureParam_get_log_probability:
    - key: [error_key_here]
      comment: [only if error]
CatFeatureParam_estimate:
    - key: [error_key_here]
      comment: [only if error]
CatFeatureParam_get_log_probability:
    - key: [error_key_here]
      comment: [only if error]
FeatureParam_test:
    - key: [error_key_here]
      comment: [only if error]
NBC_fit:
    - key: [error_key_here]
      comment: [only if error]
NBC_predict:
    - key: [error_key_here]
      comment: [only if error]
NBC_test:
    - key: [error_key_here]
      comment: [only if error]
compareNBCvsLR:
    - key: [error_key_here]
      comment: [only if error]
experiment_iris:
    - key: [error_key_here]
      comment: [only if error]
experiment_voting:
    - key: [error_key_here]
      comment: [only if error]
experiment_cancer:
    - key: [error_key_here]
      comment: [only if error]
```

## YAML Rules

1. **Each component MUST have exactly one key**
2. **Use `comment:` field ONLY for explaining errors** (not for correct implementations)
3. **Comments should be concise and specific**
4. **No extra fields or keys allowed**
5. **If key is `*_ok`, DO NOT include a comment field**

## Example: Mixed Results

```yaml
General:
    - key: 2_general_ok
ContFeatureParam_estimate:
    - key: 2_ContFeatureParam_estimate_ok
ContFeatureParam_get_log_probability:
    - key: 2_ContFeatureParam_get_log_probability_ok
BinFeatureParam_estimate:
    - key: 2_BinFeatureParam_estimate_incorrect_additive_smoothing
      comment: Used alpha=1.0 instead of required alpha=0.0001
BinFeatureParam_get_log_probability:
    - key: 2_BinFeatureParam_get_log_probability_ok
CatFeatureParam_estimate:
    - key: 2_CatFeatureParam_estimate_ok
CatFeatureParam_get_log_probability:
    - key: 2_CatFeatureParam_get_log_probability_ok
FeatureParam_test:
    - key: 2_FeatureParam_test_binary_incorrect_due_to_previous_mistake
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
    - key: 2_experiment_voting_missing
      comment: Voting experiment section is completely missing from notebook
experiment_cancer:
    - key: 2_experiment_cancer_ok
```

## Comment Guidelines

### Good Comments
- Concise and specific
- Explain what's wrong
- Help student understand the grading decision

### Examples

```yaml
BinFeatureParam_estimate:
    - key: 2_BinFeatureParam_estimate_incorrect_additive_smoothing
      comment: Used alpha=1.0 instead of required alpha=0.0001
```

```yaml
NBC_predict:
    - key: 2_NBC_predict_incorrect_calculation_log_probability
      comment: Multiplied probabilities instead of summing log probabilities
```

## File Naming

- **Pattern:** `FDS25-Txxx.yaml`
- **Location:** `/Users/dp/Desktop/TA agent/data/teacher/practical2/grading_files/`
