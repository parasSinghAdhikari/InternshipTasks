## Command Line Calculator
A well-structured Command Line Calculator implemented in Python, supporting basic arithmetic, scientific functions, logarithms, and conversion operations. The project features a modular design with an abstract Operation class and specialized subclasses (BasicOperation, UnaryOperation, PowerOperation) encapsulating individual operation logic. The CalculatorEngine orchestrates parsing and evaluation without using eval, and the CalculatorCLI provides an interactive user interface.

## Features
Basic arithmetic: addition (+), subtraction (-), multiplication (*), division (/), modulo (%)

Exponentiation: power operator (** and ^ alias)

Scientific functions: sqrt(), abs(), exp(), ceil(), floor()

Logarithms: natural log (ln), base-10 log (log)

Factorial: postfix ! or function form factorial()

Clear, modular code structure enabling easy extension for new operations

Safe parsing and evaluation without Python's eval function

## Installation
Clone the repository:

bash
git clone <repository-url>
cd command-line-calculator
Create a virtual environment (optional but recommended):

bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\\Scripts\\activate  # Windows
Install dependencies:

bash
pip install -r requirements.txt
Usage
Run the calculator via the command line:

bash
python calculator.py
You will see a prompt:

text
COMMAND LINE CALCULATOR
======================
calc>
Commands
help — Show detailed help and supported expressions

ops — List available operations by category

exit or quit — Exit the calculator

## Expression Examples
text
calc> 2 + 3
Result: 5.0

calc> 4 * (5 + 2)
Result: 28.0

calc> sqrt(16)
Result: 4.0

calc> 5!
Result: 120

calc> 2^3
Result: 8.0

calc> ln(2.71828)
Result: 1.0

## Code Structure
calculator.py — Main module containing:

Operation hierarchy (Operation, BasicOperation, UnaryOperation, PowerOperation)

CalculatorEngine — Parser and evaluator

CalculatorCLI — Command-line interface

README.md — Project overview and usage instructions

requirements.txt — Python dependencies

## Extending the Calculator
To add a new operation:

Create a subclass of Operation or BasicOperation/UnaryOperation.

Implement execute and validate_args methods.

Register the new operation in CalculatorEngine._initialize_operations() by adding it to the list of operations.

## License
This project is open source and available under the MIT License.
