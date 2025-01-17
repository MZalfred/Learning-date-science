import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Example: Create a simple dataset
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Print the dataset
print(df)

# Plot a simple bar chart
plt.bar(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age Distribution')
plt.show()
