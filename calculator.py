import sys
import itertools
import regex
from functools import reduce

REGEX = r'^\(([a-z]+)(\s+(?:\d+|\([a-z, 0-9, \s, \(, \)]+\)))+\)$'

def calculate(s_express: str):
    """
    Calculate and return the result of S-Expression
    :param s_express: the S-Expression
    :return: calculated result of the entered Expression
    """
    # remove the extra spaces
    express = s_express.lstrip().rstrip()

    # return it if the S-Expression is just a digit
    if express.isdigit():
        return int(express)

    # match the S-Expression with the defined REGEX
    m = regex.match(REGEX, express)

    if len(m.groups()) == 2:
        # get the first Function
        func = m.captures(1)
        '''
        the reason doing group conversion is considered this situation: "(Add (multiply 2 2) (add 1 2))", so I find 
        all the ') (', replace them with ')|(', and then split them with '|'
        '''
        groups = list(map(lambda g: g.replace(') (', ')|(').split('|'), m.captures(2)))
        groups = list(itertools.chain(*groups))
        # print(groups)
        if groups and len(groups) >= 2:
            groups = list(map(calculate, groups))
            if func and func[0] == 'add':
                return sum(groups)
            if func and func[0] == 'multiply':
                return reduce(lambda a, b: a*b, groups)
            # more math can be added here. For example: ^
            else:
                print('The calculator does not support an operator other than add or multiply')
    print('The format of input is not correct, it should be: (FUNCTION EXPR EXPR)')


if __name__ == "__main__":
    if sys.argv and len(sys.argv) == 2:
        result = calculate(sys.argv[1])
        print(result)
    else:
        print("No instruction is given to Calculator, please enter the S-Expression as the first parameter with "
              "double/single quote. For example: python calculator.py  '(add 1 (multiply 2 3))'")
