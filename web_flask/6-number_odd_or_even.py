#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def disp_c(text):
    """Display 'C' followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def disp_python(text="is cool"):
    """Display 'Python' followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def disp_num(n):
    """Displays 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page if n is even|odd"""
    if n % 2 != 0:
        num = "odd"
    else:
        num = "even"
    return render_template("6-number_odd_or_even.html", n=n, num=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
