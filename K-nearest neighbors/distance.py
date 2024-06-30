#calculate direct line from p1 to p2 (hypotenuse of triangle formed)
def euclidian_distance(p1, p2):
    distance = 0
    for i in range(len(p1)):
        distance += (p1[i] - p2[i]) ** 2
    return distance ** (1/2)
