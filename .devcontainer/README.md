# Dev Container for MSML

This directory contains the configuration for a standardized development environment using [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers).

## What is a Dev Container?

A dev container provides a consistent, reproducible development environment using Docker containers. It ensures all contributors work in the same environment with the same tools and dependencies.

## Features

This dev container includes:

- **Python 3.11** - Base Python environment
- **uv** - Fast Python package manager
- **Git & GitHub CLI** - Version control tools
- **VS Code Extensions**:
  - Python language support (Pylance)
  - Jupyter notebook support
  - Ruff for linting and formatting
  - TOML language support
  - GitLens for enhanced Git integration
- **Automatic Setup** - Dependencies installed automatically on container creation

## Getting Started

### Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Using the Dev Container

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BlockScience/MSML.git
   cd MSML
   ```

2. **Open in VS Code:**
   ```bash
   code .
   ```

3. **Reopen in Container:**
   - Press `F1` or `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
   - Select "Dev Containers: Reopen in Container"
   - Wait for the container to build and setup to complete

4. **Start developing!**
   - The virtual environment is automatically created at `.venv/`
   - All dependencies are pre-installed
   - Extensions are ready to use

### Using GitHub Codespaces

You can also use this dev container with GitHub Codespaces:

1. Navigate to the [MSML repository](https://github.com/BlockScience/MSML)
2. Click the green "Code" button
3. Select "Codespaces" tab
4. Click "Create codespace on main" (or your branch)
5. Wait for the environment to set up

## What Happens During Setup

The `setup.sh` script runs automatically when the container is created:

1. Installs `uv` package manager
2. Runs `uv sync` to install all project dependencies
3. Installs development tools (ruff, pytest, etc.)
4. Verifies the installation

This takes a few minutes on first run but is cached for subsequent starts.

## Using the Environment

### Running Scripts

```bash
# Activate the virtual environment
source .venv/bin/activate

# Or use uv run
uv run python scripts/load_and_validate_spec.py spec.json
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=math_spec_mapping
```

### Installing Additional Packages

```bash
# Add a dependency
uv add <package-name>

# Add a dev dependency
uv add --dev <package-name>
```

## VS Code Configuration

The dev container configures VS Code with:

- **Python interpreter**: Automatically set to `.venv/bin/python`
- **Format on save**: Enabled with Ruff
- **Linting**: Automatic with Ruff
- **Import organization**: Automatic on save
- **File exclusions**: Hides `__pycache__`, `.pyc`, etc.

## Customizing the Dev Container

### Adding Extensions

Edit `.devcontainer/devcontainer.json` and add extension IDs:

```json
"customizations": {
  "vscode": {
    "extensions": [
      "existing.extension",
      "new.extension-id"
    ]
  }
}
```

### Changing Python Version

Edit the `image` field in `devcontainer.json`:

```json
"image": "mcr.microsoft.com/devcontainers/python:3.12"
```

### Adding System Packages

Create a `Dockerfile` in `.devcontainer/` for custom image builds:

```dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && apt-get install -y \
    graphviz \
    && rm -rf /var/lib/apt/lists/*
```

Then update `devcontainer.json`:

```json
"build": {
  "dockerfile": "Dockerfile"
}
```

## Troubleshooting

### Container won't start

1. Ensure Docker is running
2. Try "Dev Containers: Rebuild Container"
3. Check Docker has sufficient resources (4GB+ RAM recommended)

### Extensions not working

1. Reload the window: `F1` → "Developer: Reload Window"
2. Check extension is installed: `Ctrl+Shift+X`
3. Rebuild container if needed

### Setup script fails

1. Check the output in the Terminal
2. Try running setup manually:
   ```bash
   bash .devcontainer/setup.sh
   ```
3. Rebuild the container

## Benefits of Using Dev Containers

- **Consistency**: Same environment for all contributors
- **Quick onboarding**: New contributors ready in minutes
- **Isolated**: Doesn't affect your local system
- **Reproducible**: Same setup in CI/CD
- **Customizable**: Easy to add tools and extensions

## Resources

- [VS Code Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [Dev Container Specification](https://containers.dev/)
- [Dev Container Features](https://containers.dev/features)
- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
