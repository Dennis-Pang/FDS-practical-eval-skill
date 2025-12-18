# TA Grading Skill for Practical 2 (NBC Assignment)

This is a Claude Code skill for grading student Jupyter notebook assignments for Practical 2: Naive Bayes Classifier implementation.

## What This Skill Does

This skill enables Claude to act as a Teaching Assistant (TA) agent that:
- Grades student implementations of Naive Bayes Classifier from scratch
- Evaluates feature parameter classes (Continuous, Binary, Categorical)
- Checks NBC fit() and predict() methods
- Verifies experiment implementations (IRIS, Voting, Cancer datasets)
- Generates structured YAML grading reports
- Uses sub-agents for parallel processing of multiple teams

## Installation

### Method 1: Copy to Claude Skills Directory

1. Copy this entire folder to your Claude skills directory:
   ```bash
   cp -r ta-grading-practical2-skill ~/.claude/skills/
   ```

2. Restart Claude Code or reload skills

### Method 2: Use in Place

Point Claude Code to use this skill directory directly by adding to your Claude configuration.

## Usage

### Basic Usage

Simply ask Claude to grade a team's Practical 2 assignment:

```
Grade Team 004's Practical 2 assignment
```

or

```
Grade Practical 2 for FDS25-T004
```

### Batch Grading Multiple Teams

```
Grade Practical 2 for teams: T004, T011, T018, T025
```

Claude will automatically:
1. Use sub-agents to grade each team in parallel
2. Fix dataset paths in student notebooks
3. Execute and evaluate all components
4. Generate YAML grading files

### What Gets Graded

The skill evaluates 15 components:

**Core Implementation:**
1. General Code Quality (matrix operations, unified NBC class)
2. ContFeatureParam.estimate()
3. ContFeatureParam.get_log_probability()
4. BinFeatureParam.estimate()
5. BinFeatureParam.get_log_probability()
6. CatFeatureParam.estimate() (bonus)
7. CatFeatureParam.get_log_probability() (bonus)
8. FeatureParam Tests
9. NBC.fit()
10. NBC.predict()
11. NBC Tests
12. compareNBCvsLR() function

**Experiments:**
13. IRIS Dataset Experiment
14. Voting Dataset Experiment
15. Cancer Dataset Experiment (bonus)

## File Structure

```
ta-grading-practical2-skill/
├── SKILL.md              # Main skill definition (grading instructions)
├── README.md             # This file
└── example-output.yaml   # Example grading result
```

## Configuration

### Required Paths (Already Configured)

The skill expects the following directory structure:

```
/Users/dp/Desktop/TA agent/data/
├── teacher/
│   └── practical2/
│       ├── Practical2_skeleton_solution.ipynb
│       ├── grading_files/
│       │   ├── FDS25-T004.yaml
│       │   ├── FDS25-T011.yaml
│       │   └── ...
│       ├── voting.csv
│       ├── breast-cancer.csv
│       ├── binary_test.csv
│       └── categorical_test.csv
└── students/
    ├── FDS25-T004/
    │   └── practical2/
    │       └── [student notebooks]
    ├── FDS25-T011/
    │   └── practical2/
    │       └── [student notebooks]
    └── ...
```

## Key Features

### 1. Sub-Agent Architecture
Each team is graded by a dedicated sub-agent, enabling:
- Parallel processing of multiple teams
- Better resource management
- Isolated execution environments

### 2. Error Propagation Handling
The skill implements intelligent error propagation rules:
- Errors do NOT cascade downstream
- If Component A has an error that affects Component B's output, but Component B's logic is correct, only Component A is marked incorrect

### 3. Strict Error Key Enforcement
- Uses only predefined error keys from Google Sheets rubric
- Each component gets exactly one error key
- Comments only added for errors (not for correct implementations)

### 4. Implementation Flexibility
- Students don't need to match reference solution exactly
- Grades based on logical soundness and methodology
- Focuses on correctness of approach, not exact code matching

## Output Format

Grading results are saved as YAML files in:
```
/Users/dp/Desktop/TA agent/data/teacher/practical2/grading_files/FDS25-Txxx.yaml
```

See `example-output.yaml` for the complete structure.

## Common Issues and Solutions

### Issue 1: Dataset Path Errors
**Solution:** The skill automatically fixes dataset paths before execution

### Issue 2: Long Execution Times
**Solution:** If execution exceeds 10 minutes, the skill will ask for user guidance

### Issue 3: Undefined Errors
**Solution:** If encountering errors not in the error key table, the skill will stop and ask the user

## Error Keys Reference

The skill uses 80+ error keys organized by component. See the complete list in `SKILL.md`.

Key categories:
- General Code Quality (3 keys)
- ContFeatureParam (9 keys)
- BinFeatureParam (9 keys)
- CatFeatureParam (8 keys)
- FeatureParam Tests (5 keys)
- NBC fit() (7 keys)
- NBC predict() (9 keys)
- NBC Tests (5 keys)
- compareNBCvsLR (7 keys)
- Experiments: IRIS (6 keys), Voting (7 keys), Cancer (10 keys)

## Customization

To adapt this skill for your own grading needs:

1. **Update paths** in SKILL.md:
   - Change base directories
   - Update dataset locations
   - Modify grading file output paths

2. **Modify error keys**:
   - Edit the error key tables in SKILL.md
   - Ensure YAML output format matches your keys

3. **Adjust grading criteria**:
   - Update the "IMPORTANT GRADING PHILOSOPHY" section
   - Modify component evaluation instructions

## Support

For issues or questions:
1. Check the comprehensive instructions in `SKILL.md`
2. Review the example output in `example-output.yaml`
3. Consult the original practical assignment specification

## License

This skill is for educational and grading purposes. Adapt as needed for your course.
