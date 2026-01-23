# MSML Scripts

This directory contains script-based entry points for common MSML workflows. These scripts are designed to be used in automated pipelines, CI/CD, and as alternatives to notebook-based exploration.

## Available Scripts

### `load_and_validate_spec.py`

Load and validate MSML specification files. Useful for CI validation or pre-processing checks.

**Usage:**
```bash
# Validate a single specification
uv run python scripts/load_and_validate_spec.py spec.json

# Validate multiple specifications
uv run python scripts/load_and_validate_spec.py spec1.json spec2.json

# Verbose output
uv run python scripts/load_and_validate_spec.py --verbose spec.json
```

**Use cases:**
- CI/CD validation of specifications before deployment
- Batch validation of multiple specs
- Pre-commit hooks to ensure spec validity

### `generate_reports.py`

Generate documentation reports from MSML specifications.

**Usage:**
```bash
# Generate all reports
uv run python scripts/generate_reports.py spec.json

# Generate to specific directory
uv run python scripts/generate_reports.py spec.json --output ./docs

# Generate only Markdown reports
uv run python scripts/generate_reports.py spec.json --format markdown

# Verbose output
uv run python scripts/generate_reports.py --verbose spec.json
```

**Use cases:**
- Automated documentation generation in CI
- Report generation for a single spec in automated workflows
- Integration with documentation sites

## Scripts vs Notebooks

### When to use scripts:

- **Reproducible workflows**: Scripts provide deterministic, versioned workflows
- **CI/CD integration**: Easy to integrate into automated pipelines
- **Batch processing**: Process multiple specifications automatically
- **Testing**: Scripts are easier to test than notebooks
- **Command-line usage**: Quick operations without starting Jupyter

### When to use notebooks:

- **Exploration**: Interactive exploration of specifications
- **Visualization**: Rich visualization of results
- **Prototyping**: Rapid prototyping of new workflows
- **Documentation**: Narrative documentation with code and outputs
- **Teaching**: Step-by-step tutorials

## Recommended Project Structure

```
my-msml-project/
├── specs/                  # MSML JSON specifications
│   ├── main.json
│   └── variants/
├── scripts/                # Executable Python scripts
│   ├── validate.py
│   ├── generate_docs.py
│   └── run_simulation.py
├── notebooks/              # Jupyter notebooks for exploration
│   ├── exploration.ipynb
│   └── analysis.ipynb
├── reports/                # Generated documentation
└── src/                    # Reusable modules
    └── my_project/
```

## Creating New Scripts

When creating new scripts:

1. **Start with a clear purpose**: One script, one well-defined task
2. **Use argparse**: Provide clear command-line interface
3. **Handle errors gracefully**: Return appropriate exit codes
4. **Add docstrings**: Document what the script does and how to use it
5. **Make it executable**: Add shebang line and set execute permissions
6. **Import from modules**: Extract reusable logic into modules

### Example template:

```python
#!/usr/bin/env python3
"""Brief description of what this script does.

Detailed description and usage examples.
"""

import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Your script description")
    parser.add_argument('input', type=Path, help='Input file')
    parser.add_argument('--option', help='Optional parameter')
    args = parser.parse_args()
    
    try:
        # Your script logic here
        print("✓ Success")
        sys.exit(0)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```

## Integration with Existing Notebooks

Many existing workflows are in notebooks. To convert a notebook workflow to a script:

1. **Extract the core logic** into functions
2. **Move functions** to a module in `src/`
3. **Create a script** that imports and calls these functions
4. **Update the notebook** to import from the module
5. **Keep the notebook** for exploration and visualization

This approach:
- Makes logic reusable across scripts and notebooks
- Keeps notebooks cleaner and focused on exploration
- Enables testing of core logic
- Supports both interactive and automated workflows

## Contributing

When adding new scripts:

1. Follow the template and conventions above
2. Add comprehensive docstrings and help text
3. Include usage examples in the script and this README
4. Test on multiple platforms if possible
5. Update this README with the new script
