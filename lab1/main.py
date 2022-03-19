import numpy as np

import tema1
from tema1 import get_u
from decimal import Decimal
from tema1 import numere_inmultite_non_asociative
import plotly.graph_objects as go


def problema1():
    u = get_u()
    print(f"Precizia masina este {u}")
    return u


def problema2():
    a = 1.0
    u = problema1()
    b = u / 10
    c = u / 10
    s1 = (Decimal(a) + Decimal(b)) + Decimal(c)
    s2 = Decimal(a) + (Decimal(b) + Decimal(c))
    if s1 != s2:
        print("Operatia de adunare data este asociativa.")
    else:
        print("Operatia de adunare data nu este asociativa.")
    x = numere_inmultite_non_asociative()
    return x


problema2()


def show_plot_sin():
    x = np.linspace(-10, 10, 1000)
    y = [tema1.sin_coef(x_value) for x_value in x]
    x = np.array(x)
    y = np.array(y)

    fig = go.Figure(data=go.Scatter(x=x, y=y, name="polynomial approx method"))
    y = [np.sin(x_value) for x_value in x]
    fig.add_trace(go.Scatter(x=x, y=y, name="numpy sin method"))
    fig.show()


def show_plot_cos():
    x = np.linspace(-10, 10, 100)

    y = [tema1.cos_coef(x_value) for x_value in x]
    fig = go.Figure(data=go.Scatter(x=x, y=y, name="polynomial approx method"))

    y = [np.cos(x_value) for x_value in x]
    fig.add_trace(go.Scatter(x=x, y=y, name="numpy cos method"))
    fig.show()


def show_plot_ln():
    x = np.linspace(0.01, 100, 1000)

    y = [tema1.coef_ln(x_value) for x_value in x]
    fig = go.Figure(data=go.Scatter(x=x, y=y, name="polynomial approx method"))

    y = [np.log(x_value) for x_value in x]
    fig.add_trace(go.Scatter(x=x, y=y, name="numpy ln method"))
    fig.show()


show_plot_sin()
show_plot_cos()
show_plot_ln()
