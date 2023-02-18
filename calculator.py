import sys

def eval(reg, regs, ops):
    (sum, _) = regs[reg]

    while len(ops[reg]) > 0:
        (op, param) = ops[reg].pop(0)

        if param.isnumeric():
            val = int(param)
        else:
            if param not in regs:
                print("Invalid input: " + param + " is not a register.")
                continue
            
            (val, updated) = regs[param]

            if not updated:
                eval(param, regs, ops)
                (val, _) = regs[param]

        if op == "add":
            sum += val
        elif op == "subtract":
            sum -= val
        elif op == "multiply":
            sum *= val

    regs[reg] = (sum, True)

def parse_line(input, regs, ops):
    if input[0] == "print":
        reg = input[1]
        (val, updated) = regs[reg]

        if not updated:
            eval(reg, regs, ops)
            (val, _) = regs[reg]

        print(val)
    else:
        [reg, op, param] = input

        if reg in ops:
            ops[reg].append((op, param))

            (val, updated) = regs[reg]

            if updated:
                regs[reg] = (val, False)
        else:
            regs[reg] = (0, False)
            ops[reg] = [(op, param)]

def main():

    regs = dict()
    ops = dict()

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            lines = [line.rstrip().lower() for line in file]

            for line in lines:
                input = line.split(" ")
                parse_line(input, regs, ops)

    else:
        for line in sys.stdin:
            input = line.rstrip().lower().split(" ")
            
            if input[0] == "quit":
                break

            parse_line(input, regs, ops)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())