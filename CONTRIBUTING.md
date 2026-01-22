# Contributing to MSML

Thank you for your interest in contributing to the Mathematical Specification Mapping Library (MSML)! This guide will help you get started.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Project Structure](#project-structure)
- [Coding Guidelines](#coding-guidelines)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful and considerate in your interactions with other contributors.

## Getting Started

### Environment Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/MSML.git
   cd MSML
   ```

2. **Install uv** (if not already installed):
   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Set up the development environment:**
   ```bash
   uv sync
   ```

   This creates a virtual environment in `.venv/` and installs all dependencies.

4. **Activate the virtual environment:**
   ```bash
   # On macOS/Linux
   source .venv/bin/activate

   # On Windows
   .venv\Scripts\activate
   ```

For more detailed setup instructions, see [SETUP.md](SETUP.md).

## Development Workflow

### Creating a Branch

Create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - New features or enhancements
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Test additions or modifications

### Making Changes

1. Make your changes in the codebase
2. Test your changes locally (see [Testing](#testing))
3. Ensure code follows our style guidelines (see [Coding Guidelines](#coding-guidelines))
4. Commit your changes with clear, descriptive messages

### Commit Messages

Write clear and descriptive commit messages:

```
Add feature to export specifications to JSON

- Implement JSONExporter class
- Add validation for export format
- Include tests for edge cases
```

Format:
- First line: Brief summary (50 chars or less)
- Blank line
- Detailed description with bullet points if needed

## Project Structure

```
MSML/
├── src/
│   └── math_spec_mapping/
│       ├── Classes/          # Core classes (Block, Space, State, etc.)
│       ├── Load/             # Loading and parsing specifications
│       ├── Reports/          # Report generation
│       └── Convenience/      # Helper utilities
├── examples/                 # Example specifications and notebooks
├── docs/                     # Documentation (Jekyll site)
├── tests/                    # Test suite (if present)
├── pyproject.toml           # Project metadata and dependencies
├── uv.lock                  # Locked dependencies
└── README.md                # Project overview
```

### Key Components

- **Classes**: Core abstractions (Block, Space, State, Mechanism, Policy, etc.)
- **Load**: Parsers and validators for JSON specifications
- **Reports**: Generators for Markdown, HTML, and Obsidian outputs
- **Convenience**: Helper functions for common workflows

## Coding Guidelines

### Python Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide
- Use meaningful variable and function names
- Keep functions focused and single-purpose
- Add docstrings to classes and public methods
- Use type hints where appropriate

### Code Quality

- **Keep it simple**: Prefer clarity over cleverness
- **DRY principle**: Don't repeat yourself
- **Avoid breaking changes**: Maintain backward compatibility when possible
- **Document assumptions**: Add comments for non-obvious logic

### Example Code Style

```python
from typing import Dict, Optional

class MyClass:
    """Brief description of the class.
    
    Longer description if needed, explaining the purpose
    and usage of the class.
    """
    
    def my_method(self, param: str, optional_param: Optional[int] = None) -> Dict[str, any]:
        """Brief description of what the method does.
        
        Args:
            param: Description of param
            optional_param: Description of optional_param
            
        Returns:
            Description of return value
        """
        # Implementation
        pass
```

## Testing

### Running Tests

If tests are present in the repository:

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_specific.py

# Run with coverage
uv run pytest --cov=math_spec_mapping
```

### Writing Tests

When adding new features:

1. Add unit tests for new functions/classes
2. Test edge cases and error conditions
3. Ensure tests are deterministic and isolated
4. Use descriptive test names

Example:
```python
def test_block_creation_with_valid_inputs():
    """Test that Block is created correctly with valid inputs."""
    # Arrange
    block_data = {...}
    
    # Act
    block = Block(block_data)
    
    # Assert
    assert block.name == expected_name
```

## Documentation

### Code Documentation

- Add docstrings to all public classes and methods
- Update docstrings when modifying existing code
- Use clear, concise language
- Include examples for complex functionality

### Project Documentation

When making significant changes:

1. Update relevant sections in `README.md`
2. Add or update documentation in `docs/`
3. Update examples if API changes affect them
4. Consider adding a guide or tutorial for new features

## Submitting Changes

### Before Submitting

1. **Test your changes**: Ensure all tests pass
2. **Check code style**: Follow the coding guidelines
3. **Update documentation**: Add/update relevant docs
4. **Review your changes**: Self-review the diff

```bash
# Review your changes
git diff

# Check what files will be committed
git status
```

### Creating a Pull Request

1. **Push your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request** on GitHub with:
   - Clear title describing the change
   - Description explaining what and why
   - Reference to related issues (e.g., "Closes #123")
   - Any special testing instructions

### Pull Request Template

```markdown
## Summary
Brief description of the changes

## Changes
- Change 1
- Change 2

## Related Issues
Closes #123

## Testing
How were these changes tested?

## Screenshots (if applicable)
Add screenshots for UI changes
```

### Review Process

- Maintainers will review your PR
- Address feedback and push updates to your branch
- Once approved, maintainers will merge your PR

### After Merging

1. Delete your feature branch (if desired)
2. Pull the latest main branch
   ```bash
   git checkout main
   git pull origin main
   ```

## Questions or Need Help?

- Open an issue for questions or discussions
- Check existing issues and documentation first
- Be specific about your environment and the problem

## Recognition

Contributors will be recognized in release notes and project documentation. Thank you for helping make MSML better!
