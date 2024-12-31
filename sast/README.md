# Static Application Security Testing (SAST)

## Overview

Static Application Security Testing analyzes source code for potential security vulnerabilities without executing the application. This directory demonstrates SAST implementation using various tools.

## Tools Demonstrated

- Semgrep
- Bandit (Python)
- ESLint Security (JavaScript)

## Directory Structure

```
sast/
├── configs/                 # Tool configurations
├── examples/               # Vulnerable code examples
└── rules/                  # Custom security rules
```

## Common Vulnerabilities Detected

- SQL Injection
- Cross-site Scripting (XSS)
- Command Injection
- Hardcoded Credentials
- Insecure Direct Object References
- Buffer Overflows
- Path Traversal

## Quick Start

1. Install required tools:
   ```bash
   pip install bandit semgrep
   ```
2. Run SAST checks:

   ```bash
   # Using Bandit
   bandit -r ../sast -f json -o results.json

   # Using Semgrep
   semgrep --config=p/security-audit
   ```
