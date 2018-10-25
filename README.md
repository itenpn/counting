# Counting.py
Author: Nicholas Iten  
Date: 2018-10-25  
Purpose: To count from 1 to 1 million on the Hack Club Slack  

## Why Python?
Python is an incredibly useful language for nearly all development. 
If you need something to get done, python probably already has a module 
available to complete your task. This makes it a powerful language for
scripting because of the wide array of options available to you. In my
case, I needed a way to convert numbers into specific keyboard inputs.
This lead me down the path of Google, where I found out about a new module
```python
from pyautogui import press
```

## Program Logic
First we need to understand how `pyautogui` accepts input. The function I called,
`press` takes in a string input, however, I have numbers that do not correspond with
a single keyboard entry. Since my domain of possible numbers is from 1 to 1E+6, I needed
to convert an integer value into separate string inputs. It's a good idea to map out what
we plan on doing before we write down some code. Let's try to understand the process we are trying
to accomplish.

Example 1.1: `2018`

This number is given to my program as an integer with a value of 2018. 
Before I get this input, I know that 2017 will pop up and afterwards 2019 will appear.
So it might be useful to physically count up in value instead of manually trying to separate
the integer. Let's look at the series I just described.

Example 1.2: `2017, 2018, 2019, 2020`

Looking at these values, I know that the tens place is changing by one, until it hits 9,
then it changes back to 0, and the tens place after it is incremented. So we know that our
program must follow some sort of logic that will make the position 0, and let the position before it increment.
But what if this occured?

Example 1.3: `298, 299, 300`

Two different positions changed in one go, this means I have to nest these tests in order to make sure that I
account for the fact that any of these could change. This is crucial information for our program. I know that
this structure is probably going to look something like this.

```python
if pos1 == 9:
  pos1 = 0
  if pos2 == 9:
    pos2 = 0
    //continue the nesting
  else:
    pos2 += 1
else:
  pos1 += 1
```

Another important aspect about the problem is that we are actually counting.
Whenever I have a task to repeat over and over again, it is important that
we use a loop to help simplify our code. Since we have a definite begining and
closing, let's use a for loop, which is perfect for our problem!

```python
for i in range(1, 1000001):
  //code
```

If you don't know, python does for loops by going through the index of an array. 
`range(1, 1000001)` creates an array of values of every integer between 1 and 1 million.
i then becomes any number on that array, so it starts as 1, then 2, and so forth.

As of right now, our code will look something like this:

```python
from pyautogui import press
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
for i in range(start, 1000001):
    if f == 9:
        if e == 9:
            e = 0
            if d == 9:
                d = 0
                if c == 9:
                    c = 0
                    if b == 9:
                        b = 0
                        a += 1
                    else:
                        b += 1
                else:
                    c +=1
            else:
                d += 1
        else:
            e += 1
```
