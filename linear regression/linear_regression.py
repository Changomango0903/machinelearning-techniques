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

