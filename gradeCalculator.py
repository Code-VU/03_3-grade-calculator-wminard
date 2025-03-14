def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    try:
        grade = float(input("Enter score:"))
        if grade > 1:
            print("Bad score")
        elif grade >= 0.9:
            print("A")
        elif grade >= 0.8:
            print("B")
        elif grade >= 0.7:
            print("C")
        elif grade >= 0.6:
            print("D")
        elif grade >= 0:
            print("F")
        else:
            print("Bad score")
    except ValueError:
        print("Bad score")

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
