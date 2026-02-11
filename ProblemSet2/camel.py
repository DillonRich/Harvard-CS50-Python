def main():

    CamelInput = input("CamelCaseInput: ")
    print(to_snake(CamelInput))

def to_snake(CamelInput):
    if not CamelInput:
        return ""
    snake = CamelInput[0].lower()
    for ch in CamelInput[1:]:
        if ch.isupper():
            snake += "_" + ch.lower()
        else:
            snake += ch
    return snake

main()

# implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case
