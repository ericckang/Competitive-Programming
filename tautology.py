#Author: Eric Kang
#It is not ok to share my code anonymously for educational purposes
def evaluate(expr, values):
    val, index = parse(expr, values, 0) #get the truth value
    return val

def parse(expr, values, index): #index points to current position in expression
    if index >= len(expr): #check if we point to outside of expr
        return None, index

    ch = expr[index] #innitialize the character to work with

    if ch in 'pqrst': #if ch is logical variable return dic value
        return values[ch], index + 1
    elif ch == 'N': #if character is NOT operation, recursively evaluate the expression with the next character and negate the value
        val, next_index = parse(expr, values, index + 1) #check the next variable
        return 1 - val, next_index  #negate the value
    else: #need two operands w and x
        w, next_index1 = parse(expr, values, index + 1) #need left and right operands
        x, next_index2 = parse(expr, values, next_index1)
        if ch == 'K': #apply the appropriate operation based on the problem give.
            return (1 if w and x else 0), next_index2 #K is and
        elif ch == 'A':
            return (1 if w or x else 0), next_index2 #A is or
        elif ch == 'C':
            return (1 if not w or x else 0), next_index2 #C is implies
        elif ch == 'E':
            return (1 if w == x else 0), next_index2 #E is equals


def is_tautology(expr):
    """Determines if the given expression is a tautology."""
    for p in range (0, 2): # check  every single combination of 1 and 0 for the variable if expression is always true
        for q in range (0, 2):
            for r in range (0, 2):
                for s in range (0, 2):
                    for t in range (0, 2):
                        values = {'p': p, 'q': q, 'r': r, 's': s, 't': t}
                        if not evaluate(expr, values): #if one evalution comes out to be false, return false
                            return False
    return True #return true if tautology


def main():
    while True:
        expr = input()
        if expr == '0':
            break
        elif is_tautology(expr):
            print("tautology")
        else:
            print("not")


if __name__ == "__main__":
    main()
