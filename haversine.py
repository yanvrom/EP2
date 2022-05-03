import math
def haversine(raio, fi1, lamb1, fi2, lamb2):
    fi1 = math.radians(fi1)
    fi2 = math.radians(fi2)
    lamb1 = math.radians(lamb1)
    lamb2 = math.radians(lamb2)
    a = (math.sin((fi2-fi1)/2))**2
    b = math.cos(fi1)*math.cos(fi2)*(math.sin((lamb2-lamb1)/2))**2
    d = 2*raio*math.asin(math.sqrt(a + b))
    return d