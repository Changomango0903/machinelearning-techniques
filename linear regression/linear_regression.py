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

#Step gradient alters the current values of b and m by a factor of the LR (learning rate)
#the formula is usually x = current_x - (LR * gradient_x)
def step_gradient(x, y, b_current, m_current):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (0.01 * b_gradient)
  m = m_current - (0.01 * m_gradient)
  return (b, m)