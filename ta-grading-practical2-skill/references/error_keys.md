# Error Key Reference

**IMPORTANT: Use ONLY these keys. Do not create custom keys.**

## General Code Quality

| Key | Points | Description |
|-----|--------|-------------|
| `2_general_ok` | 0 | Code quality is acceptable |
| `2_general_loop_over_data` | 4 | Use matrix operations rather than loops over rows |
| `2_general_NBC_separate_implementation` | 4 | Create one NBC class for different feature types |

## ContFeatureParam (Continuous Features)

### estimate() method

| Key | Points | Description |
|-----|--------|-------------|
| `2_ContFeatureParam_estimate_ok` | 0 | Continuous feature parameter estimation is correct |
| `2_ContFeatureParam_estimate_missing` | 8 | Missing or erroneous implementation |
| `2_ContFeatureParam_estimate_incorrect_mean` | 3 | Mean computation is incorrect |
| `2_ContFeatureParam_estimate_incorrect_std` | 3 | Variance/standard deviation computation is incorrect |
| `2_ContFeatureParam_estimate_incorrect_small_value` | 2 | Handling of zero variance is incorrect (should set to 1e-6) |

### get_log_probability() method

| Key | Points | Description |
|-----|--------|-------------|
| `2_ContFeatureParam_get_log_probability_ok` | 0 | Log probability calculation is correct |
| `2_ContFeatureParam_get_log_probability_missing` | 8 | Missing or erroneous implementation |
| `2_ContFeatureParam_get_log_probability_computed_probability_rather_than_log_probability` | 4 | Should compute log probabilities, not raw values |
| `2_ContFeatureParam_get_log_probability_incorrect` | 8 | Computation is incorrect |

## BinFeatureParam (Binary Features)

### estimate() method

| Key | Points | Description |
|-----|--------|-------------|
| `2_BinFeatureParam_estimate_ok` | 0 | Binary feature parameter estimation is correct |
| `2_BinFeatureParam_estimate_missing` | 8 | Missing or erroneous implementation |
| `2_BinFeatureParam_estimate_incorrect_theta` | 8 | Parameter p computation is incorrect |
| `2_BinFeatureParam_estimate_incorrect_additive_smoothing` | 4 | Additive smoothing (alpha=0.0001) implementation is incorrect |

### get_log_probability() method

| Key | Points | Description |
|-----|--------|-------------|
| `2_BinFeatureParam_get_log_probability_ok` | 0 | Log probability calculation is correct |
| `2_BinFeatureParam_get_log_probability_missing` | 8 | Missing or erroneous implementation |
| `2_BinFeatureParam_get_log_probability_computed_probability_rather_than_log_probability` | 4 | Should compute log probabilities, not raw values |
| `2_BinFeatureParam_get_log_probability_incorrect` | 8 | Computation is incorrect |

## CatFeatureParam (Categorical Features - BONUS)

### estimate() method

| Key | Points | Description |
|-----|--------|-------------|
| `2_CatFeatureParam_estimate_ok` | 0 | Categorical feature parameter estimation is correct |
| `2_CatFeatureParam_estimate_missing` | 1.5 | Missing or erroneous implementation |
| `2_CatFeatureParam_estimate_incorrect_theta` | 0.5 | Parameters computation is incorrect |
| `2_CatFeatureParam_estimate_incorrect_additive_smoothing` | 1 | Additive smoothing implementation is incorrect |

### get_log_probability() method

| Key | Points | Description |
|-----|--------|-------------|
| `2_CatFeatureParam_get_log_probability_ok` | 0 | Log probability calculation is correct |
| `2_CatFeatureParam_get_log_probability_missing` | 1.5 | Missing or erroneous implementation |
| `2_CatFeatureParam_get_log_probability_computed_probability_rather_than_log_probability` | 0.5 | Should compute log probabilities, not raw values |
| `2_CatFeatureParam_get_log_probability_incorrect` | 1 | Computation is incorrect |

## FeatureParam Tests

| Key | Points | Description |
|-----|--------|-------------|
| `2_FeatureParam_test_ok` | 0 | Feature parameter tests are correct |
| `2_FeatureParam_test_missing` | 3 | Tests missing or produce errors |
| `2_FeatureParam_test_cont_incorrect_due_to_previous_mistake` | 0 | Continuous test failure due to earlier issues |
| `2_FeatureParam_test_binary_incorrect_due_to_previous_mistake` | 0 | Binary test failure due to earlier issues |
| `2_FeatureParam_test_cat_incorrect_due_to_previous_mistake` | 0 | Categorical test failure due to earlier issues |

## NBC fit() Method

| Key | Points | Description |
|-----|--------|-------------|
| `2_NBC_fit_ok` | 0 | NBC fit implementation is correct |
| `2_NBC_fit_missing` | 12 | Missing or erroneous implementation |
| `2_NBC_fit_incorrect_pi` | 3 | Prior probability computation is incorrect |
| `2_NBC_fit_incorrect_theta_jc_cont` | 3 | Continuous theta computation is incorrect |
| `2_NBC_fit_incorrect_theta_jc_bin` | 3 | Binary theta computation is incorrect |
| `2_NBC_fit_incorrect_theta_jc_cat` | 1 | Categorical theta computation is incorrect |
| `2_NBC_fit_external_class` | 2 | Should not use external sklearn classes |

