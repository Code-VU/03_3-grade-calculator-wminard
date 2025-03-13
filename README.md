[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18675096&assignment_repo_type=AssignmentRepo)
# Assignment
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print the error message: `Bad score`. 

If the score is between 0.0 and 1.0, print a grade using the following table:


```
 Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F
```

## Starting Code
```python
def calculateGrade():
    print("Calculating Grade")

    hrs = float(input("Enter score:"))

if __name__ == "__main__":
    calculateGrade()
```

## Desired Output
```bash
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
```

## Testing
Run the program repeatedly as shown above to test the various different values for input.

When you feel like it is complete, run Pytest. 8/8 tests should pass. 
