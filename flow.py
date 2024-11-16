__autor__ = "Minhajul Islam"
__discription__ = "This is a simple python script to generate flowchart from python code."
__version__ = "1.0.0"
__email__ = "x_spoilt@yahoo.com"

import ast
import sys
from rich.console import Console
from rich.tree import Tree
from rich.style import Style

console = Console()

class FlowchartGenerator:
    def __init__(self):
        self.console = console
        self.tree = None

    def generate(self, code, filename):
        """Generate a flowchart from the Python code."""
        self.tree = Tree(filename, style=Style(color="blue", bold=True))
        parsed_tree = ast.parse(code)
        self.visit(parsed_tree, self.tree)
        return self.tree

    def visit(self, node, parent_tree):
        """Determine the node type and visit the appropriate method."""
        node_type = type(node).__name__
        method_name = f"visit_{node_type}"
        visitor = getattr(self, method_name, self.generic_visit)
        visitor(node, parent_tree)

    def visit_Module(self, node, parent_tree):
        """Handle the module (root) of the code."""
        module_tree = parent_tree.add("Module", style=Style(color="green"))
        for child in node.body:
            self.visit(child, module_tree)

    def visit_FunctionDef(self, node, parent_tree):
        """Handle function definitions."""
        func_tree = parent_tree.add(f"Function: {node.name}()", style=Style(color="yellow", bold=True))
        for n in node.body:
            self.visit(n, func_tree)

    def visit_AsyncFunctionDef(self, node, parent_tree):
        """Handle asynchronous function definitions."""
        async_func_tree = parent_tree.add(f"Async Function: {node.name}()", style=Style(color="blue", bold=True))
        for n in node.body:
            self.visit(n, async_func_tree)

    def visit_If(self, node, parent_tree):
        """Handle if statements."""
        if_tree = parent_tree.add("If Condition", style=Style(color="cyan"))
        for n in node.body:
            self.visit(n, if_tree)
        if node.orelse:
            else_tree = parent_tree.add("Else Condition", style=Style(color="magenta"))
            for n in node.orelse:
                self.visit(n, else_tree)

    def visit_For(self, node, parent_tree):
        """Handle for loops."""
        for_tree = parent_tree.add("For Loop", style=Style(color="red"))
        for n in node.body:
            self.visit(n, for_tree)

    def visit_AsyncFor(self, node, parent_tree):
        """Handle async for loops."""
        async_for_tree = parent_tree.add("Async For Loop", style=Style(color="yellow"))
        for n in node.body:
            self.visit(n, async_for_tree)

    def visit_While(self, node, parent_tree):
        """Handle while loops."""
        while_tree = parent_tree.add("While Loop", style=Style(color="orange"))
        for n in node.body:
            self.visit(n, while_tree)

    def visit_Try(self, node, parent_tree):
        """Handle try blocks."""
        try_tree = parent_tree.add("Try Block", style=Style(color="green"))
        for n in node.body:
            self.visit(n, try_tree)
        if node.handlers:
            for handler in node.handlers:
                except_tree = parent_tree.add(f"Except: {handler.type}", style=Style(color="yellow"))
                self.visit(handler, except_tree)
        if node.finalbody:
            finally_tree = parent_tree.add("Finally Block", style=Style(color="blue"))
            for n in node.finalbody:
                self.visit(n, finally_tree)

    def visit_ClassDef(self, node, parent_tree):
        """Handle class definitions."""
        class_tree = parent_tree.add(f"Class: {node.name}", style=Style(color="purple", bold=True))
        for n in node.body:
            self.visit(n, class_tree)

    def visit_Lambda(self, node, parent_tree):
        """Handle lambda functions."""
        parent_tree.add(f"Lambda: {ast.unparse(node)}", style=Style(color="green"))

    def visit_Expr(self, node, parent_tree):
        """Handle expressions."""
        if isinstance(node.value, ast.Call):
            call_tree = parent_tree.add(f"Function Call: {ast.unparse(node.value)}", style=Style(color="purple"))
        else:
            parent_tree.add(f"Expression: {ast.unparse(node)}", style=Style(color="white"))

    def visit_Assign(self, node, parent_tree):
        """Handle assignments."""
        parent_tree.add(f"Assignment: {ast.unparse(node.targets[0])} = {ast.unparse(node.value)}", style=Style(color="green"))

    def visit_Return(self, node, parent_tree):
        """Handle return statements."""
        parent_tree.add(f"Return: {ast.unparse(node.value)}", style=Style(color="blue"))

    def visit_Call(self, node, parent_tree):
        """Handle function calls."""
        parent_tree.add(f"Function Call: {ast.unparse(node)}", style=Style(color="purple"))

    def visit_With(self, node, parent_tree):
        """Handle with statements."""
        with_tree = parent_tree.add("With Statement", style=Style(color="cyan"))
        for n in node.body:
            self.visit(n, with_tree)

    def visit_Import(self, node, parent_tree):
        """Handle import statements."""
        parent_tree.add(f"Import: {ast.unparse(node)}", style=Style(color="magenta"))

    def visit_ImportFrom(self, node, parent_tree):
        """Handle from-import statements."""
        parent_tree.add(f"From Import: {ast.unparse(node)}", style=Style(color="magenta"))

    def generic_visit(self, node, parent_tree):
        """Visit all child nodes of the current node."""
        for child in ast.iter_child_nodes(node):
            self.visit(child, parent_tree)


class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_code(self):
        """Read the code from the given file."""
        with open(self.filename, 'r') as file:
            return file.read()


def main(input_file):
    """Main function to generate the flowchart from a Python file."""
    processor = FileProcessor(input_file)
    code = processor.read_code()
    generator = FlowchartGenerator()
    flowchart_tree = generator.generate(code, filename=input_file)
    console.print(flowchart_tree)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python flow.py <input_python_file.py>")
        sys.exit(1)

    input_filename = sys.argv[1]
    main(input_filename)
