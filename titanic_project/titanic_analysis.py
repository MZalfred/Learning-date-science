# Import pandas library for data handling
import pandas as pd

# Load the Titanic dataset
data = pd.read_csv('test.csv')

# Display the first 5 rows of the dataset to check it loaded correctly
print("Dataset Preview:")
print(data.head())

# Get summary information about the dataset
print("\nDataset Info:")
print(data.info())

# Check for missing values in each column
print("\nMissing Values in Each Column:")
print(data.isnull().sum())

# Step 1: Drop the 'Cabin' column since it has too many missing values
data = data.drop(columns=['Cabin'])
print("\nDropped the 'Cabin' column.")

# Step 2: Fill missing values in the 'Age' column with the mean age
data['Age'] = data['Age'].fillna(data['Age'].mean())
print("\nFilled missing values in the 'Age' column with the mean.")

# Step 3: Convert the 'Sex' column to numerical values (male: 0, female: 1)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
print("\nConverted 'Sex' column to numerical values (male: 0, female: 1).")

# Step 4: Create a new column 'FamilySize' by adding 'SibSp' and 'Parch'
data['FamilySize'] = data['SibSp'] + data['Parch']
print("\nCreated a new 'FamilySize' column.")

# Step 5: Preview the cleaned dataset
print("\nCleaned Dataset Preview:")
print(data.head())

# Step 6: Import visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Plot 1: Count of passengers by class
plt.figure(figsize=(10, 6))
sns.countplot(x='Pclass', data=data, palette='coolwarm')
plt.title('Passenger Count by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

# Plot 2: Count of passengers by survival status (if available)
if 'Survived' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Survived', data=data, palette='Set2')
    plt.title('Count of Survival Status')
    plt.xlabel('Survived (0 = No, 1 = Yes)')
    plt.ylabel('Count')
    plt.show()

# Plot 3: Distribution of passenger age
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=30, kde=True, color='blue')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
