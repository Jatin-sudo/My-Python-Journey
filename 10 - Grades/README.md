
# 10. Grades

## 🧠 If Statement

An `if` statement is used to test a condition for truth:

- If the condition evaluates to `True`, the code inside the `if` block is executed.
- If the condition evaluates to `False`, that block is skipped.

```python
if condition:
  # code inside
```

### Example:

```python
grade = 70

if grade > 60:
  print("You passed!")
```

> 📌 The code inside the `if` block must be indented (usually 2 or 4 spaces).

---

## 🙈 Else Clause

You can optionally add an `else` clause to handle the opposite case:

```python
if grade > 60:
  print("You passed.")
else:
  print("You failed.")
```

This way:

- If the condition is `True`, the first block runs.
- If it’s `False`, the `else` block runs.

---

## 🎯 Instructions

Holy moly! 😭  
Because the class average was **super low** on the test, the teacher added a curve for the grades!

Your task is to:

### ✅ Build a `grades.py` program that:

1. Creates a variable `grade` and assigns it a value from **0 to 100**.
2. Checks whether the grade is **above or below 55** using an `if/else` statement.
3. Prints:
   - `"You passed."` if grade is **greater than or equal to 55**
   - `"You failed."` otherwise

---

Try modifying the value of `grade` and rerun the code to test all outcomes!

Source Credit: All content adapted from the [Codedex](https://www.codedex.io) website. A fun and unique way to learn programming languages — from basics to advanced! 💻✨ This website has genuinely helped me a lot. Thank you, Codedex! ❤️🔥
