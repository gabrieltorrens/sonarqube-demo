#"<>" should not be used to test inequality
def main():
    number = input("Pick a number: ")
    if number <> 4:
        return("Wrong number")
    else:
        return("Correct number")

if __name__ == "__main__":
    print(main())
