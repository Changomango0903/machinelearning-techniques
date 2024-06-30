from scipy.spatial import distance

#calculate direct line from p1 to p2 (hypotenuse of triangle formed)
def euclidian_distance(p1, p2):
    distance = 0
    for i in range(len(p1)):
        distance += (p1[i] - p2[i]) ** 2
    return distance ** (1/2)

#calculate "legs" of path to p1, p2 (adjacent and opposite sides of triangle)
def manhattan_distance(p1, p2):
    distance = 0
    for i in range(len(p1)):
        distance += abs(p1[i] - p2[i])
    return distance

#calculate how many "dimensions" of each point are different
def hamming_distance(p1, p2):
    distance = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            distance += 1
    return distance

distance.euclidean([1, 2], [4, 0])
distance.cityblock([1, 2], [4, 0])
distance.hamming([5, 4, 9], [1, 7, 9])