


## Create Python virtual environment

```text
python3 -m venv ssdc
source ssdc/bin/activate
```

### Question 1

Run the following code:  `styleLint.py`

-   Question A: What happens when the code is run?
-   Question B: Can you modify this code for a more favorable outcome?
-   Question C: What amendments have you made to the code?

In this exercise, the code had indentation errors. After fixing indentation, I changed it for a more favorable out come by checking if the input an integer. 

```python
def factorial(n):
if n == 0:
return 1
else:
return n*factorial(n-1)
```
`solution1`
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Input a number to see the factorial : ")) #receive input from user as an int
print(factorial(n))
```

`solution2`
```python
from math import factorial

fac = factorial(n)
print(fac)
```

`solution3`
```python
def iter_factorial(n):
    factorial = 1
    n = input("Enter a number: ")  # c) Using recursion:
    factorial = 1
    if int(n) >= 1:
        for i in range(1, int(n) + 1):
            factorial = factorial * i
        return factorial


num = int(input("Enter the number: "))

print("factorial of ", num, " (iterative): ", end="")
```

### Question 2
- pip install pylint, then run pylint on  `pylintTest.py`
- Review each of the code errors returned. Can you correct each of the errors identified by pylint?  
```
codio@finish-promise:~/workspace$ pylint pylintTest.py 
No config file found, using default configuration
************* Module pylintTest
C:  5, 0: Trailing whitespace (trailing-whitespace)
W: 12, 0: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
W: 13, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
W: 14, 0: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
W: 15, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
W: 16, 0: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
W: 17, 0: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
C: 17, 0: Exactly one space required around assignment
      encoded=encoded + letters[x]
             ^ (bad-whitespace)
W: 18, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
W: 19, 0: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
W: 20, 0: Bad indentation. Found 8 spaces, expected 16 (bad-indentation)
W: 21, 0: Bad indentation. Found 12 spaces, expected 20 (bad-indentation)
W: 22, 0: Bad indentation. Found 8 spaces, expected 16 (bad-indentation)
W: 23, 0: Bad indentation. Found 10 spaces, expected 20 (bad-indentation)
W: 24, 0: Bad indentation. Found 10 spaces, expected 20 (bad-indentation)
C: 26, 0: Final newline missing (missing-final-newline)
C:  1, 0: Module name "pylintTest" doesn't conform to snake_case naming style (invalid-name)
C:  1, 0: Missing module docstring (missing-docstring)
C:  6, 0: Constant name "shift" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  7, 0: Constant name "choice" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  8, 0: Constant name "word" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  9, 0: Constant name "letters" doesn't conform to UPPER_CASE naming style (invalid-name)
C: 10, 0: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
W: 19, 6: Redefining name 'letter' from outer scope (line 12) (redefined-outer-name)

------------------------------------
Your code has been rated at -2.63/10
```
- Before correcting the code errors, save the pylintTest.py file with a new name (it will be needed again in the next question).

```
codio@finish-promise:~/workspace$ pylint pylintTest-correct.py
No config file found, using default configuration
************* Module pylintTest-correct
C: 28, 0: Final newline missing (missing-final-newline)
C: 28, 0: Unnecessary parens after 'print' keyword (superfluous-parens)
W:  6, 0: Redefining built-in 'raw_input' (redefined-builtin)
C:  1, 0: Module name "pylintTest-correct" doesn't conform to snake_case naming style (invalid-name)
E:  6, 0: Unable to import 'distlib.compat' (import-error)
C:  9, 0: Constant name "choice" doesn't conform to UPPER_CASE naming style (invalid-name)
C: 10, 0: Constant name "word" doesn't conform to UPPER_CASE naming style (invalid-name)
C: 11, 0: Constant name "letters" doesn't conform to UPPER_CASE naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 4.00/10 (previous run: 4.00/10, +0.00)

codio@finish-promise:~/workspace$ 
```

### Question 3

-   pip install flake8
-   Run flake8 on pylintTest.py
- Review the errors returned. In what way does this error message differ from the error message returned by pylint?  
```python
codio@finish-promise:~/workspace$ pylint pylintTest.py
No config file found, using default configuration
************* Module pylintTest
C:  5, 0: Trailing whitespace (trailing-whitespace)
W: 12, 0: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
W: 13, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
W: 14, 0: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
W: 15, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
W: 16, 0: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
W: 17, 0: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
C: 17, 0: Exactly one space required around assignment
      encoded=encoded + letters[x]
             ^ (bad-whitespace)
W: 18, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
W: 19, 0: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
W: 20, 0: Bad indentation. Found 8 spaces, expected 16 (bad-indentation)
W: 21, 0: Bad indentation. Found 12 spaces, expected 20 (bad-indentation)
W: 22, 0: Bad indentation. Found 8 spaces, expected 16 (bad-indentation)
W: 23, 0: Bad indentation. Found 10 spaces, expected 20 (bad-indentation)
W: 24, 0: Bad indentation. Found 10 spaces, expected 20 (bad-indentation)
C: 26, 0: Final newline missing (missing-final-newline)
C:  1, 0: Module name "pylintTest" doesn't conform to snake_case naming style (invalid-name)
C:  1, 0: Missing module docstring (missing-docstring)
C:  6, 0: Constant name "shift" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  7, 0: Constant name "choice" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  8, 0: Constant name "word" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  9, 0: Constant name "letters" doesn't conform to UPPER_CASE naming style (invalid-name)
C: 10, 0: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
W: 19, 6: Redefining name 'letter' from outer scope (line 12) (redefined-outer-name)

