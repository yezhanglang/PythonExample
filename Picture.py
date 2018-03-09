#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

print(t)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
