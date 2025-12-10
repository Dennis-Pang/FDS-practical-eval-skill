# FDS Practical 1 - Notebook Grading System

## Overview

This repository contains an AI-powered grading system for Jupyter notebook assignments in machine learning courses. The system has been upgraded from a monolithic prompt-based approach to the **Anthropic Skills framework** for better maintainability, efficiency, and scalability.

## Repository Structure

```
FDS-practical-1/
├── CLAUDE.md                    # Legacy prompt-based instructions (deprecated)
├── notebook-grading/            # New skills-based grading system
│   ├── SKILL.md                 # Main skill file with YAML frontmatter
│   ├── config/                  # Centralized configuration
│   │   ├── paths.yaml           # All file paths
│   │   ├── teams.yaml           # Team list
│   │   └── datasets.yaml        # Dataset information
│   ├── references/              # Detailed documentation (progressive disclosure)
│   │   ├── error_keys.md        # Error key reference table
│   │   ├── grading_philosophy.md
│   │   ├── task1_label_encoding.md
│   │   ├── task2_eda_pca.md
│   │   ├── task3_model_training.md
│   │   ├── task4_optional_testing.md
│   │   └── yaml_format.md
│   ├── assets/                  # Templates and utilities
│   │   ├── yaml_template.yaml
│   │   ├── task4_testing_template.md
│   │   └── grading_checklist.md
│   └── scripts/                 # Helper scripts (optional)
└── README.md                    # This file
```

## What Changed: Prompt-Based → Skills-Based

### Before (CLAUDE.md)
- **587 lines** in a single monolithic file
- All paths, teams, tasks, and instructions mixed together
- High token usage per grading session
- Difficult to maintain and update
- Hard to find specific information

### After (notebook-grading/)
- **Structured skill** following Anthropic's Skills framework
- **Progressive disclosure**: Load only what's needed
- **Centralized resources**: Paths, teams, datasets in config files
- **Modular documentation**: Task-specific reference files
- **Reusable templates**: YAML and testing templates
- **~70% reduction** in main skill file size (~150 lines)

## Key Design Principles Applied

### 1. Start with Evaluation
- Built skill based on observed agent performance gaps
- Addresses specific challenges in grading workflows
- Incrementally refined through testing

### 2. Structure for Scale
- **Config files** for easy updates (paths, teams, datasets)
- **Reference files** for detailed task specifications
- **Templates** for consistent output formatting
- Mutually exclusive contexts separated into different files

### 3. Think from Claude's Perspective
- Clear skill name and description in YAML frontmatter
- Progressive disclosure reduces cognitive load
- Sub-agent architecture for parallel processing
- Clear resource paths for autonomous navigation

### 4. Progressive Disclosure
Like a well-organized manual:
- **Table of contents**: SKILL.md (overview and quick start)
- **Specific chapters**: Task-specific reference files
- **Appendices**: Templates, checklists, configuration

## How to Use

### For Claude Code Agent

When grading assignments, Claude should:

1. **Activate the skill** by referencing `notebook-grading/SKILL.md`
2. **Spawn sub-agents** for each team (as specified in SKILL.md)
3. **Progressive loading**: Sub-agents load only relevant reference files
4. **Follow workflow**: Fix paths → Evaluate tasks → Record results

### For Human Graders

To use this system:

1. **Prepare environment**: Ensure all paths in `config/paths.yaml` are correct
2. **Update team list**: Modify `config/teams.yaml` if team numbers change
3. **Invoke Claude**: Ask Claude to grade teams using the notebook-grading skill
4. **Review results**: Check YAML files and f1.txt for grading outcomes

## Assignment Structure

This grading system evaluates 4 sequential tasks:

1. **Task 1**: Label Encoding
2. **Task 2**: Exploratory Data Analysis (EDA) and PCA
3. **Task 3**: Model Training (kNN + Logistic Regression)
4. **Task 4**: Optional Advanced Task (Test Set Evaluation)

See `notebook-grading/references/` for detailed task requirements.

## Key Features

### 🔄 Error Propagation Handling
**Errors do NOT cascade downstream.** If Task A causes Task B's output to be wrong but Task B's logic is correct, only Task A is marked incorrect.

