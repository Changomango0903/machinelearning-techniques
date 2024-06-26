import matplotlib.pyplot as plt
#Gradient Descent technique for Intercept
#sum of all y_value - (slope * x_value + b)
#multiply sum by -2/number of points
#b is the current intercept guesss
def get_gradient_at_b(x, y, b, m):
  diff = 0
  for i in range(len(x)):
    diff += y[i] - (m*x[i]+b)
  b_gradient = (-2/len(x)) * diff
  return b_gradient

#Gradient Descent technique for Slope
#sum of all x_value * (y_value - (slope * x_value + b))
#multipy sum by -2/number of points
#m is the current slope guess
def get_gradient_at_m(x, y, b, m):
  diff = 0
  for i in range(len(x)):
    diff += x[i] * (y[i] - (m * x[i] + b))
  m_gradient = -2/len(x) * diff
  return m_gradient

#Step gradient alters the current values of b and m by a factor of the LR (learning rate)
#the formula is usually x = current_x - (LR * gradient_x)
def step_gradient(x, y, b_current, m_current, learning_rate):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (learning_rate * b_gradient)
  m = m_current - (learning_rate * m_gradient)
  return (b, m)

def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0
  for i in range(num_iterations):
    b, m = step_gradient(x, y, b, m, learning_rate)
  return [b, m]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#Uncomment the line below to run your gradient_descent function
b, m = gradient_descent(months, revenue, 0.01, 1000)

#Uncomment the lines below to see the line you've settled upon!
y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()