--------------------------------------------------------------------
Your code has been rated at -2.63/10 (previous run: -2.63/10, +0.00)

codio@finish-promise:~/workspace$ 
```

- Run flake8 on metricTest.py. Can you correct each of the errors returned by flake8? What amendments have you made to the code?
```python
pylintTest.py:5:1: W293 blank line contains whitespace
pylintTest.py:12:3: E111 indentation is not a multiple of 4
pylintTest.py:14:7: E111 indentation is not a multiple of 4
pylintTest.py:16:7: E111 indentation is not a multiple of 4
pylintTest.py:17:7: E111 indentation is not a multiple of 4
pylintTest.py:17:14: E225 missing whitespace around operator
pylintTest.py:19:7: E111 indentation is not a multiple of 4
pylintTest.py:23:11: E111 indentation is not a multiple of 4
pylintTest.py:24:11: E111 indentation is not a multiple of 4
pylintTest.py:26:14: W292 no newline at end of file
codio@finish-promise:~/workspace$ 
```

As you can see, PyLint performs a more detailed check than flake8. When comparing Pylint vs flake8, the  [Slant community](https://www.slant.co/versus/12630/12632/~pylint_vs_flake8)  recommends Pylint for most people. In the question“What are the best Python code linters?” Pylint is ranked 1st while flake8 is ranked 2nd. The most important reason people chose Pylint is: Pylint gives very detailed reports of your code. Pylint prefixes each of the problem areas with a R, C, W, E, or F, meaning:

-   [R]efactor for a “good practice” metric violation
-   [C]onvention for coding standard violation
-   [W]arning for stylistic problems, or minor programming issues
-   [E]rror for important programming issues (i.e. most probably bug)
-   [F]atal for errors which prevented further processing

```python
codio@finish-promise:~/workspace$ flake8 metric_test_pass.py 
metric_test_pass.py:15:80: E501 line too long (92 > 79 characters)
metric_test_pass.py:25:80: E501 line too long (84 > 79 characters)
metric_test_pass.py:29:80: E501 line too long (86 > 79 characters)
```

### Question 4
- This exercise requires to pip install mccabe checker
-  Question A: Run mccabe on sums.py What is the result?
```python
codio@finish-promise:~/workspace$ pip install pytest-mccabe
Collecting pytest-mccabe
  Downloading https://files.pythonhosted.org/packages/54/97/052f65a1b55131f4f3b7c028cd31fe5ec4acff296c33e9bfe17bddc5f129/pytest_mccabe-2.0-py2.py3-none-any.whl
Collecting pytest>=5.4.0 (from pytest-mccabe)
  Could not find a version that satisfies the requirement pytest>=5.4.0 (from pytest-mccabe) (from versions: 2.0.0, 2.0.1, 2.0.2, 2.0.3, 2.1.0, 2.1.1, 2.1.2, 2.1.3, 2.2.0, 2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.3.0, 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.4.0, 2.4.1, 2.4.2, 2.5.0, 2.5.1, 2.5.2, 2.6.0, 2.6.1, 2.6.2, 2.6.3, 2.6.4, 2.7.0, 2.7.1, 2.7.2, 2.7.3, 2.8.0, 2.8.1, 2.8.2, 2.8.3, 2.8.4, 2.8.5, 2.8.6, 2.8.7, 2.9.0, 2.9.1, 2.9.2, 3.0.0, 3.0.1, 3.0.2, 3.0.3, 3.0.4, 3.0.5, 3.0.6, 3.0.7, 3.1.0, 3.1.1, 3.1.2, 3.1.3, 3.2.0, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.5, 3.3.0, 3.3.1, 3.3.2, 3.4.0, 3.4.1, 3.4.2, 3.5.0, 3.5.1, 3.6.0, 3.6.1, 3.6.2, 3.6.3, 3.6.4, 3.7.0, 3.7.1, 3.7.2, 3.7.3, 3.7.4, 3.8.0, 3.8.1, 3.8.2, 3.9.1, 3.9.2, 3.9.3, 3.10.0, 3.10.1, 4.0.0, 4.0.1, 4.0.2, 4.1.0, 4.1.1, 4.2.0, 4.2.1, 4.3.0, 4.3.1, 4.4.0, 4.4.1, 4.4.2, 4.5.0, 4.6.0, 4.6.1, 4.6.2, 4.6.3, 4.6.4, 4.6.5, 4.6.6, 4.6.7, 4.6.8, 4.6.9, 4.6.10, 4.6.11)
No matching distribution found for pytest>=5.4.0 (from pytest-mccabe)
```

-  Question A: Run mccabe on  sums2.py

-  Question C: What are the contributors to the cyclomatic complexity in each piece of code?


