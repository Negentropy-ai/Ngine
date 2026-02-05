#!/usr/bin/env python3
"""Automated rebranding script for Negentropy transformation."""

import re
import os
from pathlib import Path

# Refactoring patterns
PATTERNS = [
    # Package names
    (r'\blw_benchhub\b', 'ngine'),
    (r'\blw_benchhub_tasks\b', 'ngine.benchmarks'),
    (r'\blw_benchhub_rl\b', 'ngine.rl'),
    
    # Class names
    (r'\bLwTaskBase\b', 'TaskBase'),
    (r'\bLwEmbodimentBase\b', 'RobotBase'),
    (r'\bLwEnvBuilder\b', 'EnvBuilder'),
    (r'\bLwRL\b', 'RLConfig'),
    (r'\bLwScene\b', 'Scene'),
    
    # Task names
    (r'\blightwheel_libero_tasks\b', 'libero_tasks'),
    (r'\blightwheel_robocasa_tasks\b', 'robocasa_tasks'),
    
    # Import statements
    (r'from lightwheel_sdk\.loader import', 'from ngine.assets.registry import'),
    (r'# import lightwheel_sdk  # Optional', '# # import lightwheel_sdk  # Optional  # Optional'),
]

def refactor_file(file_path: Path, dry_run: bool = True) -> list:
    """Refactor a single Python file."""
    changes = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return changes
    
    original_content = content
    
    for pattern, replacement in PATTERNS:
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            changes.append(f"Pattern '{pattern}' -> '{replacement}'")
            content = new_content
    
    if not dry_run and changes:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return changes

def main():
    """Execute refactoring across the codebase."""
    root = Path("/home/user/startups/ngine")
    dry_run = os.environ.get("DRY_RUN", "true").lower() == "true"
    
    print(f"{'DRY RUN' if dry_run else 'LIVE RUN'} - Refactoring Negentropy transformation")
    print(f"Root directory: {root}\n")
    
    total_files = 0
    total_changes = 0
    
    for file_path in root.rglob("*.py"):
        changes = refactor_file(file_path, dry_run=dry_run)
        if changes:
            total_files += 1
            total_changes += len(changes)
            print(f"✓ {file_path.relative_to(root)}: {len(changes)} changes")
    
    print(f"\n{'='*60}")
    print(f"Total files modified: {total_files}")
    print(f"Total replacements: {total_changes}")
    
    if dry_run:
        print("\nTo apply changes, run:")
        print("  DRY_RUN=false python scripts/refactor_ngine.py")

if __name__ == "__main__":
    main()
