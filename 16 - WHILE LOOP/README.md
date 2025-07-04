# 17. Guess Number  
## 🔄 While Loop

Now that we got a sneak peek of a `while` loop, let's see what it actually does!

A `while` loop looks very similar to an `if` statement.  
Just like an `if` statement, it executes the code **if the condition is `True`**.

However, the difference is that a `while` loop will **continue to execute the code inside of it**,  
over and over again, as long as the condition remains `True`.

---

### 🧱 Syntax:

```python
while condition:
  # code inside
```

So instead of executing once, it executes again and again **while** that condition is true.

---

### 🧪 Example:

```python
guess = 0

while guess != 6:
  guess = int(input('Guess the number: '))
```

This will run repeatedly until the user guesses the number 6:

```
Guess the number: 5  
Guess the number: 3  
Guess the number: 6
```

---

### 🔍 What’s Happening:

- Starts with `guess = 0`
- Checks: is `0 != 6`? ✅ → run inside
- Checks: is `5 != 6`? ✅ → run inside
- Checks: is `3 != 6`? ✅ → run inside
- Checks: is `6 != 6`? ❌ → loop ends

Once the condition is `False`, it exits the loop and skips the code inside.

> ⚠️ Note: If the condition is `False` from the start, the loop **won’t run at all**.

---

## 🎯 Instructions

Let’s build on the example above.

Create a file called `guess.py` and enter this code:

```python
guess = 0

while guess != 6:
  guess = int(input("Guess the number:  "))

print("You got it!")
```

Run it a few times to see how it works.

---

### 🧠 Challenge

Make it a **guessing game with limited tries**!

1. Add a variable `tries = 0` at the top  
2. Modify the `while` loop condition to check **both**:
   - guess is incorrect  
   - tries are within limit

Use a relational operator like `<` to control the number of attempts.

---

Source Credit: All content adapted from the [Codedex](https://www.codedex.io) website. A fun and unique way to learn programming languages — from basics to advanced! 💻✨ Thank you, Codedex! ❤️🔥
