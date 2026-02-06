def main():

    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    if is_answer(question):
        print('Yes')
    else:
        print('No')

def is_answer(response):
    response = response.strip().lower()
    return True if response == '42' or response == 'forty-two' or response == 'forty two' else False

if __name__ == "__main__": main()


# Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything.
# Outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No
