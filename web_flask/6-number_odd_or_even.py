#!/usr/bin/python3
"""Flask Web Application

This script starts a Flask web application that listens on 0.0.0.0, port 5000.
The application defines several routes:

Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C ' followed by the value of the <text> variable.
    /python/(<text>): Displays 'Python ' followed by the value of the <text> variable.
    /number/<int:n>: Displays '<n> is a number' only if <n> is an integer.
    /number_template/<int:n>: Displays an HTML page showing '<n>' only if <n> is an integer.
    /number_odd_or_even/<int:n>: Displays an HTML page showing whether <n> is odd or even only if <n> is an integer.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Route to display 'Hello HBNB!'.

    Returns:
        str: 'Hello HBNB!'
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route to display 'HBNB'.

    Returns:
        str: 'HBNB'
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """
    Route to display 'C ' followed by the value of the <text> variable.
    Replaces underscores '_' with spaces ' '.

    Args:
        text (str): The text to display after 'C '.

    Returns:
        str: 'C ' followed by the text with underscores replaced by spaces.
    """
    return "C {}".format(text.replace("_", " "))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """
    Route to display 'Python ' followed by the value of the <text> variable.
    The default value for <text> is 'is cool'.
    Replaces underscores '_' with spaces ' '.

    Args:
        text (str, optional): The text to display after 'Python '. Defaults to 'is cool'.

    Returns:
        str: 'Python ' followed by the text with underscores replaced by spaces.
    """
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """
    Route to display '<n> is a number' only if <n> is an integer.

    Args:
        n (int): The number to display.

    Returns:
        str: The number followed by 'is a number'.
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route to display an HTML page showing 'Number: <n>' only if <n> is an integer.
    Uses the '5-number.html' template.

    Args:
        n (int): The number to display in the HTML page.

    Returns:
        str: Rendered HTML page displaying the number.
    """
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route to display an HTML page showing whether <n> is odd or even only if <n> is an integer.
    Uses the '6-number_odd_or_even.html' template.

    Args:
        n (int): The number to check and display in the HTML page.

    Returns:
        str: Rendered HTML page displaying whether the number is odd or even.
    """
    eo = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, eo=eo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

