def assembler(program):
    """
    Assemble and execute a simple program represented as a list of instructions.

    Parameters:
        program (list): A list of strings representing the program instructions.

    Returns:
        int: The final value of the register after executing all the instructions in the program.
    """
    register = 0 

    for i in range(len(program)):
        if program[i] == "inc":
            register += 1 
        elif program[i] == "dec":
            register -= 1

    return register

    

# DO NOT CHANGE CODE BELOW!!!
def main():
    """TESTING CODE"""
    program = ['dec', 'inc', 'dec', 'dec', 'dec', 'inc']
    result = assembler(program)
    print(result)  # -2


if __name__ == '__main__':
    main()