def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    try:
        grade = float(input("Enter score:"))
        if grade >= 0.9:
            print("A")
        elif grade >= 0.8:
            print("B")
        elif grade >= 0.7:
            print("C")
        elif grade >= 0.6:
            print("D")
        else:
            print("F")
    except ValueError or grade < 0 or grade > 1:
        print("Bad score")

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
