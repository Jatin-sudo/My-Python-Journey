# 06. BMI

## Exponents

Python can also perform exponentiation such as `2³` or `10²`.

In written math, we might see an exponent as a superscript number (like above), but typing superscripts isn't always easy on modern keyboards. Since exponentiation is super similar to multiplication, Python uses the notation `**`.

So `2 ** 3` is `2³` and `10 ** 2` is `10²`.

### Examples:

```python
score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
score = 2 ** 5      # score is now 32

print(score)        # Output: 32
```

---

## Instructions

The Body Mass Index (BMI) was created by a Belgian mathematician in the 1850s. It's used by health and nutrition professionals to estimate human body fat in certain populations.

It is computed by taking an individual's weight (mass) in kilograms and dividing it by the square of their height in meters:

```python
bmi = mass / (height ** 2)
```

### Task:

Create a `bmi.py` program that calculates your own BMI.

---
Source Credit: All content adapted from the Codedex website. A fun and unique way to learn programming languages — from basics to advanced! 💻✨ This website has genuinely helped me a lot. If I ever become something or achieve something great in life, a huge part of that credit will go to this platform. Thank you, Codedex! ❤️🔥
```

> 💡 FUN FACT: BMI is an archaic and oversimplified way to measure personal health. It was created by a mathematician – not a doctor!
