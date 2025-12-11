"""
Problem Solving Package

This package contains brute force and backtracking algorithms for shelf optimization.

Modules:
    - brute_force: Find all risky combinations exceeding weight limit
    - backtracking: Find optimal combination maximizing value

Author: Miguel Bravo
Date: December 2025
"""

from .brute_force import (
    find_risky_shelf_combinations,
    display_risky_combinations,
    generate_risky_combinations_report
)

from .backtracking import (
    find_optimal_shelf_backtracking,
    find_optimal_shelf_dynamic,
    display_optimal_solution,
    generate_optimal_shelf_report,
    compare_backtracking_vs_brute_force
)

__all__ = [
    # Brute Force
    'find_risky_shelf_combinations',
    'display_risky_combinations',
    'generate_risky_combinations_report',
    # Backtracking
    'find_optimal_shelf_backtracking',
    'find_optimal_shelf_dynamic',
    'display_optimal_solution',
    'generate_optimal_shelf_report',
    'compare_backtracking_vs_brute_force',
]
