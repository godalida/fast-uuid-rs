import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data
with open("benchmark_results.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Create visualization
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Create barplot
ax = sns.barplot(
    data=df,
    x="size",
    y="rows_per_second",
    hue="framework",
    palette="viridis"
)

plt.title("UUID Generation Speed: fast-uuid vs Standard Python/Polars", fontsize=16)
plt.xlabel("Number of Rows (Count)", fontsize=12)
plt.ylabel("Rows per Second (Higher is Better)", fontsize=12)
plt.legend(title="Method")

# Save to file
plt.savefig("benchmark_chart.png", dpi=300)
print("Saved benchmark_chart.png")
