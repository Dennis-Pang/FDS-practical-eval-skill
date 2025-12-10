# Task 2: Exploratory Data Analysis (EDA) and PCA

## Task Description

Students must perform exploratory data analysis to understand the dataset and apply Principal Component Analysis (PCA) for dimensionality reduction.

## Requirements

### Part 1: Class Imbalance Analysis
- Identify and visualize class distribution
- Use plot or table to show class imbalance
- Discuss implications of imbalance

### Part 2: PCA Implementation
- Perform PCA for dimensionality reduction
- Create PCA visualization (scatter plot)
- Analyze and interpret PCA results

## Error Keys

| Key | Points | Description |
|-----|--------|-------------|
| `2_task_2_ok` | 0 | Task solved correctly |
| `2_ClassImbalance_not_found` | 1 | Class imbalance not identified via plot or table |
| `2_PCA_missing_or_wrong` | 1 | PCA not performed or wrong |
| `2_PCA_Plot_missing_or_wrong` | 1 | PCA Plot not done or wrong |
| `2_PCA_Plot_text_analysis_missing_or_wrong` | 1 | Plot text based analysis not done or conclusions are wrong |

## What to Check

### Class Imbalance
- [ ] Plot or table showing class distribution
- [ ] Clear visualization of imbalance
- [ ] Discussion or acknowledgment of imbalance

### PCA
- [ ] PCA is implemented correctly
- [ ] Appropriate number of components selected
- [ ] PCA scatter plot created
- [ ] Plot has proper labels and legend
- [ ] Text analysis interpreting PCA results
- [ ] Conclusions drawn from PCA visualization

## Common Issues

1. **Missing class imbalance analysis**: No plot or table showing class distribution
2. **Wrong PCA implementation**: Incorrect parameters or usage
3. **Missing PCA plot**: PCA performed but not visualized
4. **Poor visualization**: Plot missing labels, legend, or clarity
5. **Missing interpretation**: No text analysis of PCA results

## Evaluation Notes

- Accept different visualization methods (bar plot, pie chart, table)
- Focus on whether students identified the imbalance, not the exact format
- PCA plots may use different styling - check for correct data representation
- Text analysis should show understanding of what PCA reveals about the data

## Error Propagation Consideration

- If Task 1 (label encoding) was wrong, class distribution numbers may be affected
- Grade Task 2 based on implementation logic, not output correctness
- If the plotting/analysis code is correct but data is wrong due to upstream error, mark Task 2 as correct
