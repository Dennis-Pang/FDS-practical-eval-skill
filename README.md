# FDS Practical 1 - Notebook Grading System

## Overview

This repository contains an AI-powered grading system for Jupyter notebook assignments in machine learning courses. The system has been upgraded from a monolithic prompt-based approach to the **Anthropic Skills framework** for better maintainability, efficiency, and scalability.

## Quick Start

### First-Time Setup

The skill uses configuration files to store paths and team information. You need to set these up before grading:

#### Option 1: Interactive Setup (Recommended)
```bash
cd notebook-grading
python scripts/init_config.py
```

The wizard will ask you for:
- Student submission directory path
- Dataset directory path
- Grading output directory
- Team identifiers
- Folder naming patterns

#### Option 2: Manual Setup
1. Copy template files:
   ```bash
   cd notebook-grading/config
   cp paths.yaml.template paths.yaml
   cp teams.yaml.template teams.yaml
   cp datasets.yaml.template datasets.yaml
   ```

2. Edit each file and replace `PLACEHOLDER_*` values with your actual paths and team information.

#### Option 3: Claude-Assisted Setup
If configuration files are missing, Claude will automatically:
1. Detect missing configuration
2. Ask you for required information
3. Create configuration files with your provided values

### Verify Configuration
```bash
python scripts/validate_paths.py
```

This will check that all configured paths exist and are accessible.

### Start Grading
```
User: "Please grade Team 004 using the notebook-grading skill"

Claude will:
1. Load configuration from config/*.yaml
2. Spawn sub-agent for Team 004
3. Grade the assignment
4. Save results to configured output directory
```

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
- **Centralized resources**: Paths, teams, datasets in config files (not hardcoded)
- **Dynamic configuration**: Claude asks for missing information and writes config files
- **Modular documentation**: Task-specific reference files
- **Reusable templates**: YAML and testing templates
- **~70% reduction** in main skill file size (~150 lines)
- **Portable**: Works across different environments by adapting configuration

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

When grading assignments, Claude will:

1. **Check configuration**: Verify `config/*.yaml` files exist and are populated
2. **Ask for configuration if missing**: Prompt user for paths and team information
3. **Load configuration**: Read paths and team list from config files
4. **Spawn sub-agents**: Create isolated grading environment for each team
5. **Progressive loading**: Sub-agents load only relevant reference files as needed
6. **Follow workflow**: Fix paths → Evaluate tasks → Record results

### For Human Graders

#### Initial Setup (One-Time)
```bash
# Run interactive configuration wizard
cd notebook-grading
python scripts/init_config.py

# Or manually edit config/*.yaml files
```

#### Grading Workflow
```bash
# Verify configuration
python scripts/validate_paths.py

# Start grading (via Claude)
# "Grade Team 004 using the notebook-grading skill"
```

#### Updating Configuration
```bash
# Update team list
vim config/teams.yaml

# Update paths
vim config/paths.yaml

# Verify changes
python scripts/validate_paths.py
```

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

### Initial Configuration

**Recommended: Use the interactive wizard**
```bash
python notebook-grading/scripts/init_config.py
```

The wizard will:
1. Ask for all required paths and information
2. Validate your inputs
3. Generate properly formatted config files
4. Create necessary directories

### Updating Configuration

#### Update File Paths
Edit `notebook-grading/config/paths.yaml`:
```yaml
student_submissions:
  base_directory: "/path/to/students"
datasets:
  location: "/path/to/datasets"
grading_outputs:
  yaml_files_directory: "/path/to/grading/files"
  f1_scores_file: "/path/to/f1.txt"
```

#### Update Team List
Edit `notebook-grading/config/teams.yaml`:
```yaml
teams:
  - "004"
  - "011"
  - "018"
  # ... add more teams
folder_prefix: "FDS-25-T"
folder_pattern: "FDS-25-Txxx"
```

#### Update Error Keys
Edit `notebook-grading/references/error_keys.md` to modify grading rubrics.

#### Verify Configuration
```bash
python notebook-grading/scripts/validate_paths.py
```

### Configuration Files

| File | Purpose | When to Update |
|------|---------|----------------|
| `config/paths.yaml` | File paths for all directories | When directory structure changes |
| `config/teams.yaml` | List of teams to grade | Each semester/assignment |
| `config/datasets.yaml` | Dataset metadata | When datasets change |
| `*.yaml.template` | Templates for new setups | Never (these are templates) |

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

### Scenario 1: First-Time User

```
User: Grade Team 004 using the notebook-grading skill

Claude: I need to check the configuration first.
[Checks config/*.yaml files]

Claude: Configuration files are missing. I need some information to set up:

        1. Where are student notebook folders located?
        2. Where are the datasets located?
        3. Where should grading results be saved?
        4. What are the team identifiers?

User: [Provides the information]

Claude: Thank you! I'll create the configuration files.
[Writes config/paths.yaml, config/teams.yaml, config/datasets.yaml]

Claude: Configuration complete. Now grading Team 004...
[Spawns sub-agent and proceeds with grading]

Sub-agent:
1. Loads config/paths.yaml for file locations
2. Loads config/teams.yaml to verify Team 004
3. Finds Team 004's notebook in configured directory
4. Loads references/error_keys.md for grading rubric
5. Grades notebook following workflow
6. Saves results to configured YAML directory

Claude: ✓ Team 004 grading complete. Results saved to [configured path]/FDS-25-T004.yaml
```

### Scenario 2: Configured System

```
User: Grade Team 004

Claude: Loading configuration from config/*.yaml
[Configuration found and loaded]

Claude: Grading Team 004...
[Spawns sub-agent]

Sub-agent: [Proceeds directly with grading]

Claude: ✓ Team 004 complete.
        - Task 1: 1_task_1_ok
        - Task 2: 2_task_2_ok
        - Task 3: 3_task_3_ok
        - Task 4: 4_task_4_ok (F1: 0.8234)
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
