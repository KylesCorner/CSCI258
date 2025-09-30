#!/usr/bin/env bash

# Bash script to create a Django project in the current directory.

# Exit on error
set -e

# Check if project name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <project_name>"
  exit 1
fi

PROJECT_NAME=$1

# Check if python3 and pip are available
if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 is not installed."
  exit 1
fi

if ! command -v pip3 >/dev/null 2>&1; then
  echo "Error: pip3 is not installed."
  exit 1
fi

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install Django
pip install --upgrade pip
pip install django black

# Start Django project
django-admin startproject "$PROJECT_NAME" .
python3 manage.py migrate

echo "✅ Django project '$PROJECT_NAME' created in $(pwd)"
echo "Run: source venv/bin/activate && python manage.py runserver"
```
# /bin/bash

