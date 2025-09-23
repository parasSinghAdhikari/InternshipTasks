#!/usr/bin/env python
# coding: utf-8

# In[31]:


"""Command Line Calculator A well-structured calculator """
import math
import operator
from abc import ABC, abstractmethod
from typing import Union, List, Dict, Callable
from enum import Enum
import re


# In[32]:


class OperationType(Enum):
    """Enumeration for different types of calculator operations"""
    BASIC = "basic"
    SCIENTIFIC = "scientific"
    LOGARITHMIC = "logarithmic"
    CONVERSION = "conversion"


# In[33]:


class Operation(ABC):
    """Abstract base class for all calculator operations"""

    def __init__(self, name: str, symbol: str, operation_type: OperationType):
        self.name = name
        self.symbol = symbol
        self.operation_type = operation_type

    @abstractmethod
    def execute(self, *args) -> float:
        """Execute the operation with given arguments"""
        pass

    @abstractmethod
    def validate_args(self, *args) -> bool:
        """Validate the arguments for this operation"""
        pass


# In[34]:


# type(a) == int                                             isinstance(a, int)
# This checks if the exact type of a is int.                 This checks if a is an instance of int or a subclass of int.
# It does not consider inheritance.                          More flexible.  

class BasicOperation(Operation):
    """Basic arithmetic operations like +, -, *, /"""

    def __init__(self, name: str, symbol: str, func: Callable):
        super().__init__(name, symbol, OperationType.BASIC)
        self.func = func

    def execute(self, a: float, b: float) -> float:
        if not self.validate_args(a, b):
            raise ValueError(f"Invalid arguments for {self.name}")
        return self.func(a, b)

    def validate_args(self, a: float, b: float) -> bool:
        if self.symbol == "/" and b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return isinstance(a, (int, float)) and isinstance(b, (int, float))


# In[35]:


class UnaryOperation(Operation):
    """Unary operations like sqrt, sin, cos, etc."""

    def __init__(self, name: str, symbol: str, operation_type: OperationType, func: Callable):
        super().__init__(name, symbol, operation_type)
        self.func = func

    def execute(self, a: float) -> float:
        if not self.validate_args(a):
            raise ValueError(f"Invalid argument for {self.name}")
        return self.func(a)

    def validate_args(self, a: float) -> bool:
        # Special validation for specific functions
        if self.symbol == "sqrt" and a < 0:
            raise ValueError("Cannot take square root of negative number")
        if self.symbol == "!" and (a < 0 or not isinstance(a, int) and not a.is_integer()):
            raise ValueError("Factorial is only defined for non-negative integers")
        if self.symbol in ["asin", "acos"] and (a < -1 or a > 1):
            raise ValueError(f"{self.name} domain error: input must be between -1 and 1")
        return isinstance(a, (int, float))


# In[36]:


class PowerOperation(Operation):
    """Power operations """
    def __init__(self):
        super().__init__("power", "^", OperationType.BASIC)

    def execute(self, base: float, exponent: float) -> float:
        if not self.validate_args(base, exponent):
            raise ValueError("Invalid arguments for power operation")
        return pow(base, exponent)

    def validate_args(self, base: float, exponent: float) -> bool:
        if base == 0 and exponent < 0:
            raise ValueError("Cannot raise 0 to negative power")
        if base < 0 and not isinstance(exponent, int) and not exponent.is_integer():
            raise ValueError("Cannot raise negative number to non-integer power")
        return isinstance(base, (int, float)) and isinstance(exponent, (int, float))


# In[50]:


