#Gradient Descent technique for Intercept
#sum of all y_value - (slope * x_value + b)
#multiply sum by -2/number of points
#b is the current intercept guesss
def get_gradient_at_b(x, y, m, b):
  diff = 0
  for i in range(len(x)):
    diff += y[i] - (m*x[i]+b)
  b_gradient = (-2/len(x)) * diff
  return b_gradient

#Gradient Descent technique for Slope
#sum of all x_value * (y_value - (slope * x_value + b))
#multipy sum by -2/number of points
#m is the current slope guess
def get_gradient_at_m(x, y, m, b):
  diff = 0
  for i in range(len(x)):
    diff += x[i] * (y[i] - (m * x[i] + b))
  m_gradient = -2/len(x) * diff
  return m_gradient