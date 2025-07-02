# Nested If Statements  
## 🧠 Syntax

As our program gets longer and more complex, so does the decision-making of our code.  
You might've already run into situations where you want to check for **another condition** after a condition is true.

You know what else we can do with `if`/`elif`/`else` statements?

We can **nest them inside one another!** 🪹

A **nested if statement** is an `if` statement inside another `if` statement.

---

### Example 1

Suppose we have a simple `if`/`else` statement:

```python
if age >= 18:
  print('You are old enough to apply for a loan.')
else:
  print('You are too young to apply for a loan.')
```

Let's add another `if`/`else` statement **nested inside** the outer `if` statement:

```python
if age >= 18:
  if income >= 20000:
    print('You are eligible for a loan.')
  else:
    print('Your income is too low to be eligible for a loan.')
else:
  print('You are too young to apply for a loan.')
```

In Python, **indentation** is the only way to determine the nesting level.  
Because lines 2–5 are indented more, they're inside the outer `if` statement.

---

> ⚠️ Note: Avoid nesting too deeply (more than 2–3 levels),  
> as it makes your code harder to read and maintain.

---

## 🌦️ Example 2

Here’s another program using nested control flow:

```python
weather = 'Sunny'
humidity = 35

if weather == 'Sunny':
  if humidity < 60:
    print('Let’s go to the beach! 🏖️')
  else:
    print('Hmmm, it’s a little humid for a beach day.')
else:
  print('It’s not sunny today... let’s try for another day.')
```

### Output:

```
Let’s go to the beach! 🏖️
```

If `humidity` is 65, the output would be:

```
Hmmm, it’s a little humid for a beach day.
```

---

Now you can add **layers of decision-making** to your Python programs! 🎯
