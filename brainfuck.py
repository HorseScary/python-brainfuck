def matchLoops(program):
    loops = {}
    loopStart = []
    for i in range(len(program)):
        if program[i] == '[':
            loopStart.append(i)
        elif program[i] == ']':
            loops[i] = loopStart.pop()

    return(loops)

def makeList(pro):
    program = []

    for i in range(len(pro)):
        program.append(pro[i])
    return(program)

def main(pro):
    #create variables
    program = makeList(pro)
    loops = matchLoops(program)

    cell = [0]
    pointer = 0
    open = 0

    i = 0
    while i < len(program):
#        print(f'cells: {cell}\nloop status: {open}')

        if program[i] == '>':
            pointer += 1

            try:
                cell[pointer]

            except IndexError:
                cell.append(0)

        elif program[i] == '<':
            if pointer == 0:
                cell.insert(0, 0)

            else:
                pointer -= 1

        elif program[i] == '+':
            cell[pointer] += 1

        elif program[i] == '-':
            cell[pointer] -= 1

        elif program[i] == '.':
            print(f"{chr(cell[pointer])}", end='')

        elif program[i] ==",":
            cell[pointer] = ord(input()[0])

        elif program[i] == '[':
            open += 1

        elif program[i] == ']':
            if open == 0:
                print("LoopError\nA loop has an end, but no start!")

            elif cell[pointer] == 0:
                open -= 1
                pass

            else: 
                i = loops[i]

        i += 1

    if open != 0:
        return('LoopError\nA loop has a start, but no end!')

    print("")