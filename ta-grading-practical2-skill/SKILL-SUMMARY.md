# Practical 2 Grading Skill - Complete Summary

## Skill Creation Complete ✓

This skill has been successfully created for grading student Practical 2 (Naive Bayes Classifier) assignments.

**Location:** `/Users/dp/Desktop/TA agent/ta-grading-practical2-skill/`

---

## File Structure

```
ta-grading-practical2-skill/
├── SKILL.md                 # Main skill definition (742 lines)
├── README.md                # Installation and overview (210 lines)
├── QUICK-REFERENCE.md       # Quick reference guide (238 lines)
├── USAGE-EXAMPLES.md        # Detailed usage examples (291 lines)
├── example-output.yaml      # Example grading output (33 lines)
└── SKILL-SUMMARY.md         # This file

Total: 1,514 lines of documentation
```

---

## What Each File Contains

### 1. SKILL.md (Main Skill Definition)
**Purpose:** Core skill that Claude reads when grading

**Sections:**
- Role and overview
- File paths and directory structure
- Assignment overview (15 components)
- Grading workflow with sub-agent instructions
- Complete error key reference (80+ keys)
- YAML output format
- Important grading philosophy (error propagation, implementation flexibility)
- Special considerations and requirements
- Execution constraints and verification checklist

**Key Features:**
- ✓ Mandatory sub-agent usage for each team
- ✓ Error propagation rules (errors don't cascade)
- ✓ Implementation flexibility (grade logic, not exact code)
- ✓ Strict error key enforcement
- ✓ Comments only for errors

### 2. README.md (User Documentation)
**Purpose:** Installation, setup, and overview for users

**Sections:**
- What the skill does
- Installation methods
- Usage instructions
- Component breakdown
- File structure requirements
- Key features explanation
- Output format
- Common issues and solutions
- Customization guide

**Best for:** Understanding how to install and use the skill

### 3. QUICK-REFERENCE.md (Cheat Sheet)
**Purpose:** Quick lookup guide for grading

**Sections:**
- Quick start commands
- Components checklist (15 components)
- Common errors to check
- Error propagation rules with examples
- YAML structure guide
- Point values reference
- Team numbers list
- File paths cheat sheet
- Troubleshooting guide
- Sub-agent usage explanation

**Best for:** Quick reference while grading

### 4. USAGE-EXAMPLES.md (Practical Examples)
**Purpose:** Real-world usage scenarios

**Contains 10 detailed examples:**
1. Grade a single team
2. Grade multiple teams in parallel
3. Understanding error propagation
4. Handling missing components
5. Checking specific component
6. Bonus task evaluation
7. Handling execution timeouts
8. Verifying YAML output
9. Batch processing all teams
10. Troubleshooting undefined error

**Best for:** Learning by example

### 5. example-output.yaml (Sample Output)
**Purpose:** Shows correct YAML format

**Features:**
- Complete example with all 15 components
- Shows correct format for OK keys (no comments)
- Shows correct format for error keys (with comments)
- Demonstrates error propagation (*_due_to_previous_mistake)

**Best for:** Verifying output format

---

## Key Concepts

### 1. Sub-Agent Architecture
Each team is graded by a dedicated sub-agent:
- Enables parallel processing
- Better resource management
- Isolated execution environments
- Cleaner organization

### 2. Error Propagation Rules
**Critical Rule:** Errors do NOT cascade downstream

Example:
```
❌ ContFeatureParam.estimate() → Wrong std calculation (3 points)
✅ NBC.fit() → Correctly calls estimate() (0 points, even though parameters are wrong)
```

Only penalize the FIRST occurrence of an error.

### 3. Implementation Flexibility
Students can:
- Use different code structures
- Take different approaches
- Implement differently from reference

As long as the logic is sound and requirements are met.

### 4. Strict Error Key Enforcement
- Must use ONLY predefined error keys
- Never create custom keys
- One key per component
- Comments only for errors

### 5. YAML Output Format
```yaml
Component_name:
    - key: error_key_or_ok_key
      comment: [ONLY if error key]
```

Rules:
- One key per component
- Comments ONLY when key indicates error
- Comments explain WHAT is wrong
- No comments for *_ok keys

---

## Components Being Graded (15 Total)

### Core Implementation (12 components)

1. **General** - Code quality (matrix operations, unified NBC)
2. **ContFeatureParam.estimate()** - Gaussian parameters
3. **ContFeatureParam.get_log_probability()** - Log density
4. **BinFeatureParam.estimate()** - Bernoulli parameters
5. **BinFeatureParam.get_log_probability()** - Log PMF
6. **CatFeatureParam.estimate()** - Multinoulli parameters (BONUS)
7. **CatFeatureParam.get_log_probability()** - Categorical log PMF (BONUS)
8. **FeatureParam_test** - Test cells verification
9. **NBC.fit()** - Prior and theta estimation
10. **NBC.predict()** - Prediction implementation
11. **NBC_test** - NBC test cells
12. **compareNBCvsLR** - Comparison function

### Experiments (3 components)

13. **experiment_iris** - All continuous features
14. **experiment_voting** - All binary features
15. **experiment_cancer** - Mixed features (BONUS)

---

## Error Key Categories (80+ Total)

| Category | Keys | Max Points |
|----------|------|------------|
| General | 3 | 4 |
| ContFeatureParam | 9 | 8 |
| BinFeatureParam | 9 | 8 |
| CatFeatureParam | 8 | 1.5 |
| FeatureParam Tests | 5 | 3 |
| NBC fit() | 7 | 12 |
| NBC predict() | 9 | 12 |
| NBC Tests | 5 | 3 |
| compareNBCvsLR | 7 | 10 |
| Experiment IRIS | 6 | 10 |
| Experiment Voting | 7 | 10 |
| Experiment Cancer | 10 | 5 |

---

## Common Errors to Watch For

### Critical Parameters
- **ALPHA = 0.0001** (NOT 1.0) - Most common error
- **Small value = 1e-6** for zero variance
- **Train/test split = 80/20**

### Implementation Issues
- Computing raw probabilities instead of log probabilities
- Using loops over data rows instead of matrix operations
- Creating separate NBC classes for different feature types
- Using sklearn NBC instead of implementing from scratch

### Experiment Issues
- Not handling missing data in Voting dataset
- Not encoding text values in Voting dataset
- Wrong feature types for datasets
- Not handling ordinal vs categorical data in Cancer dataset

---

## Quick Start Guide

### Step 1: Install the Skill
```bash
# Option 1: Copy to Claude skills directory
cp -r ta-grading-practical2-skill ~/.claude/skills/

# Option 2: Use in place (configure in Claude settings)
```

### Step 2: Use the Skill
Simply ask Claude:
```
Grade Practical 2 for Team 004
```

Or for multiple teams:
```
Grade Practical 2 for teams: 004, 011, 018, 025
```

### Step 3: Verify Output
Check the generated YAML files:
```
/Users/dp/Desktop/TA agent/data/teacher/practical2/grading_files/FDS25-T*.yaml
```

---

## File Paths Configuration

The skill is pre-configured for:

**Student submissions:**
```
/Users/dp/Desktop/TA agent/data/students/FDS25-Txxx/practical2/
```

**Reference solution:**
```
/Users/dp/Desktop/TA agent/data/teacher/practical2/Practical2_skeleton_solution.ipynb
```

**Output YAML files:**
```
/Users/dp/Desktop/TA agent/data/teacher/practical2/grading_files/
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

## Team Numbers

19 teams available for grading:
```
004, 011, 018, 025, 032, 039, 046, 053, 060, 067,
074, 081, 088, 095, 102, 109, 116, 123, 130
```

---

## Grading Philosophy

1. **Implementation Flexibility**
   - Grade logic and methodology
   - Not exact code matching
   - Students can use different approaches

2. **No Error Propagation**
   - Only penalize first occurrence
   - Don't cascade penalties downstream
   - Evaluate each component independently

3. **Strict Key Enforcement**
   - Use ONLY predefined error keys
   - Never create custom keys
   - One key per component

4. **Comments for Errors Only**
   - No comments for correct implementations
   - Comments explain WHAT is wrong
   - Keep comments concise

5. **Sub-Agent Processing**
   - Each team gets dedicated sub-agent
   - Enables parallel grading
   - Better resource management

---

## Advanced Features

### Parallel Processing
Grade multiple teams simultaneously:
```
Grade Practical 2 for teams: 004, 011, 018, 025, 032, 039, 046, 053
```
Claude automatically creates 8 sub-agents and processes in parallel.

### Error Propagation Handling
Automatically detects upstream errors and avoids double-penalization:
```yaml
ContFeatureParam_estimate:
    - key: 2_ContFeatureParam_estimate_incorrect_std
      comment: Used np.var() instead of np.std()

NBC_fit:
    - key: 2_NBC_fit_ok  # NOT penalized even though parameters are wrong
```

### Bonus Task Detection
Automatically detects and evaluates bonus components:
- CatFeatureParam implementation
- Cancer dataset experiment

---

## Troubleshooting

### Skill Not Loading
1. Check file location: `~/.claude/skills/ta-grading-practical2-skill/`
2. Verify `SKILL.md` exists
3. Restart Claude Code

### Execution Too Slow
- Normal for NBC training (5-10 minutes)
- If >10 minutes, skill will ask for guidance
- Check if student used excessive num_runs

### Undefined Errors
- Skill will stop and ask user
- Document the case
- Consult with instructor

### Dataset Path Issues
- Automatically fixed by skill
- No manual intervention needed

---

## Next Steps

1. **Review the documentation:**
   - Start with `README.md` for installation
   - Use `QUICK-REFERENCE.md` while grading
   - Refer to `USAGE-EXAMPLES.md` for scenarios

2. **Test the skill:**
   - Grade a single team first
   - Verify YAML output format
   - Check error handling

3. **Batch processing:**
   - Once verified, grade multiple teams
   - Use parallel processing
   - Monitor for any issues

4. **Customize if needed:**
   - Modify paths in `SKILL.md`
   - Adjust error keys if rubric changes
   - Update team numbers list

---

## Support Resources

| Need | See File |
|------|----------|
| Installation | README.md |
| Quick commands | QUICK-REFERENCE.md |
| Usage examples | USAGE-EXAMPLES.md |
| Complete details | SKILL.md |
| Output format | example-output.yaml |
| Overview | This file |

---

## Statistics

- **Total files:** 6
- **Total lines:** 1,514
- **Total components:** 15
- **Total error keys:** 80+
- **Supported teams:** 19
- **Documentation pages:** 5

---

## Summary

This skill provides a complete, production-ready solution for grading Practical 2 assignments with:

✓ Comprehensive error key coverage
✓ Intelligent error propagation handling
✓ Parallel processing via sub-agents
✓ Strict YAML format enforcement
✓ Implementation flexibility
✓ Detailed documentation
✓ Practical examples
✓ Quick reference guides

**Ready to use immediately!**

Simply copy to your skills directory and start grading:
```
Grade Practical 2 for Team 004
```

---

## Version Information

- **Created:** December 11, 2024
- **Skill Version:** 1.0
- **Target Assignment:** Practical 2 - Naive Bayes Classifier
- **Course:** FDS-25
- **Compatible with:** Claude Code (Anthropic skills format)

---

For questions or issues, refer to the documentation files or consult the course instructor.
