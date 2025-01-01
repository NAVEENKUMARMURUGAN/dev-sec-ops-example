# Static Application Security Testing (SAST)

## Overview

Static Application Security Testing analyzes source code for potential security vulnerabilities without executing the application. This repository implements SAST using Bandit and Semgrep.

## Tools Configuration

### Bandit

Located in `configs/bandit.yaml`:

- Excludes test directories and cache files
- Skips certain warnings (B101, B404)
- Configured with medium and high severity profiles
- Detects issues like:
  - Flask debug mode
  - Unsafe pickle usage
  - YAML loading vulnerabilities
  - Shell/SQL injection risks

### Semgrep

Located in `configs/semgrep.yaml`:

- Custom rules for:
  - SQL injection detection
  - Hardcoded secrets
  - Command injection vulnerabilities
- Supports multiple languages (Python, Java, JavaScript)

## Example Vulnerabilities

The `vulnerable_examples/` directory contains sample code demonstrating:

- Weak cryptography usage
- SQL injection risks
- Cross-site scripting (XSS)
- Hardcoded secrets
- Unsafe deserialization

## CI/CD Integration

SAST is integrated into the CI/CD pipeline via GitHub Actions:

- Runs on push/PR to main branch
- Executes both Bandit and Semgrep scans
- Reports results to GitHub Security dashboard
- Fails pipeline on high-severity findings

## Quick Start

1. Local setup:

   ```bash
   pip install bandit
   pip install semgrep
   ```

2. Run scans:

   ```bash
   # Bandit scan
   bandit -r . -c ./sast/configs/bandit.yaml

   # Semgrep scan
   semgrep --config ./sast/configs/semgrep.yaml
   ```
