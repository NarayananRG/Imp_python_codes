import pandas as pd
import os
import numpy as np
import statistics as sc
from scipy.stats import kstest,norm,normaltest

os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads")

df=pd.read_csv("sku_dist.csv")
apple=np.array(df['apple_juice'])
mean=apple.mean()
std_div=sc.stdev(apple)
print(mean,std_div)
kstest=kstest(apple,'norm',args=(mean,std_div))
print(kstest)