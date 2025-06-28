#program to count how many genes to each family from the given data and visualise using bar chart
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data = {
    "GeneID": [f"G{i}" for i in range(1, 19)],
    "Family": [
        "Kinase", "Ligase", "Kinase", "Polymerase", "Kinase", "Ligase",
        "Transferase", "Kinase", "Transferase", "Polymerase", "Ligase",
        "Kinase", "Transferase", "Polymerase", "Ligase", "Kinase",
        "Transferase", "Kinase"
    ]
}

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Count genes per family
family_counts = df['Family'].value_counts()

# Step 4: Plot using bar chart
plt.figure(figsize=(8, 5))
family_counts.plot(kind='bar', color='skyblue', edgecolor='black')

# Step 5: Add labels and title
plt.title("Number of Genes per Family")
plt.xlabel("Gene Family")
plt.ylabel("Number of Genes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Step 6: Show plot
plt.show()

















