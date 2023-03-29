import numpy as np
if __name__ == '__main__':
    X = np.random.normal(0, 1, size = (500, 1))
    Y = 0.1*X + 25
    print(np.mean(Y), np.std(Y), "This is a test for conflict")


