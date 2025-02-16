import numpy as np # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Example: Create a simple dataset
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Print the dataset
print(df)

# Plot a simple graph
ages = df['Age']
names = df['Name']
plt.bar(names, ages)
plt.xlabel("Names")
plt.ylabel("Ages")
plt.title("Age Distribution")
plt.show()
