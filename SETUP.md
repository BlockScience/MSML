# Development Setup

## Prerequisites

- Python 3.8 or higher
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver

## Installing uv

If you don't have uv installed, install it using one of these methods:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Using pip
pip install uv
```

## Setting Up the Development Environment

1. Clone the repository:
```bash
git clone https://github.com/BlockScience/MSML.git
cd MSML
```

2. Install dependencies using uv:
```bash
uv sync
```

This will:
- Create a virtual environment in `.venv/`
- Install all project dependencies
- Install the package in editable mode

3. Activate the virtual environment:
```bash
# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

## Running Commands in the Virtual Environment

You can run commands in the virtual environment without activating it:

```bash
# Run Python scripts
uv run python your_script.py

# Run installed command-line tools
uv run <command>
```

## Installing the Library for Users

For regular users who just want to use MSML (not develop it):

```bash
pip install math-spec-mapping
```

Or with uv:

```bash
uv pip install math-spec-mapping
```

## Adding New Dependencies

If you need to add a new dependency to the project:

```bash
# Add a dependency
uv add <package-name>

# Add a development dependency
uv add --dev <package-name>
```

Then commit the updated `pyproject.toml` and `uv.lock` files.

## Updating Dependencies

To update all dependencies to their latest compatible versions:

```bash
uv sync --upgrade
```

## CI/CD Integration

The project uses uv in CI workflows for fast, reproducible builds. See `.github/workflows/` for examples.
