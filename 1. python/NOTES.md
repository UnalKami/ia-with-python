# SETUP

## Install or update Python

In my case, I already had Python 3.12.3 installed, but for this course I upgraded to Python 3.13, the same version as Dave.

For that I going to use a virtual enviroment, using this scripts:

```
# Creating a new venv
python3.13 -m venv .venv

# Activate it
source .venv/bin/activate

# Check Python version
python --version
```

I also create a requirements.txt file to have all Package use in this repository, so you can easily install using:

```
# Install all packages we need in the project
pip install -r requirements.txt
```

## VScode 

For this project I'm using this extesion in my VSCode setup:

1. Python by Microsoft.
2. Pylance by Microsft.
3. Jupyter ny Microsoft.

## Setup Python in VScode

Remmeber choose the correct Python version that Visual Studio Code will use.

# Start With Python

## Basic concepts

- Package: As many project created with Python, we can use Package like *requests, pandas, numpy, openai, beatifulsoup4*. To install all of these, we use pip as our Python's package manager.
- snake_case: Standard way to name variables in Python using lowercase with underscores between words.
- Comments: IN PYTHON WE CAN COMMENT USING # TO COMMENT ONLY ONE LINE AND TRIPLE QUOTES TO COMMENT MULTIPLE LINES.
- Python as calculator: Python works literally like an calculator so we can write numbers with operators and get the answer

## Interative Python

Dave show a package named ipykernel that run Python code in a interactive window that looks like a Jypiter Notebook. (It works with shift + enter)

## Variables

We save data into varibles. We can set a value and modify it. 
```
# Update a value in a variable
number = 1
number += 2
print(number)  # number storage 3
```

## Data Types

As other languages, we have diferent kinds of information in Python so lets remember all very quickly:

1. Numbers: Can be integers (int) or floats (float). The main difference between both type of data is how are storage in memory.
2. Strings: Those are chains of characters write inside quotes. Python doesn't care if are simple or double quotes.
3. Booleans: Logical data that can be True o False.


# REFERENCES

1. Python for AI - Full Beginner Course by Dave Ebbelaar: https://www.youtube.com/watch?v=ygXn5nV5qFc
2. Handbook: https://python.datalumina.com/?utm_source=youtube&utm_medium=video&utm_campaign=python-evergreen&utm_content=python-for-ai-full-course-description&dub_id=LU43elHjlYSfaVTO 