See `notebook-grading/references/grading_philosophy.md` for details.

### 🎯 Implementation Flexibility
Student implementations don't need to match the reference solution exactly. Grading is based on logical soundness and meeting requirements.

### 🚀 Parallel Processing with Sub-Agents
Each team is graded by a separate sub-agent instance, enabling:
- Better resource management
- Parallel processing for multiple teams
- Isolated execution environments
- Efficient context management

### 📊 Structured Output
All grading results are recorded in standardized YAML format with:
- Error keys from `references/error_keys.md`
- Optional comments for clarification
- F1 scores tracked in centralized `f1.txt`

## Configuration Management

### Updating File Paths
Edit `notebook-grading/config/paths.yaml`:
```yaml
student_submissions:
  base_directory: "/path/to/students"
datasets:
  location: "/path/to/datasets"
```

### Updating Team List
Edit `notebook-grading/config/teams.yaml`:
```yaml
teams:
  - "004"
  - "011"
  # ... add more teams
```

### Updating Error Keys
Edit `notebook-grading/references/error_keys.md` to modify grading rubrics.

## Benefits of Skills-Based Architecture

### 1. **Efficiency**
- **Progressive disclosure**: Load only needed information (~70% token reduction)
- **Parallel processing**: Grade multiple teams simultaneously
- **Reusable templates**: Standardized outputs

### 2. **Maintainability**
- **Centralized configuration**: Update paths/teams in one place
- **Modular documentation**: Easy to update specific tasks
- **Clear structure**: Find information quickly

### 3. **Scalability**
- **Add new tasks**: Create new reference files
- **Add new teams**: Update `teams.yaml`
- **Reuse for other courses**: Adapt templates and error keys

### 4. **Quality**
- **Consistent grading**: Standardized workflows and templates
- **Audit trail**: Task 4 testing records
- **Error handling**: Clear constraints and stopping conditions

## Migration Guide

### From CLAUDE.md to Skills

**Old way:**
```
Read entire CLAUDE.md (587 lines) → Grade team → Repeat for each team
```

**New way:**
```
Read SKILL.md (150 lines) → Spawn sub-agent → Sub-agent loads only relevant references → Grade team → Repeat
```

### Token Usage Comparison

| Approach | Main Context | Per Team | 18 Teams |
|----------|-------------|----------|----------|
| **Old (CLAUDE.md)** | ~5000 tokens | ~5000 tokens | ~90,000 tokens |
| **New (Skills)** | ~1500 tokens | ~2000 tokens | ~37,500 tokens |
| **Savings** | ~70% | ~60% | ~58% |

*Note: Estimated based on file sizes and progressive disclosure*

## Example Usage

```
User: Grade Team 004

Claude: I'll use the notebook-grading skill to grade Team 004.
[Spawns sub-agent with team number and skill references]

Sub-agent:
1. Reads SKILL.md for overview
2. Loads config/paths.yaml for file locations
3. Loads references/error_keys.md for grading rubric
4. Loads task-specific references as needed
5. Grades notebook following workflow
6. Records results in YAML and f1.txt

Claude: Team 004 grading complete. Results saved to FDS25-T004.yaml
```

## Design Inspirations

This upgrade follows the **Anthropic Skills framework**:
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Equipping Agents for the Real World](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Agent Skills Announcement](https://claude.com/blog/skills)

## Future Enhancements

Potential improvements:
- [ ] Add scripts for automated path validation
- [ ] Create visualization tools for grading statistics
- [ ] Develop interactive grading dashboard
- [ ] Add support for multiple assignment types
- [ ] Create testing suite for skill validation

## Version History

### v1.0 (Current)
- Upgraded from monolithic CLAUDE.md to skills-based architecture
- Implemented progressive disclosure pattern
- Centralized configuration management
- Created modular reference documentation
- Added reusable templates and checklists

### v0.x (Legacy)
- Single CLAUDE.md file with all instructions
- Manual path management
- No progressive disclosure

## License

[Add your license here]

## Contact

For questions or issues, please contact [your contact information].
