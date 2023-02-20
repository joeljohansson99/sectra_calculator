# Sectra Calculator Assignment

Simple calculator that can add, subtract and multiply values in a set of registers.

## Prerequisites

* Python 3 - https://www.python.org/downloads/

## Installation

```
git clone https://github.com/joeljohansson99/sectra_calculator.git
```

## Run

The calculator can either take console input, or a file as input.

To run with console input:
```
python3 calculator.py
```

To run with file input:
```
python3 calculator.py <file>
```

## Usage 

Syntax is as following:
```
<register> <operation> <value>
print <register>
quit
```

Registers is defined as any combination of alphanumeric characters.

All registers contains the value zero from start.

Allowed operations are `add`, `subtract` and `multiply`.