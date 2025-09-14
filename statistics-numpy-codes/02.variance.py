import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Generate some data for this
# demonstration.
data = np.random.normal(170, 10, 250)

variance=np.var(data)
max_val=np.max(data)
min_val=np.min(data)
# Fit a normal distribution to
# the data:
# mean and standard deviation
mu, std = norm.fit(data)

# Plot the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='b')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Speed Values Recorded"
plt.title(title)
plt.grid(True)
plt.text( 180,0.03, 
         f"VARIANCE={float(variance):.4f}\n" + 
         f"STD={float(std):.4f}\n"+
         f"MAX={float(max_val):.4f}\n"+
         f"MEAN={float(mu):.4f}\n"+
         f"MIN={float(min_val):.4f}\n", 
         style='italic',
         bbox={
             'facecolor': 'gray', 
             'alpha': 0.5, 
             'pad': 10
             }
         )

plt.xlabel("Speed Values")
plt.ylabel("Probability Distribution")



plt.show()

