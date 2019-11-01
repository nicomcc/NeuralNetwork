import numpy as np

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def sigmoideFunction(soma):
    return 1/(1 + np.exp(-soma))

def tahnFunction(soma):
    return ((np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma)))

def reluFunction(soma):
    if (soma >= 0) :
        return soma
    return 0

def linearFunction(soma):
    return soma

def softmaxFunction(x):    
    ex = np.exp(x)
    return ex/ex.sum()


teste5 = softmaxFunction([5.0, 2.0, 1.3])
print(teste5)
valores = [5.0, 2.0, 1.4]
print(softmaxFunction(valores))           

teste = stepFunction(300)
sigmoide = sigmoideFunction(2.1)
tahn = tahnFunction(2.1)
relu = reluFunction(2.1)
linear = linearFunction(2.1)
