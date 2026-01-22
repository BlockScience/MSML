#!/usr/bin/env python3
"""Load and validate an MSML specification from JSON.

This script provides a command-line interface for loading and validating
MSML specifications. It can be used in CI/CD pipelines or as part of
automated workflows.

Example usage:
    python scripts/load_and_validate_spec.py spec.json
    python scripts/load_and_validate_spec.py --verbose spec.json
"""

import argparse
import json
import sys
from pathlib import Path

from math_spec_mapping import load_from_json


def load_and_validate(spec_path: Path, verbose: bool = False) -> bool:
    """Load and validate an MSML specification.
    
    Args:
        spec_path: Path to the JSON specification file
        verbose: Whether to print detailed output
        
    Returns:
        True if validation successful, False otherwise
    """
    try:
        if verbose:
            print(f"Loading specification from: {spec_path}")
        
        # Load the specification
        with open(spec_path, 'r') as f:
            spec_data = json.load(f)
        
        # Parse with MSML
        ms = load_from_json(spec_data)
        
        if verbose:
            print(f"✓ Specification loaded successfully")
            print(f"  Blocks: {len(ms.blocks)}")
            print(f"  Spaces: {len(ms.spaces)}")
            print(f"  States: {len(ms.state)}")
            print(f"  Parameters: {len(ms.parameters)}")
        else:
            print(f"✓ {spec_path.name} is valid")
        
        return True
        
    except FileNotFoundError:
        print(f"✗ Error: File not found: {spec_path}", file=sys.stderr)
        return False
    except json.JSONDecodeError as e:
        print(f"✗ Error: Invalid JSON in {spec_path}: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"✗ Error validating {spec_path}: {e}", file=sys.stderr)
        if verbose:
            import traceback
            traceback.print_exc()
        return False


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Load and validate MSML specifications",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s spec.json
  %(prog)s --verbose spec.json
  %(prog)s spec1.json spec2.json spec3.json
        """
    )
    
    parser.add_argument(
        'specs',
        nargs='+',
        type=Path,
        help='Path(s) to MSML specification JSON file(s)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Print detailed output'
    )
    
    args = parser.parse_args()
    
    # Validate all specs
    all_valid = True
    for spec_path in args.specs:
        if not load_and_validate(spec_path, args.verbose):
            all_valid = False
    
    # Exit with appropriate code
    sys.exit(0 if all_valid else 1)


if __name__ == '__main__':
    main()
