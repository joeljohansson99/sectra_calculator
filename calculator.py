import sys

# This function evaluates a register value
def eval(reg, regs, ops):
    (sum, _) = regs[reg]

    while len(ops[reg]) > 0:
        (op, param) = ops[reg].pop(0)

        if param.isnumeric():
            val = int(param)
        else: 
            if param not in regs:
                regs[param] = (0, True)

            (val, updated) = regs[param]

            if not updated:
                eval(param, regs, ops)
                (val, _) = regs[param]

        # Operations
        if op == "add":
            sum += val
        elif op == "subtract":
            sum -= val
        elif op == "multiply":
            sum *= val
        else:
            print("Invalid operand: " + op)

    regs[reg] = (sum, True)

# This function parses a command
def parse_command(cmd, regs, ops):
    if cmd[0] == "print":
        reg = cmd[1]

        if reg not in regs:
            regs[reg] = (0,True)

        (val, updated) = regs[reg]

        if not updated:
            eval(reg, regs, ops)
            (val, _) = regs[reg]

        print(val)

    else:
        [reg, op, param] = cmd

        if reg in ops:
            ops[reg].append((op, param))

            (val, updated) = regs[reg]

            if updated:
                regs[reg] = (val, False)
        else:
            regs[reg] = (0, False)
            ops[reg] = [(op, param)]

def main():
    regs = dict() # stores value and updated field for each register
    ops = dict() # stores (pending) operations for each register

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:

            for line in file:
                cmd = line.rstrip().lower().split(" ")
                try:
                    parse_command(cmd, regs, ops)
                except:
                    print("Invalid command: " + line.rstrip())
    else:
        for line in sys.stdin:
            cmd = line.rstrip().lower().split(" ")
            
            if cmd[0] == "quit":
                break
            try:
                parse_command(cmd, regs, ops)
            except:
                print("Invalid command: " + line.rstrip())
    
    return 0

if __name__ == '__main__':
    sys.exit(main())