import argparse

def matchLoops(program):
    loops = {}
    loopStart = []
    for i in range(len(program)):
        if program[i] == '[':
            loopStart.append(i)
        elif program[i] == ']':
            loops[i] = loopStart.pop()

    return(loops)

def readFromFile(fileName):
    program = ''
    file = open(fileName, 'r')

    for line in file:
        program += line
    
    return(program)

def fuck(program):
    #create variables
    loops = matchLoops(program)

    cell = [0]
    pointer = 0
    open = 0

    i = 0
    while i < len(program):
        match program[i]:
            case '>':
                pointer += 1

                try:
                    cell[pointer]

                except IndexError:
                    cell.append(0)

            case '<':
                if pointer == 0:
                    cell.insert(0, 0)

                else:
                    pointer -= 1

            case '+':
                cell[pointer] += 1

            case '-':
                cell[pointer] -= 1

            case '.':
                print(f"{chr(cell[pointer])}", end='')

            case ",":
                cell[pointer] = ord(input()[0])

            case '[':
                open += 1

            case']':
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

def main(file):
    program = readFromFile(file)

    fuck(program)

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

main(args.file)
