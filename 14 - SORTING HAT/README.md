
# 16. Sorting Hat

## 🎉 Congrats!

Here's a recap of everything we learned so far:

- **Control flow** is the order in which the program's code executes.
- `if` statement tests a condition for truth and executes the code if it's `True`.
- `elif` clause can be added between `if` and `else`.
- `else` executes the code if none of the above is `True`.
- **Relational operators** are used to compare two values: `==`, `!=`, `>`, `>=`, `<`, `<=`.
- **Logical operators** are used to combine two or more conditions: `and`, `or`, `not`.

Here's an `if/elif/else` statement in action just in case:

```python
if review >= 4.5:
  print('Extraordinary')
elif review >= 4:
  print('Excellent')
elif review >= 3:
  print('Good')
else:
  print('Eh')
```

---

## 🧙‍♂️ Instructions

The **Sorting Hat** is a magical talking hat at Hogwarts School of Witchcraft and Wizardry.  
The hat decides which of the four "Houses" each first-year student goes to:

- 🦁 Gryffindor
- 🦅 Ravenclaw
- 🦡 Hufflepuff
- 🐍 Slytherin

---

### Your Task

Write a program that asks the user some questions using the `int()` and `input()` functions:

---

**Q1) Do you like Dawn or Dusk?**  
1) Dawn  
2) Dusk

- If answer is `1`, Gryffindor and Ravenclaw both get a +1.  
- Else if answer is `2`, Hufflepuff and Slytherin both get a +1.  
- Else, output the message `"Wrong input."`

---

**Q2) When I’m dead, I want people to remember me as:**  
1) The Good  
2) The Great  
3) The Wise  
4) The Bold

- If answer is `1`, Hufflepuff +2  
- If answer is `2`, Slytherin +2  
- If answer is `3`, Ravenclaw +2  
- If answer is `4`, Gryffindor +2  
- Else, output the message `"Wrong input."`

---

**Q3) Which kind of instrument most pleases your ear?**  
1) The violin  
2) The trumpet  
3) The piano  
4) The drum

- If answer is `1`, Slytherin +4  
- If answer is `2`, Hufflepuff +4  
- If answer is `3`, Ravenclaw +4  
- If answer is `4`, Gryffindor +4  
- Else, output `"Wrong input."`

---

### 🧮 Final Step

Print out the **score** for each house.

---

### ⭐ Bonus

If you want to go further, see if you can figure out how to print out the **house with the most points**!

---

Source Credit: All content adapted from the [Codedex](https://www.codedex.io) website. A fun and unique way to learn programming languages — from basics to advanced! 💻✨ Thank you, Codedex! ❤️🔥
