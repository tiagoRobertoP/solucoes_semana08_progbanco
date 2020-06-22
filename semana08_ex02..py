import random
from collections import Counter
import matplotlib.pyplot as plt
import math

heigth_weight_age = [170, 70, 40]

grades = [95, 80, 75, 62]

# resultante[i] = a[i] + b[i]
# v = [1, 2, 3]
# w = [10, 20, 30]
# zip (v, w) = [(1, 10), (2, 20), (3, 30)]
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_add_test():
    v = [1, 7]
    w = [5, 4]
    r = vector_add(v, w)
    print(r)


# v = [2, 4, 6]
# w = [1, 1, 2]
# resultante = [1, 3, 4]
def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_subtract_test():
    v = [1, 7]
    w = [5, 4]
    r = vector_subtract(v, w)
    print(r)


def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


def vector_sum_test():
    v1 = [1, 2, 5, 6]
    v2 = [4, 3, 2, 1]
    v3 = [1, 1, 1, 1]
    r = vector_sum([v1, v2, v3])
    print(r)


# v = [2, 4, 3, 1]
# valor = 5
# resultante = [10, 20, 15, 5]
# resultante[i] = v[i] * valor


def scalar_multiply(c, v):
    return [c * v_i for v_i in v]


def scalar_multiply_test():
    c = 5
    v = [2, 4, 3, 1]
    r = scalar_multiply(c, v)
    print(r)


# v1 = [2 4, 5]
# v2 = [1, 2, 3]
# v3 = [3, 3, 1]
# resultante = [2, 3, 3]
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply((1 / n), vector_sum(vectors))


def vector_mean_test():
    v1 = [1, 2, 5, 6]
    v2 = [4, 3, 2, 1]
    v3 = [1, 1, 1, 1]
    r = vector_mean([v1, v2, v3])
    print(r)


# v = [1, 2, 3]
# w = [4, 2, 2]
# v dot w = 1x4 + 2x2 + 3x2 = 4 + 4 + 6 = 14


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def dot_test():
    v = [1, 2, 3]
    w = [4, 2, 2]
    r = dot(v, w)
    print(r)


# v = [1, 2]
# quero calcular v * v = [1, 4] => 5


def sum_of_squares(v):
    return dot(v, v)


def sum_of_squares_test():
    v = [1, 2, 3]
    r = sum_of_squares(v)
    print(r)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def magnitude_test():
    v = [1, 2, 3]
    r = magnitude(v)
    print(r)


def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    return math.sqrt(squared_distance(v, w))


# atalho
# def distance(v, w):
#    return magnitude(vector_subtract(v, w))


def distance_test():
    v1 = [27, 80, 180]
    v2 = [58, 100, 198]
    v3 = [29, 79, 179]
    print(f"dist(v1, v2): {distance(v1, v2)}")
    print(f"dist(v1, v3): {distance(v1, v3)}")
    print(f"dist(v2, v3): {distance(v2, v3)}")


def qtde_amigos_minutos_passados():
    return ([1, 10, 50, 2, 150], [5, 200, 350, 17, 1])


def variance(v):
    mean = sum(v) / len(v)
    return [v_i - mean for v_i in v]


def variance_test():
    v = [1, 2, 3]
    r = variance(v)
    print(r)


x = [1, 2, 3]
y = [1, 2, 3]


def covariance(x, y):
    n = len(x)
    return dot(variance(x), variance(y)) / (n - 1)


def covariance_test():
    # teste 1
    x = [3, 12, 3]
    y = [1, 7, 4]
    print(f"covariance: {covariance(x, y)}")
    # teste 2
    x = [-1, 8, 11]
    y = [8, 2, 2]
    print(f"covariance: {covariance(x, y)}")
    # teste 3
    x = [8, 6, 4]
    y = [2, 6, 4]
    print(f"covariance: {covariance(x, y)}")


def correlation(x, y):
    desvio_padrao_x = math.sqrt(sum_of_squares(variance(x)) / (len(x) - 1))
    desvio_padrao_y = math.sqrt(sum_of_squares(variance(y)) / (len(y) - 1))
    if desvio_padrao_x > 0 and desvio_padrao_y > 0:
        return covariance(x, y) / desvio_padrao_y / desvio_padrao_x
    return 0


def correlation_test():
    # teste 1
    x = [3, 12, 3]
    y = [1, 7, 4]
    print(f"correlation: {correlation(x, y)}")
    # teste 2
    x = [-1, 8, 11]
    y = [8, 2, 2]
    print(f"correlation: {correlation(x, y)}")
    # teste 3
    x = [8, 6, 4]
    y = [2, 6, 4]
    print(f"correlation: {correlation(x, y)}")

def quantidade_de_usuarios_na_rede():
    return 100


def gera_idade(quantidade_de_usuarios_na_rede):
    idades = []
    for i in range(quantidade_de_usuarios_na_rede):
        idades.append((random.randint(18,60)))
    return idades


def gera_amizades(numero_conexoes_desejado, qtde_usuarios_na_rede):
    conexoes = []
    for i in range(numero_conexoes_desejado):
        while True:
            u1 = random.randint(0, qtde_usuarios_na_rede - 1)
            u2 = random.randint(0, qtde_usuarios_na_rede - 1)
            if u1 != u2:
                conexoes.append((u1, u2))
                break
    return [aux for aux in set(conexoes)]


def quantidade_de_amigos(amizades):
    a = Counter(i for i, _ in amizades)
    b = Counter(i for _, i in amizades)
    tudo = a + b
    return Counter(x for x in tudo.values())




def main():
    print (correlation(gera_idade(quantidade_de_usuarios_na_rede()),quantidade_de_amigos(gera_amizades(50, quantidade_de_usuarios_na_rede()))))
    #print(gera_idade(quantidade_de_usuarios_na_rede()))
    
    
    #print("Covariancia:")
    #covariance_test()
    #print("Correlação:")
    #correlation_test()
    # variance_test()


# distance_test()
# magnitude_test()
# sum_of_squares_test()
# dot_test()
# vector_mean_test()
# scalar_multiply_test()
# vector_add_test()
# vector_subtract_test()
# vector_sum_test()


main()
