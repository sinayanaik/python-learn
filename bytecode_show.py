import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

numbers = np.random.randint(0, 100, 10)
print(numbers)

#convert to dataframe
df = pd.DataFrame(numbers)

print(df)

# plot the dataframe
plt.plot(df)