#!/usr/bin/env python3
"""Generate reports from an MSML specification.

This script generates various reports (Markdown, Obsidian vault)
from an MSML specification. Useful for automated documentation generation
in CI/CD pipelines.

Example usage:
    python scripts/generate_reports.py spec.json --output ./reports
    python scripts/generate_reports.py spec.json --format markdown --output ./docs
"""

import argparse
import json
import sys
from pathlib import Path

from math_spec_mapping import load_from_json


def generate_reports(
    spec_path: Path,
    output_dir: Path,
    report_format: str = 'all',
    verbose: bool = False
) -> bool:
    """Generate reports from an MSML specification.
    
    Args:
        spec_path: Path to the JSON specification file
        output_dir: Directory to write reports to
        report_format: Format of reports ('markdown', 'obsidian', 'all')
        verbose: Whether to print detailed output
        
    Returns:
        True if successful, False otherwise
    """
    try:
        if verbose:
            print(f"Loading specification from: {spec_path}")
        
        # Load the specification
        with open(spec_path, 'r') as f:
            spec_data = json.load(f)
        
        _ms = load_from_json(spec_data)
        
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)
        
        if verbose:
            print(f"Generating reports in: {output_dir}")
        
        # Generate requested reports
        if report_format in ('markdown', 'all'):
            if verbose:
                print("  Generating Markdown reports...")
            ms.write_markdown_reports(output_dir)
            print(f"  ✓ Markdown reports generated")
        
        if report_format in ('obsidian', 'all'):
            if verbose:
                print("  Generating Obsidian vault...")
            ms.write_obsidian_vault(output_dir / "obsidian")
            print(f"  ✓ Obsidian vault generated")
        
        print(f"✓ Reports generated successfully in {output_dir}")
        return True
        
    except FileNotFoundError:
        print(f"✗ Error: File not found: {spec_path}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"✗ Error generating reports: {e}", file=sys.stderr)
        if verbose:
            import traceback
            traceback.print_exc()
        return False


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate reports from MSML specifications",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s spec.json
  %(prog)s spec.json --output ./reports
  %(prog)s spec.json --format markdown --output ./docs
        """
    )
    
    parser.add_argument(
        'spec',
        type=Path,
        help='Path to MSML specification JSON file'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=Path,
        default=Path('./reports'),
        help='Output directory for reports (default: ./reports)'
    )
    
    parser.add_argument(
        '-f', '--format',
        choices=['markdown', 'obsidian', 'all'],
        default='all',
        help='Report format to generate (default: all)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Print detailed output'
    )
    
    args = parser.parse_args()
    
    success = generate_reports(
        args.spec,
        args.output,
        args.format,
        args.verbose
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
