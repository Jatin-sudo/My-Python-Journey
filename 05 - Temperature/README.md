# 05. Temperature

## Operators

Computers are incredible at doing math calculations. Now that we have learned about variables, let's use them with arithmetic operators to calculate things! 🔢

Python has the following arithmetic operators:

- `+` Addition  
- `-` Subtraction  
- `*` Multiplication  
- `/` Division  
- `%` Modulo (returns the remainder)

### Examples:

```python
score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1

print(score)        # Output: 1
```

### Tip Calculator Example:

```python
pizza = 2.99
coke = 0.99

total = pizza + coke
tip = total * 0.2

print(tip)  # Output: 0.796
```

Another way using parentheses:

```python
tip = (pizza + coke) * 0.2
```

🧠 **Note**: In Python, parentheses have the highest order of operations.

---

## Instructions

Create a `temperature.py` program that converts a number from Fahrenheit (°F) to Celsius (°C).

1. Google the current temperature of Brooklyn, NY (in °F).
2. Use this formula in Python:

```python
Celsius = (Fahrenheit - 32) / 1.8
```

3. Print out the converted temperature. 🌡️

---
Source Credit: All content adapted from the Codedex website. A fun and unique way to learn programming languages — from basics to advanced! 💻✨ This website has genuinely helped me a lot. If I ever become something or achieve something great in life, a huge part of that credit will go to this platform. Thank you, Codedex! ❤️🔥