class CalculatorEngine:
    """Main calculator engine that manages all operations"""

    def __init__(self):
        self.operations: Dict[str, Operation] = {}
        self._initialize_operations()

    def _initialize_operations(self):
        """Initialize all calculator operations"""

        # Basic arithmetic operations
        basic_ops = [
            BasicOperation("addition", "+", operator.add),
            BasicOperation("subtraction", "-", operator.sub),
            BasicOperation("multiplication", "*", operator.mul),
            BasicOperation("division", "/", operator.truediv),
            BasicOperation("modulo", "%", operator.mod),
            BasicOperation("power", "**", operator.pow)
        ]

        # Power operation
        power_op = PowerOperation()

        # Scientific/Mathematical operations
        scientific_ops = [
            UnaryOperation("square_root", "sqrt", OperationType.SCIENTIFIC, math.sqrt),
            UnaryOperation("absolute", "abs", OperationType.SCIENTIFIC, abs),
            UnaryOperation("factorial", "!", OperationType.SCIENTIFIC, lambda x: math.factorial(int(x))),
            UnaryOperation("natural_log", "ln", OperationType.LOGARITHMIC, math.log),
            UnaryOperation("log_base_10", "log", OperationType.LOGARITHMIC, math.log10),
            UnaryOperation("exponential", "exp", OperationType.SCIENTIFIC, math.exp),
            UnaryOperation("ceiling", "ceil", OperationType.SCIENTIFIC, math.ceil),
            UnaryOperation("floor", "floor", OperationType.SCIENTIFIC, math.floor)
        ]

        # Add all operations to the operations dictionary
        all_operations = basic_ops + [power_op] + scientific_ops

        for op in all_operations:
            self.operations[op.symbol] = op
            self.operations[op.name] = op

    def calculate(self, expression: str) -> float:
        """Calculate a mathematical expression"""
        try:
            result = self._evaluate_expression(expression)
            return result
        except Exception as e:
            print(f"Error: {str(e)}")

    def _evaluate_expression(self, expr: str) -> float:
        expr = expr.strip()
        # 1) Function call? e.g. sqrt(3)
        func_match = re.fullmatch(r'([a-zA-Z_]+)\(([-\d\.]+)\)', expr)
        if func_match:
            sym, val = func_match.groups()
            val = float(val)
            op = self.operations.get(sym)
            if not op or not isinstance(op, UnaryOperation):
                raise ValueError(f"Unknown unary op {sym}")
            return op.execute(val)

        # 2) Factorial postfix? e.g. 5!
        fact_match = re.fullmatch(r'([-\d\.]+)!', expr)
        if fact_match:
            val = float(fact_match.group(1))
            op = self.operations.get("!")
            return op.execute(val)

        # 3) Binary op? e.g. 2+3, 3**2
        #    Sort symbols by length to match '**' before '*'
        syms = sorted(self.operations.keys(), key=len, reverse=True)
        for sym in syms:
            if sym in ["+", "-", "*", "/", "%", "**"]:
                parts = expr.split(sym)
                if len(parts) == 2:
                    a, b = map(float, parts)
                    op = self.operations[sym]
                    return op.execute(a, b)

        raise ValueError(f"Could not parse expression: {expr}")



    def list_operations(self, operation_type: OperationType = None) -> Dict:
        """List all available operations, optionally filtered by type"""
        if operation_type:
            return {operation_type: [f"{op.symbol}: {op.name}" for op in self.operations.values() 
                   if op.operation_type == operation_type]}
        else:
            # Group by type
            grouped = {}
            for op in self.operations.values():
                if op.operation_type not in grouped:
                    grouped[op.operation_type] = []
                if f"{op.symbol}: {op.name}" not in grouped[op.operation_type]:
                    grouped[op.operation_type].append(f"{op.symbol}: {op.name}")
            return grouped



# In[52]:


class CalculatorCLI:
    """Command line interface for the calculator"""

    def __init__(self):
        self.calculator = CalculatorEngine()
        self.running = True

    def display_welcome(self):
        """Display welcome message and instructions"""
        print("=" * 70)
        print("COMMAND LINE CALCULATOR")
        print("=" * 70)
        print("Welcome to the Calculator!")
        print("\n FEATURES:")
        print("• Basic arithmetic: +, -, *, /, %,**")
        print("• Scientific: sqrt, abs, factorial(!), exp, ceil, floor")
        print("• Logarithmic: ln (natural log), log (base 10)")
        print("\n COMMANDS:")
        print("• 'help' - Show detailed help")
        print("• 'ops' - List all operations by category")
        print("• 'quit' or 'exit' - Exit calculator")
        print("=" * 70)

    def display_help(self):
        """Display detailed help information"""
        print("\n CALCULATOR HELP")
        print("-" * 50)
        print(" Expression Examples:")
        print("• Basic arithmetic: 5 + 3 * 2, (10 - 4) / 2")
        print("• Powers: 2**8, sqrt(16)")
        print("• Functions: sqrt(25), abs(-10), 5!")
        print("• Logarithms: ln(e), log(100)")
        print("• Scientific: exp(1), ceil(4.2), floor(4.8)")
        print("\n Supported Operations:")
        print("• +, -, *, /, %, // (floor division)")
        print("• ^ or ** (power)")
        print("• sqrt(), abs(), exp(), ln(), log()")
        print("• factorial: 5! or factorial(5)")
        print("• ceil(), floor(), rad(), deg()")
        print("-" * 50)

    def list_operations(self):
        """Display all available operations grouped by type"""
        print("\n AVAILABLE OPERATIONS")
        print("-" * 50)
        grouped_ops = self.calculator.list_operations()

        for op_type, operations in grouped_ops.items():
            print(f"\n {op_type.value.upper()}:")
            for op in operations:
                print(f"   {op}")
        print("-" * 50)


    def run(self):
        """Main calculator loop"""
        self.display_welcome()

        while self.running:
            try:
                user_input = input("\n calc> ").strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye! Thanks for using the calculator!")
                    break
                elif user_input.lower() == 'help':
                    self.display_help()
                    continue
                elif user_input.lower() == 'ops':
                    self.list_operations()
                    continue

                # Calculate expression
                result = self.calculator.calculate(user_input)
                print(f" Result: {result}")

                # Format large numbers nicely
                if abs(result) > 1000000:
                    print(f" Scientific: {result:.2e}")
                elif abs(result) < 0.001 and result != 0:
                    print(f" Scientific: {result:.2e}")

            except KeyboardInterrupt:
                print("\n\n Goodbye! Thanks for using the calculator!")
                break
            except ZeroDivisionError:
                print("Error: Division by zero!")
            except ValueError as e:
                print(f" Error: {e}")
            except Exception as e:
                print(f" Unexpected error: {e}")


def main():
    """Main function to run the calculator"""
    calculator_cli = CalculatorCLI()
    calculator_cli.run()

if __name__ == "__main__":
    main()

