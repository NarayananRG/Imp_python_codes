import numpy as np
import statistics as sc

a = np.random.uniform(1, 100, 100).round(decimals=0)
print(a.mean())
print(sc.median(a))
print(sc.mode(a))
print(sc.stdev(a))

def range_data(data):
    b = max(data) - min(data)
    return b
print(range_data(a))

print(sc.variance(a))

print(np.percentile(a,50))

