# 15. Enter PIN  
## 🔁 Loop

In programming, a **loop** is used to repeat a block of code until a specified condition is satisfied.  
It's another incredibly powerful tool that's used a ton!

People will often use the generic term **“iterate”** when referring to loops;  
iterate simply means “to repeat”.

---

The first kind of loop that we are going to learn is the `while` loop.  
You can think of the `while` loop like a traffic circle:

🛞 Each lap is one iteration!  
🚗 A car will iterate over and over again until it can't do so anymore.

---

## 🏦 Instructions

Before we dive deep into `while` loops, let's see a demo using a bank's ATM.

Create a file called `enter_pin.py` and type in the following:

```python
print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')
```

---

### ▶️ Run and Test

Next, press the "Run" button to see the messages print to the terminal.

Try entering the following PINs in sequence:

1. `1111` → enter  
2. `2023` → enter  
3. `1991` → enter  
4. `1234` → enter  

---

💡 Were you able to get access to the ATM?

Source Credit: All content adapted from the [Codedex](https://www.codedex.io) website. A fun and unique way to learn programming languages — from basics to advanced! 💻✨ Thank you, Codedex! ❤️🔥
