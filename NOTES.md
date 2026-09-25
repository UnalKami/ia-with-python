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

- Package: As many project created with Python, we can use Package like *requests, pandas, numpy, openai, beatifulsoup4*. To install all of these, we use pip as our Python's package manager

## Interative Python

Dave show a package named ipykernel that run Python code in a interactive window that looks like a Jypiter Notebook. (It works with shift + enter)

# REFERENCES

1. Python for AI - Full Beginner Course by Dave Ebbelaar: https://www.youtube.com/watch?v=ygXn5nV5qFc
2. Handbook: https://python.datalumina.com/?utm_source=youtube&utm_medium=video&utm_campaign=python-evergreen&utm_content=python-for-ai-full-course-description&dub_id=LU43elHjlYSfaVTO 