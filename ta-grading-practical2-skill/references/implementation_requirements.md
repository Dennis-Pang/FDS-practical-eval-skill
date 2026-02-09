# Implementation Requirements

## NBC Core Requirements

Students MUST:
1. Implement NBC from scratch (cannot use sklearn.naive_bayes)
2. Use matrix operations (avoid loops over data rows)
3. Handle all computations in log space (avoid underflow)
4. Support multiple feature types in a single NBC class

## Common Mistakes

| Mistake | Error Key |
|---------|-----------|
| Looping over data rows | `2_general_loop_over_data` |
| Separate NBC classes for feature types | `2_general_NBC_separate_implementation` |
| Using external sklearn NBC | `*_external_class` keys |

## Additive Smoothing (CRITICAL)

**Required value: `alpha = 0.0001`**

- Many students incorrectly use `alpha = 1.0` (Laplace smoothing)
- If wrong alpha value → assign appropriate smoothing error key

## Log Probabilities (CRITICAL)

`get_log_probability()` must return `log(P(x|theta))`, NOT `P(x|theta)`

- Common mistake: returning raw probabilities
- Error key: `*_computed_probability_rather_than_log_probability`

## compareNBCvsLR Requirements

The function should:
1. Shuffle data and split 80% train / 20% test
2. Train with increasing training data (10%, 20%, ..., 100%)
3. Repeat `num_runs` times (default 200)
4. Average test errors across runs
5. Return: `nbc_errors, lr_errors`

## Experiment Requirements

### IRIS
- All features: continuous ('r')
- Load: `sklearn.datasets.load_iris`

### Voting
- All features: binary ('b')
- Handle missing values (drop NA)
- Encode text to 0/1
- Use ~100 data points

### Cancer (BONUS)
- Mixed features: continuous, binary, categorical, ordinal
- Handle missing values
- Handle ordinal data (age ranges, tumor sizes)
- One-hot encode unordered categorical features
- Generate comparison plots

## Test Cells Reference

| Cell | Tests |
|------|-------|
| 14-15 | ContFeatureParam |
| 15 | BinFeatureParam |
| 16 | CatFeatureParam (bonus) |
| 21 | NBC on IRIS |
| 22 | NBC on binary dataset |
| 23 | NBC on categorical (bonus) |

## Test Failure Evaluation

- Test passes → Component likely correct
- Test fails → Determine cause:
  - Error in component itself → mark incorrect
  - Error in upstream component → use `*_incorrect_due_to_previous_mistake` (0 points)
