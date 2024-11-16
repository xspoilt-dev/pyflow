# PyFlow: Python Code Flowchart Generator

PyFlow is a Python tool designed to parse Python code and generate flowcharts representing the flow of the code using the `ast` module and the `rich` library. The flowcharts are displayed in a tree-like structure for better understanding and visualization of the code's logic.

## Features

- Parse Python code using the `ast` module.
- Generate flowcharts with various Python constructs, such as functions, classes, loops, conditionals, and more.
- Utilize the `rich` library for color-coded, visually appealing flowcharts.
- Support for synchronous and asynchronous constructs.
- Handle common Python statements like imports, assignments, and function calls.

## Supported Constructs

PyFlow can handle a wide range of Python constructs, including but not limited to:

| **Construct Type**             | **Description**                                           |
|---------------------------------|-----------------------------------------------------------|
| `Module`                       | Root module of the code.                                  |
| `FunctionDef`                  | Function definitions, including both normal and async.     |
| `ClassDef`                     | Class definitions, including methods and attributes.       |
| `If`                           | If conditional statements, including `else` blocks.        |
| `For`                          | For loops.                                                 |
| `While`                        | While loops.                                               |
| `AsyncFor`                     | Asynchronous for loops.                                   |
| `Try`                          | Try blocks with `except` and `finally` blocks.             |
| `Return`                       | Return statements and their returned values.              |
| `Expr`                         | General expressions including function calls.             |
| `Lambda`                       | Lambda function definitions.                              |
| `With`                         | Context management (`with` statements).                    |
| `Import`                       | Regular `import` statements.                               |
| `ImportFrom`                   | `from module import` statements.                          |
| `Assign`                       | Variable assignments.                                     |
| `AsyncFunctionDef`             | Asynchronous function definitions.                        |
| `Call`                         | Function calls (both normal and lambda calls).             |

## Installation

To get started with PyFlow, follow these steps:
   ```bash
   git clone https://github.com/xspoilt-dev/pyflow.git
   cd pyflow
   pip install rich
   python flow.py
   ```

## Example 
example.py:
   ```python
  def example_function():
    a = 10
    if a > 5:
        return "Greater than 5"
    else:
        return "Less than or equal to 5"

   ```
When you run the following command:
   ```bash
   python flow.py example.py
   ```

Output: 
 ```mathematica
xd.py
└── Module
    └── Function: example_function()
        ├── Assignment: a = 10
        ├── If Condition
        │   └── Return: 'Greater than 5'
        └── Else Condition
            └── Return: 'Less than or equal to 5'
   
   ```
