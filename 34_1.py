import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1 + np.exp(-x))
def df(x):
    return f(x)*(1-f(x))

N=100000
e= 0.4

W13 = np.random.rand()
W14 = np.random.rand()
W23 = np.random.rand()
W24 = np.random.rand()
W35 = np.random.rand()
W45 = np.random.rand()

Wk45 = W45
Wk35 = W35
Wk24 = W24
Wk23 = W23
Wk14 = W14
Wk13 = W13

errors =[]

N=100000000
e= 0.05
epoch = [[0,1, 1],
                [1,0, 1],
                [0,0, 0],
                [1,1, 0]]

for j in range(N):
    error = 0
    for i in range(len(epoch)):
        In3 = epoch[i][0] * W13 + epoch[i][1] * W23
        In4 = epoch[i][0] * W14 + epoch[i][1] * W24
        Out3 = f(In3)
        Out4 = f(In4)
        In5 = W35 * Out3 + W45 * Out4
        Out5 = f(In5)

        err = epoch[i][2] - Out5
        Delta5 = err * df(In5)
        error += err**2
        Delta3 = Delta5 * W35 * df(In3)
        Delta4 = Delta5 * W45 * df(In4)

        W45 = W45 + e * Delta5 * Out4
        W35 = W35 + e * Delta5 * Out3

        W24 = W24 + e * Delta4 * epoch[i][1]
        W23 = W23 + e * Delta3 * epoch[i][1]

        W14 = W14 + e * Delta4 * epoch[i][0]
        W13 = W13 + e * Delta3 * epoch[i][0]
        if j==N-1:
            Wk45 = W45
            Wk35 = W35

            Wk24 = W24
            Wk23 = W23

            Wk14 = W14
            Wk13 = W13

    errors.append(error)

for i in range(4):
    In3 = epoch[i][0] * Wk13 + epoch[i][1] * Wk23
    In4 = epoch[i][0] * Wk14 + epoch[i][1] * Wk24
    Out3 = f(In3)
    Out4 = f(In4)
    In5 = Wk35 * Out3 + Wk45 * Out4
    Out5 = f(In5)
    print(f"Выход НС: {Out5} => {epoch[i][2]}")
plt.plot(errors)
plt.xlabel("Эпоха")
plt.ylabel("Ошибка")
plt.show()