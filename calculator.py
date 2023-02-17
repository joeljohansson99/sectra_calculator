import sys

def eval(reg, regs, ops):
    (sum, _) = regs[reg]

    while len(ops[reg]) > 0:
        (op, param) = ops[reg].pop(0)

        if param.isnumeric():
            val = int(param)
        else:
            (val, updated) = regs[param]

            if not updated:
                eval(param, regs, ops)
                (val, _) = regs[param]

            val = regs[val]

        if op == "add":
            sum += val
        elif op == "subtract":
            sum -= val
        elif op == "multiply":
            sum *= val

    regs[reg] = (sum, True)

def main():

    regs = dict()
    ops = dict()

    if len(sys.argv) > 1:
        file = sys.argv[1]

    else:
        for line in sys.stdin:
            input = line.rstrip().lower().split(" ")
            
            if input[0] == "quit":
                break

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
                    ops[reg] = [(op, val)]
    
    return 0

if __name__ == '__main__':
    sys.exit(main())