## NBC predict() Method

| Key | Points | Description |
|-----|--------|-------------|
| `2_NBC_predict_ok` | 0 | NBC predict implementation is correct |
| `2_NBC_predict_missing` | 12 | Missing or erroneous implementation |
| `2_NBC_predict_incorrect_prior` | 2 | Prior computation is incorrect |
| `2_NBC_predict_incorrect_class_conditional_cont` | 3 | Continuous conditional probability is incorrect |
| `2_NBC_predict_incorrect_class_conditional_bin` | 3 | Binary conditional probability is incorrect |
| `2_NBC_predict_incorrect_class_conditional_cat` | 1 | Categorical conditional probability is incorrect |
| `2_NBC_predict_incorrect_calculation_log_probability` | 4 | Should sum log probabilities, not multiply them |
| `2_NBC_predict_external_class` | 2 | Should not use external sklearn classes |

## NBC Tests

| Key | Points | Description |
|-----|--------|-------------|
| `2_NBC_test_ok` | 0 | NBC tests are correct |
| `2_NBC_test_missing` | 3 | Tests missing or produce errors |
| `2_NBC_test_cont_incorrect_due_to_previous_mistake` | 0 | Continuous test failure due to earlier issues |
| `2_NBC_test_binary_incorrect_due_to_previous_mistake` | 0 | Binary test failure due to earlier issues |
| `2_NBC_test_cat_incorrect_due_to_previous_mistake` | 0 | Categorical test failure due to earlier issues |

## compareNBCvsLR Function

| Key | Points | Description |
|-----|--------|-------------|
| `2_compareNBCvsLR_ok` | 0 | Comparison implementation is correct |
| `2_compareNBCvsLR_missing` | 10 | Missing or erroneous implementation |
| `2_compareNBCvsLR_incorrect_data_shuffle` | 2 | Data shuffling is incorrect |
| `2_compareNBCvsLR_incorrect_slicing_test_data` | 2 | Test data slicing (20% for test) is incorrect |
| `2_compareNBCvsLR_incorrect_slicing_training_data` | 2 | Training data slicing (80% for train) is incorrect |
| `2_compareNBCvsLR_incorrect_error_computation` | 2 | Classifier error computation is incorrect |
| `2_compareNBCvsLR_LR_implementation_missing` | 4 | Logistic regression model not implemented |

## Experiment: IRIS Dataset

| Key | Points | Description |
|-----|--------|-------------|
| `2_experiment_iris_ok` | 0 | IRIS experiment is correct |
| `2_experiment_iris_missing` | 10 | Missing or erroneous implementation |
| `2_experiment_iris_totally_incorrect` | 8 | Experiment is fundamentally incorrect |
| `2_experiment_iris_external_class` | 0 | Should not use external sklearn NBC classes |
| `2_experiment_iris_incorrect_NBC_feature_type` | 2 | NBC feature types are incorrect (should be all 'r') |
| `2_experiment_iris_incorrect_dataset_preparation` | 3 | Data preparation is incorrect |

## Experiment: Voting Dataset

| Key | Points | Description |
|-----|--------|-------------|
| `2_experiment_voting_ok` | 0 | Voting experiment is correct |
| `2_experiment_voting_missing` | 10 | Missing or erroneous implementation |
| `2_experiment_voting_incorrect_missing_data_handle` | 2 | Missing data handling is improper (should drop NA) |
| `2_experiment_voting_incorrect_text_data_handle` | 2 | Text data handling is improper (should encode to 0/1) |
| `2_experiment_voting_totally_incorrect` | 8 | Experiment is fundamentally incorrect |
| `2_experiment_voting_external_class` | 0 | Should not use external sklearn NBC classes |
| `2_experiment_voting_incorrect_NBC_feature_type` | 2 | NBC feature types are incorrect (should be all 'b') |

## Experiment: Cancer Dataset (BONUS)

| Key | Points | Description |
|-----|--------|-------------|
| `2_experiment_cancer_ok` | 0 | Cancer experiment is correct |
| `2_experiment_cancer_missing` | 5 | Missing or erroneous implementation |
| `2_experiment_cancer_totally_incorrect` | 5 | Experiment is fundamentally incorrect |
| `2_experiment_cancer_incorrect_missing_data_handle` | 1 | Missing data handling is improper |
| `2_experiment_cancer_incorrect_ordinal_data` | 1.5 | Ordinal data handling is improper |
| `2_experiment_cancer_incorrect_categorical_data` | 1.5 | Categorical data handling is improper |
| `2_experiment_cancer_plot_incorrect` | 1 | Plot is incorrect or missing |
| `2_experiment_cancer_process_ordinal_as_unordered` | 0 | Ordinal data treated as unordered categorical |
| `2_experiment_cancer_process_unordered_as_ordinal` | 1 | Unordered data treated as ordered categorical |
| `2_experiment_cancer_wrong_data_types` | 1 | Data types are incorrectly assigned |
