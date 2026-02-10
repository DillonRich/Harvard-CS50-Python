def main():

    m = int(input("Give a mass: ")) # in kilograms
    c = 300000000 # in meters per second
    E = m * c**2
    print(E)
# print(f"The mass of {m} Kg is equal to {E} Jules")
if __name__ == "__main__": main()


'''
𝐸 =𝑚⁢𝑐2, wherein 𝐸 represents energy (measured in Joules), 𝑚 represents mass (measured in kilograms), and 𝑐 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
