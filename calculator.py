import sys

# This function evaluates a register value
def eval(reg, regs, ops):
    (sum, _) = regs[reg]
    
    # Loop through the pending operations
    while len(ops[reg]) > 0:
        (op, param) = ops[reg].pop(0)

        # Check whether the parameter is a register or value
        if param.isnumeric():
            val = int(param)
        else: 
            # If no operations have been made in the specified register,
            # it is added to regs dictionary with value zero
            if param not in regs:
                regs[param] = (0, True)

            (val, updated) = regs[param]

            # If the value is not updated then it is evaluated first
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
            print("Invalid operation: " + op)

    # Lastly write the new value to the register and flag it as up-to-date
    regs[reg] = (sum, True)

# This function parses a command
def parse_command(cmd, regs, ops):
    if cmd[0] == "print":
        reg = cmd[1]

        # If no operations have been made in the specified register,
        # it is added to regs dictionary with value zero
        if reg not in regs:
            regs[reg] = (0,True)

        (val, updated) = regs[reg]

        # If the the registers value is not up-to-date then evaluate it first
        if not updated:
            eval(reg, regs, ops)
            (val, _) = regs[reg]

        print(val)
    
    else:
        [reg, op, param] = cmd

        # Add pending operation to register, and set the updated field to false
        if reg in ops:
            ops[reg].append((op, param))

            (val, updated) = regs[reg]

            # If the register had already been flagged as not up-to-date, then no need to write to it again
            if updated:
                regs[reg] = (val, False)
        else:
            # If the register is not in regs dictionary, add it with value zero and flagged as not up-to-date
            regs[reg] = (0, False)
            ops[reg] = [(op, param)]

def main():
    regs = dict() # stores value and updated field for each register
    ops = dict() # stores (pending) operations for each register

    # Reads input from either file or console
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:

            for line in file:
                cmd = line.rstrip().lower().split(" ")
                try:
                    parse_command(cmd, regs, ops)
                except:
                    # Will catch any input that does not match syntax
                    print("Invalid command: " + line.rstrip())

    else:
        for line in sys.stdin:
            cmd = line.rstrip().lower().split(" ")
            
            if cmd[0] == "quit":
                break
            try:
                parse_command(cmd, regs, ops)
            except:
                # Will catch any input that does not match syntax
                print("Invalid command: " + line.rstrip())
    
    return 0

if __name__ == '__main__':
    sys.exit(main())