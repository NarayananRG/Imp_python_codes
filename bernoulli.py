import matplotlib.pyplot as plt
from scipy.stats import bernoulli
#
# Instance of Bernoulli distribution with parameter p = 0.7
#
bd = bernoulli(0.7)
#
# Outcome of experiment can take value as 0, 1
#
X = [0, 1,2,3]
#
# Create a bar plot; Note the usage of "pmf" function
# to determine the probability of different values of
# random variable
#
plt.figure(figsize=(7,7))
plt.xlim(-1, 2)
plt.bar(X, bd.pmf(X), color='orange')
plt.title('Bernoulli Distribution (p=0.7)', fontsize='15')
plt.xlabel('Values of Random Variable X (0, 1)', fontsize='15')
plt.ylabel('Probability', fontsize='15')
plt.show()