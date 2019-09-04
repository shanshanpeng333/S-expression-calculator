# S-expression-calculator
A python program that acts as a simple calculator: it takes a single argument as an expression and prints out the integer result of evaluating it.

## Main idea of this solution:
1. use regex to define the S-Expression
Firstly, I defined REGEX_OLD which support exactly two arguments in the Expression:
```sh
REGEX_OLD = r'^\(([a-z]+)\s+(\d+|\([a-z, 0-9, \s, \(, \)]+\))\s+(\d+|\([a-z, 0-9, \s, \(, \)]+\))\)$'
```
2. I updated it to support an arbitrary number of arguments. To support it, I also modified the codes in calculate:
```sh
REGEX = r'^\(([a-z]+)(\s+(?:\d+|\([a-z, 0-9, \s, \(, \)]+\)))+\)$'
```
3. Use the regex match function and recursion to find all the groups and do the calculation

## How to run it:
install regex
```sh
pip install regex
```
Run calculator in command line. It only requires one argument which is S-Expression.
```sh
python calculator.py "(add 1 2)"
```

Run unit test
```sh
python -m unittest test/test_calculator.py
```
