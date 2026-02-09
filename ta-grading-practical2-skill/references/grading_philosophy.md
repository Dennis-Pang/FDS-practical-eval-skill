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

If Component X has an error that causes Component Y's output to be wrong, but Component Y's implementation is logically correct:
- Mark Component X as incorrect (assign appropriate error key)
- Mark Component Y as correct (if the implementation logic is sound)

## Error Propagation Examples

### Example 1: ContFeatureParam affects NBC

```
ContFeatureParam.estimate():
- Student incorrectly computed variance (forgot to square the deviations)
- Error key: 2_ContFeatureParam_estimate_incorrect_std

NBC.fit() using ContFeatureParam:
- Student's fit() code correctly calls theta_jc.estimate(X_jc) for each class
- BUT the stored parameters are wrong because of upstream error
- Decision: Mark NBC.fit() as CORRECT (2_NBC_fit_ok)
- Reasoning: The fit() implementation logic is sound, error originated upstream
```

### Example 2: BinFeatureParam affects NBC

```
BinFeatureParam.estimate():
- Student used alpha=1.0 instead of alpha=0.0001
- Error key: 2_BinFeatureParam_estimate_incorrect_additive_smoothing

NBC.predict() using BinFeatureParam:
- Student's predict() correctly sums log probabilities
- Decision: Mark NBC.predict() as CORRECT (2_NBC_predict_ok)
- Reasoning: The predict() logic is correct, smoothing error is upstream
```

## Evaluation Process

When grading sequential components where Component B depends on Component A:

1. **Identify if Component A has an error**
2. **Identify if Component B's implementation logic is correct**
3. **If Component A is wrong BUT Component B's logic is sound** → Mark only Component A as incorrect
4. **Do NOT penalize Component B** for using incorrect data from Component A

## Common Error Propagation Scenarios

| Upstream Error | Downstream Component | How to Grade |
|----------------|---------------------|--------------|
| Wrong variance (ContFeatureParam) | NBC.fit() uses ContFeatureParam | ContFeatureParam: incorrect, NBC.fit(): correct |
| Wrong smoothing (BinFeatureParam) | NBC predictions | BinFeatureParam: incorrect, NBC: correct |
| Wrong theta values (NBC.fit) | NBC.predict() | NBC.fit: incorrect, NBC.predict: correct |
| Wrong NBC implementation | compareNBCvsLR | NBC: incorrect, compareNBCvsLR: correct |
| Wrong NBC implementation | Experiments | NBC: incorrect, Experiments: correct |

## Key Question

**"If the upstream component had been correct, would this downstream component's implementation produce correct results?"**

- **If YES** → Mark downstream component as correct
- **If NO** → Mark downstream component as incorrect (it has its own error)

## Summary

- Evaluate the **logic and methodology** of each component independently
- Do NOT penalize students twice for the same upstream error
- Only mark the FIRST occurrence of an error
- Downstream components should be judged on implementation correctness, not output correctness caused by upstream errors
