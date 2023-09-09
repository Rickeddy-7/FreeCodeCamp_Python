
def arithmetic_arranger(problems, answer=False):
    """takes in a list of basic math problems and returns a visual
       representation of the problem arranged vertically side by side"""

    verdict = correct_data(problems)
    if verdict != 'proceed':
        return verdict

    top_row_nums,btm_row_nums,line_row,solutions = [],[],[],[]
    sep = '    ' # seperator

    problems = [prob.split() for prob in problems]
    for prob in problems:
        if len(prob[0]) > len(prob[2]):
            max_len = len(prob[0])+2
        else: max_len = len(prob[2])+2
        
        num1 = ' '*(max_len-len(prob[0])) + prob[0]
        top_row_nums.append(num1)

        num2 = prob[1] + ' '*((max_len-1)-len(prob[2])) + prob[2]
        btm_row_nums.append(num2)

        line = '-'*max_len
        line_row.append(line)

        solution = solve(int(prob[0]),prob[1],int(prob[2]))
        ans = ' '*(max_len-len(str(solution))) + str(solution)
        solutions.append(str(ans))
    
    arranged_problems = [sep.join(top_row_nums),sep.join(btm_row_nums),sep.join(line_row),sep.join(solutions)]

    if answer: return '\n'.join(arranged_problems)
    else: return '\n'.join(arranged_problems[:3])


def correct_data(problems):
    """returns an error message if data is not accurate"""

    if len(problems) > 5:
        return 'Error: Too many problems.'

    p = [prob.split() for prob in problems]

    proper_len = check_length(p)
    if not proper_len:
        return 'Error: Numbers cannot be more than four digits.'
    
    operator_allowed = proper_operand(p)
    if not operator_allowed:
        return 'Error: Operator must be \'+\' or \'-\'.'

    problems_are_all_nums = all_numbers(p)
    if not problems_are_all_nums:
        return 'Error: Numbers must only contain digits.'
    
    return 'proceed'


def solve(a,operand,b):
    """returns the sum or difference of the given problem"""

    if operand == '-':
        return a-b
    return a+b


def all_numbers(lst):
    """returns true if all elements in the given iterable are digits"""

    for item in lst:
        if not item[0].isdigit() or not item[-1].isdigit():
            return False
    return True


def proper_operand(lst):
    """return true only if the operands in the iterable are '-' or '+'"""

    unwanted = ['/','*']
    for prob in lst:
        for elem in prob:
            if elem in unwanted:
                return False
    return True
    

def check_length(lst):
    """returns true if elements in iterable are <= max"""

    max = 4
    for prob in lst:
        for elem in prob:
            if len(elem) > max:
                return False
    return True
