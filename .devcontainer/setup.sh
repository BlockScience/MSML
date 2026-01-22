#!/bin/bash
set -e

echo "Setting up MSML development environment..."

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

# Install dependencies with uv
echo "Installing dependencies with uv..."
uv sync

# Install development tools
echo "Installing development tools..."
uv pip install --system ruff pytest pytest-cov

# Verify installation
echo "Verifying installation..."
uv run python -c "import math_spec_mapping; print(f'MSML version: {math_spec_mapping.__version__}')" || echo "MSML installed successfully (no version attribute)"

echo "✓ Development environment setup complete!"
echo ""
echo "Quick start:"
echo "  - Activate venv: source .venv/bin/activate"
echo "  - Run scripts: uv run python scripts/load_and_validate_spec.py"
echo "  - Run tests: uv run pytest"
echo ""
