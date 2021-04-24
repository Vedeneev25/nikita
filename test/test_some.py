command = input("some calc")

def parse_command(command: str) -> list:
    parsedlone = command.replace(' ','')
    res = list(parsedlone)
    return res

def calc(command: str) -> float:
    precalc = ''.join(parse_command(command))
    res = eval(precalc)
    return res

command = input("some calc")
print(calc(command))