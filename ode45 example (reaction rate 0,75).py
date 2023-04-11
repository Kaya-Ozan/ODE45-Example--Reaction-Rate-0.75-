import numpy as np
from scipy.integrate import solve_ivp
from bokeh.plotting import figure, show
from bokeh.io import output_file

def reaction_rates(t, y, k):
    rate = -k * y ** 0.75
    return rate

# Parametreleri tanımlayın
A0 = 1.0  # mol/L
k = 0.5  # L^(0.25)/(mol^(0.25)*s)
t_span = (0, 10)
initial_conditions = [A0]

# ODE çözümünü elde etmek için solve_ivp fonksiyonunu kullanın
sol = solve_ivp(reaction_rates, t_span, initial_conditions, args=(k,), dense_output=True)

# Zaman aralığını ve çözümü oluşturun
t_values = np.linspace(t_span[0], t_span[1], 500)
y_values = sol.sol(t_values)[0]

# Grafiği oluşturun
output_file("fractional_order_reaction.html")
p = figure(title="0.75 Order Reaction", x_axis_label="Time (s)", y_axis_label="Concentration [A] (mol/L)")
p.line(t_values, y_values, line_width=2)

# Grafiği gösterin
show(p)