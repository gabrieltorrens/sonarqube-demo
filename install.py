#"<>" should not be used to test inequality
def main():
    number = input("Pick a number: ")
    if number <> 4:
        break #should not be used outside a loop
    else:
        return("Correct Number")

if __name__ == "__main__":
    print(main())
