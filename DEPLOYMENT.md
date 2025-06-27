# Python Package Deployment Guide

This guide explains how to deploy the `rr-webapi` Python package to PyPI and push the code to GitHub using GitLab CI/CD.

## Overview

The deployment process is automated via GitLab CI/CD and follows the same pattern as the Node.js library:

1. **Build and Test**: Runs on every commit to `main` and on tags
2. **Deploy to GitHub**: Pushes the library code to GitHub repository 
3. **Publish to PyPI**: Publishes the package to PyPI for public installation

## Prerequisites

### 1. PyPI Account and Trusted Publisher

1. Create an account at [pypi.org](https://pypi.org)
2. Set up **Trusted Publishing** (recommended modern approach):
   - Go to **Account Settings** → **Publishing** → **Add a new pending publisher**
   - Select **GitLab** as the publisher
   - Fill in the project details (see configuration section below)

**Benefits of Trusted Publishing:**
- ✅ **No API tokens to manage** - more secure
- ✅ **Works with private GitLab projects**
- ✅ **Automatic token generation** using OIDC
- ✅ **No token expiration worries**

### 2. GitHub Repository

1. The GitHub repository should be created at: `https://github.com/SPTiming/python-rr-webapi`
2. Generate an SSH key for GitLab CI/CD to push to GitHub

### 3. GitLab CI/CD Variables

Set the following environment variables in your GitLab project settings:

#### Required Variables:
- `GITHUB_SSH_KEY`: Base64-encoded SSH private key for GitHub access (masked, protected)

**Note**: With Trusted Publishing, you don't need to store PyPI tokens!

#### Setting up GitHub SSH Key:
```bash
# Generate SSH key pair
ssh-keygen -t ed25519 -C "gitlab-ci@sptiming.ch" -f gitlab_ci_key

# Add public key to GitHub repo (Settings → Deploy keys)
cat gitlab_ci_key.pub

# Encode private key for GitLab variable
base64 -i gitlab_ci_key | pbcopy  # macOS
base64 -w 0 gitlab_ci_key         # Linux
```

## PyPI Trusted Publisher Configuration

Fill out the PyPI pending publisher form with these values:

- **PyPI Project Name**: `rr-webapi`
- **Namespace**: Your GitLab username or group (e.g., `sptiming`)
- **Project name**: Your GitLab project name (e.g., `go-webapi` or `rr-webapi`)
- **Top-level pipeline file path**: `.gitlab-ci.yml`
- **Environment name**: `release`

### How to find your GitLab project details:

1. **Namespace**: Look at your GitLab project URL: `https://gitlab.com/[NAMESPACE]/[PROJECT]`
   - For `https://gitlab.com/sptiming/go-webapi` → namespace is `sptiming`

2. **Project name**: The name of your GitLab project
   - For `https://gitlab.com/sptiming/go-webapi` → project name is `go-webapi`

**Important**: Your GitLab project can remain **private** - Trusted Publishing works with private repositories!

## Package Configuration

The package is configured using modern Python packaging standards:

- **pyproject.toml**: Main configuration file (PEP 621)
- **setup.py**: Legacy wrapper (for compatibility)
- **MANIFEST.in**: Controls which files are included in the package
- **requirements.txt**: Runtime dependencies

### Key Files:
- Package name: `rr-webapi` (PyPI) / `rr_webapi` (import)
- License: GPL-3.0-or-later
- Python support: 3.7+
- Dependencies: requests, python-dateutil, python-dotenv

## Deployment Process

### Automatic Deployment (Recommended)

1. **Commit your changes** to the `main` branch
2. **Create and push a tag** to trigger deployment:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

3. **GitLab CI/CD will automatically**:
   - Build and test the package
   - Push code to GitHub repository
   - Publish to PyPI

### Manual Testing

You can test the package locally:

```bash
cd lib/python

# Test imports and basic functionality
python test_setup.py

# Build the package
pip install build
python -m build

# Check the built package
ls dist/
```

## GitLab CI/CD Jobs

The following jobs are configured:

### `build_and_test_python`
- Runs on every commit to `main` and on tags
- Installs dependencies and builds the package
- Performs basic import tests
- Stores build artifacts

### `deploy_python_to_github`
- Runs only on tags
- Clones/creates the GitHub repository
- Copies all library files
- Updates version in pyproject.toml
- Commits and pushes to GitHub
- Creates GitHub release tags

### `publish_to_pypi`
- Runs only on tags
- Uses pre-built artifacts from build stage
- Updates version to match Git tag
- Publishes to PyPI using twine

## Post-Deployment

After successful deployment:

1. **Verify PyPI publication**: Check [pypi.org/project/rr-webapi](https://pypi.org/project/rr-webapi)
2. **Verify GitHub repository**: Check [github.com/SPTiming/python-rr-webapi](https://github.com/SPTiming/python-rr-webapi)
3. **Test installation**:
   ```bash
   pip install rr-webapi
   python -c "from rr_webapi import API; print('Success!')"
   ```

## Version Management

- Package version is automatically updated from Git tags
- Use semantic versioning: `v1.0.0`, `v1.0.1`, `v1.1.0`, etc.
- Each tag creates a new release on both PyPI and GitHub

## Troubleshooting

### Common Issues:

1. **PyPI publication fails**: Check if version already exists
2. **GitHub push fails**: Verify SSH key is correctly configured
3. **Build fails**: Check Python syntax and import issues

### Debugging:

1. Check GitLab CI/CD pipeline logs
2. Test package build locally
3. Verify environment variables are set correctly

## Directory Structure

```
lib/python/
├── rr_webapi/           # Main package
│   ├── __init__.py
│   ├── api.py
│   ├── public.py
│   ├── eventapi.py
│   └── endpoints/
├── tests/               # Test files
├── pyproject.toml       # Modern package config
├── setup.py            # Legacy setup file
├── MANIFEST.in         # Package manifest
├── requirements.txt    # Dependencies
├── README.md           # Package documentation
├── LICENSE             # GPL-3.0 license
└── .gitignore          # Git ignore rules
```

## Support

For issues:
- Check GitLab CI/CD pipeline logs
- Review this documentation
- Contact the development team 