# Folder Sorter

A simple Python CLI tool that automatically organizes files in a given folder based on their file types. Supports dry-run simulation to preview actions before applying them.

## Features

- Sorts files into categorized folders:
  - `.pdf` -> `PDFs/`
  - `.py` -> `Python/`
  - `.jpg`, `.jpeg`, `.png` -> `Images/`
- Ignores subdirectories and unsupported file types
- Dry-run mode to simulate actions without modifying files
- Clear, colorless CLI output

## Usage

```bash
python core.py [folder_path] [--dry_run]
```

## Example
```bash
python core.py D:\Downloads --dry_run
```
Simulates the sorting process.
```bash
python core.py D:\Downloads
```
Performs the actual sorting by moving the files.

## Running Tests
All unit tests are located in the **tests/** directory
To run the tests:
```bash
python -m unittest discover tests
```

## Setup (Optional CLI install)
To install the package locally with a CLI entry point:
1. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```
2. Install in editable mode:
```bash
pip install -e .
```
3. Use the CLI:
```bash
folder-sorter [folder_path] [--dry_run]
```

## Project Structure
```arduino
folder-sorter/
	.gitignore
	__init__.py
	core.py
	LICENSE
	main.py
	README.md
	requirements.txt
	setup.py
	tests/
		__init__.py
		test_core.py
```

## License
MIT License © 2025 Beatrice M. Antoniu