# mock-python 🐍

Welcome to **mock-python**, a beginner-friendly Python challenge!  
Your goal: complete the exercises in `main.py`, run the tests in `test_main.py`, and submit a pull request so we can see your progress.

---

## 📚 Exercises Overview

1. **Add Numbers**  
   Function: `add_numbers(a, b)`  
   Returns the sum of two numbers.  
   **Example:** `add_numbers(2, 3) -> 5`

2. **Subtract Numbers**  
   Function: `subtract_numbers(a, b)`  
   Returns the result of a minus b.  
   **Example:** `subtract_numbers(5, 3) -> 2`

3. **FruitLoop**  
   Function: `fruitloop(n)`  
   Prints numbers from 1 to n:  
   - Multiples of 3 → "Fruit"  
   - Multiples of 5 → "Loop"  
   - Multiples of both 3 and 5 → "FruitLoop"  
   **Example:** `fruitloop(5)` prints:

1
2
Fruit
4
Loop


4. **Fibonacci**  
Function: `fibonacci(n)`  
Returns the nth Fibonacci number (0-indexed).  
**Example:** `fibonacci(5) -> 5`

5. **Find Maximum**  
Function: `find_max(numbers)`  
Returns the largest number in a list.  
**Example:** `find_max([1,2,3]) -> 3`

6. **Find Minimum**  
Function: `find_min(numbers)`  
Returns the smallest number in a list.  
**Example:** `find_min([1,2,3]) -> 1`

7. **Person Class**  
Class: `Person`  
- Attributes: `name` (str), `age` (int)  
- Method: `greet()` → returns `"Hello, my name is {name} and I am {age} years old."`  
**Example:**
```python
p = Person("Alice", 25)
p.greet()  # "Hello, my name is Alice and I am 25 years old."



**⚡ How to Run Locally**
1. Clone your fork

git clone https://github.com/YOUR_USERNAME/mock-python.git
cd mock-python

2. Complete the exercises

Edit main.py and implement the required functions.
3. Run the tests

Using Python's built-in unittest:

python3 -m unittest test_main.py 

Or using pytest (optional, cleaner output):

pip install pytest
pytest -v


🏆 Tips

    Only edit main.py. Do not touch test_main.py.

    Run the tests locally before submitting a PR.

    Debugging is part of the fun — try different approaches and see what works!