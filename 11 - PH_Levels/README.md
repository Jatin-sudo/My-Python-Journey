
# 11. pH Levels

## 🧪 Relational Operators

Relational operators are used to compare two values in a condition:

| Operator | Meaning                  |
|----------|---------------------------|
| `==`     | Equal to                  |
| `!=`     | Not equal to              |
| `>`      | Greater than              |
| `<`      | Less than                 |
| `>=`     | Greater than or equal to  |
| `<=`     | Less than or equal to     |

---

## 🔄 Elif (Else If)

When more than two conditions are needed, use `elif` to add intermediate checks:

```python
if grade > 90:
  print('A')
elif grade > 80:
  print('B')
elif grade > 70:
  print('C')
elif grade > 60:
  print('D')
else:
  print('F')
```

> ⚠️ Note: Only **one** of these blocks will run—the **first one** that matches.

---

## 🧪 Instructions

In chemistry, **pH** is a scale used to specify the **acidity** or **basicity** of a liquid.

### ✅ Create a `ph_levels.py` program that:

1. Asks the user for a pH level between `0` and `14`.
2. Stores the value in a variable named `ph`.
3. Uses an `if/elif/else` statement to determine:

- If `ph > 7`, print `"Basic"`.
- If `ph < 7`, print `"Acidic"`.
- Else, print `"Neutral"`.

---


Test your program by running it with different values like `3`, `7`, and `11` to ensure all conditions work!

Source Credit: All content adapted from the [Codedex](https://www.codedex.io) website. A fun and unique way to learn programming languages — from basics to advanced! 💻✨ This website has genuinely helped me a lot. Thank you, Codedex! ❤️🔥
