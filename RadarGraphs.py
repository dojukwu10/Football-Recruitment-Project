import csv
import matplotlib.pyplot as plt
import numpy as np

# Initialize dictionaries to store average values for each playstyle
playstyle_averages = {}
allowed_playstyles = ["Poacher", "Creator", "Aggressor", "Offensive Wing Back"]
attributes = ["Gls", "Ast", "Tkl+Int", "Touches", "AttTO"]  # Replace "Succ%" with "AttTO"

with open('PlayerDataRefined.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        playstyle = row['Playstyles']

        # Check if the playstyle is allowed
        if playstyle in allowed_playstyles:
            try:
                Gls = float(row['Gls'])
                Assists = float(row['Ast'])
                Tackles = float(row['Tkl+Int'])
                Touches = float(row['Touches'])
                AttTO = float(row['AttTO'])  # Replace "Succ%" with "AttTO"

                if playstyle not in playstyle_averages:
                    playstyle_averages[playstyle] = {
                        "Gls": [],
                        "Ast": [],
                        "Tkl+Int": [],
                        "Touches": [],
                        "AttTO": []  
                    }

                playstyle_averages[playstyle]["Gls"].append(Gls)
                playstyle_averages[playstyle]["Ast"].append(Assists)
                playstyle_averages[playstyle]["Tkl+Int"].append(Tackles)
                playstyle_averages[playstyle]["Touches"].append(Touches)
                playstyle_averages[playstyle]["AttTO"].append(AttTO)  # Replace "Succ%" with "AttTO"
            except ValueError:
                pass

# Calculate averages for each playstyle
for playstyle, data in playstyle_averages.items():
    for attribute in attributes:
        data[attribute] = sum(data[attribute]) / len(data[attribute])

# Normalize the values across playstyles
min_max_values = {}
for attribute in attributes:
    min_value = min(data[attribute] for data in playstyle_averages.values())
    max_value = max(data[attribute] for data in playstyle_averages.values())
    min_max_values[attribute] = (min_value, max_value)

for playstyle, data in playstyle_averages.items():
    for attribute in attributes:
        min_value, max_value = min_max_values[attribute]
        if max_value - min_value != 0:
            data[attribute] = (data[attribute] - min_value) / (max_value - min_value)
        else:
            data[attribute] = 0

# Create a radar chart
num_playstyles = len(playstyle_averages)
categories = attributes
values = []

for playstyle in playstyle_averages.keys():
    values.append([playstyle_averages[playstyle][attribute] for attribute in attributes])

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for i, playstyle in enumerate(playstyle_averages.keys()):
    values_playstyle = values[i]
    values_playstyle += values_playstyle[:1]
    ax.fill(angles, values_playstyle, alpha=0.25, label=playstyle)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.yaxis.grid(True)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
ax.set_rlabel_position(45)  # Adjust the position of the radial labels
plt.title('Radar Chart for Normalized Average Stats by Playstyle')
plt.show()
