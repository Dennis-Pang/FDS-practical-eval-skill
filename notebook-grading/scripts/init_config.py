#!/usr/bin/env python3
"""
Interactive Configuration Setup for Notebook Grading Skill

This script helps you set up the configuration files needed for the grading system.
It will ask you a series of questions and generate the config files automatically.

Usage:
    python init_config.py [--interactive]

Options:
    --interactive    Use interactive mode (default)
    --from-file     Load configuration from a JSON file
"""

import yaml
import json
import sys
from pathlib import Path
from typing import Dict, List


class ConfigurationWizard:
    """Interactive configuration setup wizard."""

    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.config_dir = self.script_dir.parent / 'config'
        self.config = {}

    def welcome(self):
        """Display welcome message."""
        print("=" * 70)
        print("Notebook Grading System - Configuration Wizard")
        print("=" * 70)
        print()
        print("This wizard will help you set up the configuration files needed")
        print("for the grading system. You'll be asked for file paths and team")
        print("information.")
        print()
        print("You can press Ctrl+C at any time to cancel.")
        print()

    def ask_question(self, question: str, default: str = None, required: bool = True) -> str:
        """Ask user a question and return the answer."""
        if default:
            prompt = f"{question} [{default}]: "
        else:
            prompt = f"{question}: "

        while True:
            answer = input(prompt).strip()

            if not answer and default:
                return default
            elif not answer and not required:
                return ""
            elif not answer and required:
                print("  ⚠ This field is required. Please provide a value.")
                continue
            else:
                return answer

    def ask_yes_no(self, question: str, default: bool = True) -> bool:
        """Ask a yes/no question."""
        default_str = "Y/n" if default else "y/N"
        prompt = f"{question} [{default_str}]: "

        while True:
            answer = input(prompt).strip().lower()

            if not answer:
                return default
            elif answer in ['y', 'yes']:
                return True
            elif answer in ['n', 'no']:
                return False
            else:
                print("  ⚠ Please answer 'y' or 'n'")

    def ask_list(self, question: str, example: str) -> List[str]:
        """Ask for a comma-separated list."""
        print(f"\n{question}")
        print(f"  Example: {example}")
        print("  Enter items separated by commas:")

        while True:
            answer = input("  > ").strip()
            if not answer:
                print("  ⚠ Please provide at least one item.")
                continue

            items = [item.strip() for item in answer.split(',')]
            items = [item for item in items if item]  # Remove empty strings

            print(f"\n  You entered {len(items)} item(s): {', '.join(items)}")
            if self.ask_yes_no("  Is this correct?"):
                return items

    def configure_paths(self):
        """Configure file paths."""
        print("\n" + "=" * 70)
        print("Step 1: File Paths Configuration")
        print("=" * 70)

        print("\n1. Student Submissions Directory")
        print("   Where are the student notebook folders located?")
        student_base = self.ask_question("   Path")

        print("\n2. Team Folder Naming Pattern")
        print("   How are team folders named?")
        folder_pattern = self.ask_question(
            "   Pattern (use 'xxx' as placeholder for team number)",
            default="FDS-25-Txxx"
        )

        print("\n3. Dataset Directory")
        print("   Where are the training datasets located?")
        dataset_location = self.ask_question("   Path")

        print("\n4. Test Dataset (Optional)")
        print("   Where is the test dataset (df_test.pkl)?")
        test_dataset = self.ask_question(
            "   Path",
            required=False
        )
        if not test_dataset:
            test_dataset = f"{dataset_location}/df_test.pkl"

        print("\n5. Grading Output Directory")
        print("   Where should YAML grading files be saved?")
        grading_output = self.ask_question(
            "   Path",
            default=f"{dataset_location}/grading_files"
        )

        print("\n6. YAML File Naming Pattern")
        yaml_pattern = self.ask_question(
            "   Pattern (use 'xxx' as placeholder for team number)",
            default="FDS-25-Txxx.yaml"
        )

        print("\n7. F1 Scores File")
        print("   Where should F1 scores be recorded?")
        f1_file = self.ask_question(
            "   Path",
            default=f"{dataset_location}/f1.txt"
        )

        print("\n8. Reference Solution (Optional)")
        print("   Where is the reference solution notebook?")
        ref_solution = self.ask_question(
            "   Path",
            required=False
        )
        if not ref_solution:
            ref_solution = f"{dataset_location}/reference_solution.ipynb"

        # Store paths configuration
        self.config['paths'] = {
            'reference_solution': {
                'path': ref_solution,
                'description': "Correct reference implementation for grader's understanding"
            },
            'student_submissions': {
                'base_directory': student_base,
                'folder_pattern': folder_pattern,
                'description': "Student submission folders, each may contain 1-2 .ipynb files"
            },
            'datasets': {
                'location': dataset_location,
                'test_dataset': test_dataset,
                'description': "All required datasets for training and testing"
            },
            'grading_outputs': {
                'yaml_files_directory': grading_output,
                'yaml_filename_pattern': yaml_pattern,
                'f1_scores_file': f1_file,
                'description': "Grading results and F1 score records"
            },
            'path_replacements': {
                'target_directory': dataset_location,
                'common_patterns': [
                    "../data/",
                    "./data/",
                    "data/",
                    "/home/student/"
                ],
                'note': "Replace all dataset loading paths with absolute paths to ensure notebooks execute correctly"
            },
            'configured': True
        }

    def configure_teams(self):
        """Configure team information."""
        print("\n" + "=" * 70)
        print("Step 2: Team Configuration")
        print("=" * 70)

        print("\nTeam Identifiers")
        teams = self.ask_list(
            "What are the team numbers/identifiers to grade?",
            "004, 011, 018, 025"
        )

        folder_pattern = self.config['paths']['student_submissions']['folder_pattern']
        folder_prefix = folder_pattern.replace('xxx', '')

        # Store teams configuration
        self.config['teams'] = {
            'teams': teams,
            'folder_prefix': folder_prefix,
            'folder_pattern': folder_pattern,
            'submission_notes': [
                "Each team folder may contain 1-2 .ipynb files",
                "Submission formats vary between teams",
                "Some teams split their work across 2 notebooks",
                "All notebooks should contain similar task content",
                "Grade ONLY .ipynb files"
            ],
            'configured': True
        }

    def configure_datasets(self):
        """Configure dataset information."""
        print("\n" + "=" * 70)
        print("Step 3: Dataset Configuration")
        print("=" * 70)

        dataset_location = self.config['paths']['datasets']['location']
        test_dataset = self.config['paths']['datasets']['test_dataset']

        # Store datasets configuration
        self.config['datasets'] = {
            'datasets': {
                'training': {
                    'location': dataset_location,
                    'description': "Training datasets used by students in their notebooks",
                    'note': "Students load these datasets with various relative paths that need to be fixed"
                },
                'testing': {
                    'file_path': test_dataset,
                    'format': 'pickle',
                    'description': "Test dataset for evaluating Task 4 (Optional Advanced Task)",
                    'usage': "Students did NOT use this during training - graders must load and apply student's pipeline",
                    'load_command': f"pd.read_pickle('{test_dataset}')"
                }
            },
            'path_fixing': {
                'required': True,
                'priority': "CRITICAL - must be done BEFORE executing any student code",
                'steps': [
                    "Search for dataset loading statements in student notebooks",
                    "Replace their paths with absolute paths to dataset location",
                    "Match dataset filenames exactly (case-sensitive)",
                    "DO NOT modify any other code"
                ]
            },
            'configured': True
        }

    def preview_configuration(self):
        """Show configuration preview."""
        print("\n" + "=" * 70)
        print("Configuration Preview")
        print("=" * 70)

        print("\nPaths:")
        print(f"  Student submissions: {self.config['paths']['student_submissions']['base_directory']}")
        print(f"  Folder pattern: {self.config['paths']['student_submissions']['folder_pattern']}")
        print(f"  Datasets: {self.config['paths']['datasets']['location']}")
        print(f"  Test dataset: {self.config['paths']['datasets']['test_dataset']}")
        print(f"  Grading output: {self.config['paths']['grading_outputs']['yaml_files_directory']}")
        print(f"  F1 scores: {self.config['paths']['grading_outputs']['f1_scores_file']}")

        print("\nTeams:")
        print(f"  Count: {len(self.config['teams']['teams'])}")
        print(f"  Identifiers: {', '.join(self.config['teams']['teams'])}")

        print()

    def write_config_files(self):
        """Write configuration to YAML files."""
        print("\nWriting configuration files...")

        # Write paths.yaml
        paths_file = self.config_dir / 'paths.yaml'
        with open(paths_file, 'w') as f:
            yaml.dump(self.config['paths'], f, default_flow_style=False, sort_keys=False)
        print(f"  ✓ {paths_file}")

        # Write teams.yaml
        teams_file = self.config_dir / 'teams.yaml'
        with open(teams_file, 'w') as f:
            yaml.dump(self.config['teams'], f, default_flow_style=False, sort_keys=False)
        print(f"  ✓ {teams_file}")

        # Write datasets.yaml
        datasets_file = self.config_dir / 'datasets.yaml'
        with open(datasets_file, 'w') as f:
            yaml.dump(self.config['datasets'], f, default_flow_style=False, sort_keys=False)
        print(f"  ✓ {datasets_file}")

        print("\n✓ Configuration complete!")
        print(f"\nConfiguration files have been created in: {self.config_dir}")
        print("\nYou can now use the notebook-grading skill to grade assignments.")

    def run(self):
        """Run the configuration wizard."""
        try:
            self.welcome()
            self.configure_paths()
            self.configure_teams()
            self.configure_datasets()
            self.preview_configuration()

            if self.ask_yes_no("\nSave this configuration?"):
                self.write_config_files()
            else:
                print("\nConfiguration cancelled.")
                sys.exit(0)

        except KeyboardInterrupt:
            print("\n\nConfiguration cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"\n\n✗ Error: {e}")
            sys.exit(1)


def main():
    """Main entry point."""
    wizard = ConfigurationWizard()
    wizard.run()


if __name__ == '__main__':
    main()
