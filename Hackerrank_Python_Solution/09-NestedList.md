# Nested List

## Problem
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

## Example
records  = [[ “chi”, 20.0]], [“beta”, 50.0], [“alpha”, 50.0]
The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score: [“beta”, “alpha”]. Ordered alphabetically, the names are printed as:

```
alpha
beta
```
## Input Format
The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

## Constraints
-2<=N<=5
-There will always be one or more students having the second lowest grade.

## Output Format
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

```
Sample Input0:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```
```
Sample Output0:
Berry
Harry
```
### Explanation0:
There are 5 students in this class whose names and grades are assembled to build the following list:
python students = [[‘Harry’, 37.21], [‘Berry’, 37.21], [‘Tina’, 37.2], [‘Akriti’, 41], [‘Harsh’, 39]]
The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

## Solution

```python
if __name__ == '__main__':
    Name=[]
    Score=[]
    for _ in range(int(input())):
        name = input()
        Name.append(name)
        score = float(input())
        Score.append(score)
    records=[[name, score] for name, score in zip(Name, Score)]
    Scores=[record[1] for record in records]
    unique_score=sorted(set(Scores))
    Second_lowest_score=unique_score[1]
    Student_with_second_lowest=sorted([record[0] for record in records if record[1]==Second_lowest_score])
    for students in Student_with_second_lowest:
        print(students)
```
#### EXPLANATION:
- `zip(Name, Score)`:<br>
Uses zip() to pair each name with its corresponding score.<br>
Creates a list of lists, like:<br>
 [[‘Harry’, 37.21], [‘Berry’, 37.21], [‘Tina’, 37.2], [‘Akriti’, 41], [‘Harsh’, 39]]

- `[record[1] for record in records]`: <br>
This pulls out only the scores from records.<br>
<B>NOTE:</B>
if we use (record[1] for record in records) this will works as a generator.means That works the first time we iterate over it,
❌ But if we try to reuse Scores after that, it would be empty, because generators can be exhausted.
```PYTHON
Scores = (record[1] for record in records)
print(list(Scores))  # Works ✅
print(list(Scores))  # Empty ❌
```

- `for _ in range(int(input())): `<br>
Asks the user how many students they want to enter (e.g., 3), and loops that many times.<br> _ is a placeholder variable when the loop variable itself isn’t used.








