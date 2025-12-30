#!/usr/bin/env python3
"""
Security validation script for web applications.

Usage:
    python validate.py src/

Checks for common security anti-patterns.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

# ANSI colors
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Patterns to check (pattern, severity, message)
DANGEROUS_PATTERNS: List[Tuple[str, str, str]] = [
    # Auth bypass risks
    (
        r'user_metadata\.(isPaid|isAdmin|hasPaid|has_paid|role)',
        'CRITICAL',
        'Never trust user_metadata for authorization - check database instead'
    ),
    (
        r'user_metadata\[[\'"](isPaid|isAdmin|hasPaid|has_paid|role)',
        'CRITICAL',
        'Never trust user_metadata for authorization - check database instead'
    ),

    # Exposed secrets
    (
        r'NEXT_PUBLIC_.*SECRET',
        'CRITICAL',
        'Secrets must not be exposed via NEXT_PUBLIC_ variables'
    ),
    (
        r'NEXT_PUBLIC_.*KEY(?!_PUBLISHABLE)',
        'WARNING',
        'Verify this key is safe to expose publicly'
    ),
    (
        r'sk_live_[a-zA-Z0-9]+',
        'CRITICAL',
        'Live Stripe secret key found in code - use environment variable'
    ),
    (
        r'sk_test_[a-zA-Z0-9]+',
        'WARNING',
        'Test Stripe secret key found in code - use environment variable'
    ),

    # Client-side database operations on sensitive tables
    (
        r'\.from\([\'"]orders[\'"]\)\.insert',
        'WARNING',
        'Client-side order creation detected - should use webhook only'
    ),
    (
        r'\.from\([\'"]payments[\'"]\)\.insert',
        'WARNING',
        'Client-side payment creation detected - should use webhook only'
    ),
    (
        r'\.from\([\'"]subscriptions[\'"]\)\.insert',
        'WARNING',
        'Client-side subscription creation detected - should use webhook only'
    ),

    # Missing auth patterns (in API routes)
    (
        r'export async function (GET|POST|PUT|DELETE|PATCH).*\n(?!.*getUser)',
        'INFO',
        'API route may be missing authentication check'
    ),

    # Webhook without signature verification
    (
        r'api/webhook.*route\.ts.*(?!constructEvent)',
        'WARNING',
        'Webhook handler may be missing signature verification'
    ),
]

# File extensions to check
EXTENSIONS = {'.ts', '.tsx', '.js', '.jsx'}


def find_issues(file_path: Path) -> List[Tuple[int, str, str, str]]:
    """Find security issues in a file."""
    issues = []

    try:
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')

        for pattern, severity, message in DANGEROUS_PATTERNS:
            for match in re.finditer(pattern, content, re.MULTILINE | re.IGNORECASE):
                # Find line number
                line_num = content[:match.start()].count('\n') + 1
                line_content = lines[line_num - 1].strip()
                issues.append((line_num, severity, message, line_content))

    except Exception as e:
        print(f"{YELLOW}Warning: Could not read {file_path}: {e}{RESET}")

    return issues


def scan_directory(directory: str) -> dict:
    """Scan directory for security issues."""
    results = {
        'critical': [],
        'warning': [],
        'info': [],
        'files_scanned': 0
    }

    path = Path(directory)

    if not path.exists():
        print(f"{RED}Error: Directory {directory} does not exist{RESET}")
        sys.exit(1)

    for file_path in path.rglob('*'):
        if file_path.suffix not in EXTENSIONS:
            continue

        # Skip node_modules and .next
        if 'node_modules' in str(file_path) or '.next' in str(file_path):
            continue

        results['files_scanned'] += 1
        issues = find_issues(file_path)

        for line_num, severity, message, line_content in issues:
            issue = {
                'file': str(file_path),
                'line': line_num,
                'message': message,
                'code': line_content[:80] + '...' if len(line_content) > 80 else line_content
            }

            if severity == 'CRITICAL':
                results['critical'].append(issue)
            elif severity == 'WARNING':
                results['warning'].append(issue)
            else:
                results['info'].append(issue)

    return results


def print_results(results: dict) -> int:
    """Print results and return exit code."""
    print(f"\n{'='*60}")
    print(f"Security Scan Results")
    print(f"{'='*60}")
    print(f"Files scanned: {results['files_scanned']}")
    print()

    exit_code = 0

    if results['critical']:
        print(f"{RED}CRITICAL ISSUES ({len(results['critical'])}):{RESET}")
        for issue in results['critical']:
            print(f"  {issue['file']}:{issue['line']}")
            print(f"    {RED}{issue['message']}{RESET}")
            print(f"    Code: {issue['code']}")
            print()
        exit_code = 1

    if results['warning']:
        print(f"{YELLOW}WARNINGS ({len(results['warning'])}):{RESET}")
        for issue in results['warning']:
            print(f"  {issue['file']}:{issue['line']}")
            print(f"    {YELLOW}{issue['message']}{RESET}")
            print(f"    Code: {issue['code']}")
            print()

    if results['info']:
        print(f"INFO ({len(results['info'])}):")
        for issue in results['info']:
            print(f"  {issue['file']}:{issue['line']}")
            print(f"    {issue['message']}")
            print()

    if not results['critical'] and not results['warning']:
        print(f"{GREEN}No security issues found!{RESET}")

    print(f"{'='*60}")

    return exit_code


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate.py <directory>")
        print("Example: python validate.py src/")
        sys.exit(1)

    directory = sys.argv[1]
    results = scan_directory(directory)
    exit_code = print_results(results)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
