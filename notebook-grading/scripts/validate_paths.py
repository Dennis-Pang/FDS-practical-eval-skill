#!/usr/bin/env python3
"""
Path Validation Script

This script validates that all paths specified in config/paths.yaml exist
and are accessible. Run this before starting grading to catch configuration errors.

Usage:
    python validate_paths.py
"""

import yaml
from pathlib import Path
import sys


def load_config(config_path):
    """Load YAML configuration file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def validate_paths(paths_config):
    """Validate all paths in the configuration."""
    errors = []
    warnings = []

    # Validate reference solution
    ref_path = Path(paths_config['reference_solution']['path'])
    if not ref_path.exists():
        errors.append(f"Reference solution not found: {ref_path}")
    else:
        print(f"✓ Reference solution found: {ref_path}")

    # Validate student submissions directory
    student_base = Path(paths_config['student_submissions']['base_directory'])
    if not student_base.exists():
        errors.append(f"Student submissions directory not found: {student_base}")
    else:
        print(f"✓ Student submissions directory found: {student_base}")

    # Validate datasets location
    dataset_location = Path(paths_config['datasets']['location'])
    if not dataset_location.exists():
        errors.append(f"Dataset location not found: {dataset_location}")
    else:
        print(f"✓ Dataset location found: {dataset_location}")

    # Validate test dataset
    test_dataset = Path(paths_config['datasets']['test_dataset'])
    if not test_dataset.exists():
        warnings.append(f"Test dataset not found: {test_dataset}")
    else:
        print(f"✓ Test dataset found: {test_dataset}")

    # Validate grading outputs directory
    grading_dir = Path(paths_config['grading_outputs']['yaml_files_directory'])
    if not grading_dir.exists():
        warnings.append(f"Grading output directory not found (will be created): {grading_dir}")
        grading_dir.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created grading output directory: {grading_dir}")
    else:
        print(f"✓ Grading output directory found: {grading_dir}")

    # Validate F1 scores file
    f1_file = Path(paths_config['grading_outputs']['f1_scores_file'])
    if not f1_file.exists():
        warnings.append(f"F1 scores file not found (will be created): {f1_file}")
        f1_file.touch()
        print(f"✓ Created F1 scores file: {f1_file}")
    else:
        print(f"✓ F1 scores file found: {f1_file}")

    return errors, warnings


def validate_teams(teams_config, student_base_path):
    """Validate that all team folders exist."""
    errors = []
    warnings = []

    folder_prefix = teams_config['folder_prefix']
    teams = teams_config['teams']

    student_base = Path(student_base_path)

    for team_number in teams:
        team_folder = student_base / f"{folder_prefix}{team_number}"
        if not team_folder.exists():
            warnings.append(f"Team folder not found: {team_folder}")
        else:
            # Check for .ipynb files
            ipynb_files = list(team_folder.glob("*.ipynb"))
            if not ipynb_files:
                warnings.append(f"No .ipynb files found in: {team_folder}")
            else:
                print(f"✓ Team {team_number} folder found with {len(ipynb_files)} notebook(s)")

    return errors, warnings


def main():
    """Main validation routine."""
    script_dir = Path(__file__).parent
    config_dir = script_dir.parent / 'config'

    print("=" * 60)
    print("Notebook Grading System - Path Validation")
    print("=" * 60)
    print()

    # Load configurations
    try:
        paths_config = load_config(config_dir / 'paths.yaml')
        teams_config = load_config(config_dir / 'teams.yaml')
    except Exception as e:
        print(f"✗ Error loading configuration: {e}")
        sys.exit(1)

    print("Validating paths...")
    print()

    # Validate paths
    path_errors, path_warnings = validate_paths(paths_config)

    print()
    print("Validating team folders...")
    print()

    # Validate teams
    team_errors, team_warnings = validate_teams(
        teams_config,
        paths_config['student_submissions']['base_directory']
    )

    # Combine results
    all_errors = path_errors + team_errors
    all_warnings = path_warnings + team_warnings

    print()
    print("=" * 60)
    print("Validation Summary")
    print("=" * 60)

    if all_errors:
        print(f"\n✗ ERRORS ({len(all_errors)}):")
        for error in all_errors:
            print(f"  - {error}")

    if all_warnings:
        print(f"\n⚠ WARNINGS ({len(all_warnings)}):")
        for warning in all_warnings:
            print(f"  - {warning}")

    if not all_errors and not all_warnings:
        print("\n✓ All validations passed!")
    elif not all_errors:
        print("\n✓ No critical errors found. Review warnings above.")
    else:
        print("\n✗ Critical errors found. Please fix before grading.")
        sys.exit(1)


if __name__ == '__main__':
    main()
