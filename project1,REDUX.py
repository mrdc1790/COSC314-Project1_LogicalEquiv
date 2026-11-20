"""Evaluate a Boolean expression using up to five supplied variables."""

import ast
import re


def evaluate_expression(expression, values):
    """Evaluate names, Boolean values, parentheses, not, and, and or."""
    expression = re.sub(r'\bn([a-e])\b', r'not \1', expression.lower()).strip()
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as error:
        raise ValueError("Enter a valid Boolean expression.") from error

    def evaluate(node):
        if isinstance(node, ast.Name):
            if node.id in values:
                return values[node.id]
            if node.id in ("true", "false"):
                return node.id == "true"
            raise ValueError(f"Unknown variable: {node.id}")
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            return not evaluate(node.operand)
        if isinstance(node, ast.BoolOp):
            operands = [evaluate(operand) for operand in node.values]
            return all(operands) if isinstance(node.op, ast.And) else any(operands)
        raise ValueError("Use Boolean values, variables, parentheses, not, and, or.")

    return evaluate(tree.body)


def main():
    print("Logical Expressions Evaluator")
    while True:
        count = input("Enter the number of variables in the expression (1-5): ").strip()
        if count in ("1", "2", "3", "4", "5"):
            break
        print("Enter an integer from 1 to 5.")

    values = {}
    for name in "abcde"[:int(count)]:
        while True:
            choice = input(f"{name} (true or false): ").strip().lower()
            if choice in ("t", "true", "f", "false"):
                values[name] = choice in ("t", "true")
                break
            print("Enter true or false.")

    while True:
        expression = input("Enter a logical expression: ")
        try:
            result = evaluate_expression(expression, values)
        except (ValueError, RecursionError) as error:
            print(error)
        else:
            print(f"The truth value of the given logical expression is: {result}")
            return


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        pass
