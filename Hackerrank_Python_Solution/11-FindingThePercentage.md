# Finding The Percentage

## Problem
The provided code stub is read in a dictionary containing key/value pairs of name:[Marks] for a list of students. Print the average of the marks array for the student name is provided, showing 2 places after the decimal.

## Example
marks key: value pairs are
‘alpha’:[20, 30, 40]
‘beta’:[30, 50, 70]
query_name = ‘beta’

The query_name is ‘beta’. beta’s average score is (30 + 50 + 70)/3 = 50.0.

## Input Format
The first line contains the integer n, the number of student records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

## Constraints
-2 ≤ n ≤ 10
-0 ≤ marks[i] ≤ 100
-length of the marks array = 3

## Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

## Sample Input 0
```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

## Sample Output 0
```
56.00
```

## Explanation 0
Marks of Malika are {52, 56, 60} whose average is (52 +56 +60)/3 ⇒  56

## Sample Input 1
```
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
```

## Sample Output 1
```
26.50
```

## Solution
``` python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    z=0
    count=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=student_marks.get(query_name,[])
    if marks:
        total=sum(marks)
        count=len(marks)
        average=total/count
        formatted_average=f"{average:.2f}"
    print(formatted_average)
```

## Explanation 

## Access Scores:
marks= students_scores.get(query_name, []) retrieves the list of scores for the key stored in query_name. If that key is not in the dictionary, it returns an empty list.
## Check for Scores:
Ensure that scores is not empty before proceeding with calculations.
## Calculate Total Sum, Number of Scores, and Average:
- **Sum of Scores**:
total = sum(marks) calculates the sum of the list.

- **count**:
count= len(marks) finds out how many scores there are.

- **Calculate the Average**:
average = total / count computes the average.

## Output:
The print statements display the scores, sum, and average, with the average formatted to two decimal places.


