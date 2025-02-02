# Python Module Import Guide for VS Code

This guide demonstrates how to properly set up Python module imports in VS Code, specifically addressing the common `ModuleNotFoundError` issue.

## Project Structure

```
project/
├── .venv/             # Virtual environment
├── __init__.py        # Makes the root directory a package
├── folder1/
│   ├── __init__.py    # Makes folder1 a package
│   └── main.py        # Script that imports the module
└── folder2/
    ├── __init__.py    # Makes folder2 a package
    └── calculator.py  # Module containing our functions
```

## Step 1: Create Project Structure

1. Create the project directory and its subdirectories
2. Create empty `__init__.py` files in each directory
3. These files mark directories as Python packages, making them importable

## Step 2: Set Up Virtual Environment

```bash
# Navigate to project root
cd path/to/project

# Create virtual environment using uv
uv init python 3.11

# Activate virtual environment (Windows)
.venv\Scripts\activate
```

## Step 3: Create the Calculator Module

In `folder2/calculator.py`:
```python
def sum_numbers(*args):
    """Sum any number of input values."""
    return sum(args)

def multiply_numbers(*args):
    """Multiply any number of input values."""
    result = 1
    for num in args:
        result *= num
    return result
```

## Step 4: Create the Main Script

In `folder1/main.py`:
```python
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from folder2.calculator import sum_numbers, multiply_numbers

def main():
    # Test sum_numbers
    print("Sum test: 1 + 2 + 3 + 4 =", sum_numbers(1, 2, 3, 4))
    
    # Test multiply_numbers
    print("Multiplication test: 2 * 3 * 4 =", multiply_numbers(2, 3, 4))

if __name__ == "__main__":
    main()
```

## VS Code vs PyCharm: Understanding the Difference

The extra code needed in VS Code but not in PyCharm:
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

### Why is this needed?

1. **PyCharm's Auto-Configuration**: 
   - PyCharm automatically marks source roots and configures the Python path
   - It handles module imports internally without additional code

2. **VS Code's Minimal Approach**:
   - VS Code doesn't automatically modify the Python path
   - It requires explicit path configuration for importing modules from different directories
   - The added code manually adds the project root to Python's path, enabling imports from any project directory

3. **The Code Explained**:
   - `os.path.abspath(__file__)`: Gets the absolute path of the current file
   - `os.path.dirname()`: Gets the parent directory (used twice to get project root)
   - `sys.path.append()`: Adds the project root to Python's import path

## Setting Up VS Code

1. Select Python Interpreter:
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose the interpreter from your `.venv` folder

2. Configure Workspace Settings (Optional):
   Create `.vscode/settings.json`:
```json
{
    "python.analysis.extraPaths": [
        "${workspaceFolder}"
    ]
}
```

## Testing the Setup

Run `main.py` to verify the setup:
```bash
python folder1/main.py
```

Expected output:
```
Sum test: 1 + 2 + 3 + 4 = 10
Multiplication test: 2 * 3 * 4 = 24
```