import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load data from the CSV file (replace 'your_data.csv' with your actual CSV file)
data = pd.read_csv('PlayerDataRefined.csv')

# Exclude the first column (player names)
data = data.iloc[:, 1:]

# Separate features (X) and the target variable (y, Playstyle)
X = data.drop(columns=['Playstyles'])  # Assuming 'Playstyle' is the column containing the target variable
y = data['Playstyles']

# Create and fit a RandomForestClassifier to predict Playstyle
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Get feature importances
feature_importances = clf.feature_importances_

# Get feature names from the column names of the DataFrame
feature_names = X.columns.tolist()

# Sort feature importances in descending order
sorted_idx = np.argsort(feature_importances)[::-1]

# Define the number of top features to display
top_n = 10  # Change this to the desired number of top features

# Create a bar chart of the top N feature importances
plt.figure(figsize=(10, 6))
plt.bar(range(top_n), feature_importances[sorted_idx][:top_n], align='center')
plt.xticks(range(top_n), [feature_names[i] for i in sorted_idx][:top_n], rotation=90)
plt.xlabel('Feature')
plt.ylabel('Feature Importance')
plt.title(f'Top {top_n} Feature Importance Plot for Playstyle Prediction')
plt.tight_layout()
plt.show()
