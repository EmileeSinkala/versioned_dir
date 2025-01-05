## The project - Investigating the impact of sleep deprivation on different species of fruit flies

### Step 1: Import Libraries and Load Data

# Import necessary libraries
import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import os  # Import os module
# Load the Excel file from the URL
url = "https://github.com/EmileeSinkala/versioned_dir/raw/refs/heads/main/Metadata_1.xlsx"
data = pd.read_excel(url)

### Check working directory

print("Note: The script is loading the data directly from GitHub. Current working directory:", os.getcwd())

### Step 2: Visualize Metadata

# Display a preview of the dataset
print("Preview of the metadata:")
print(data.head())
# Display the columns in the dataset
print("\nColumns in the dataset:")
print(data.columns)

### Step 3: Pre-processing the data 

# Convert 'survival_30_10' column to numeric (0 for alive, 1 for dead)
data['survival_30_10'] = data['survival_30_10'].map({'alive': 0, 'dead': 1}).astype(float)
# Drop rows with missing or invalid data in 'time' or 'survival_30_10'
data = data.dropna(subset=['time', 'survival_30_10'])
# Ensure 'time' column is numeric
data['time'] = pd.to_numeric(data['time'], errors='coerce')
data = data.dropna(subset=['time'])

### Step 4: Perform Survival Analysis

### This first initial plot is showing the different fly species altogether but as you can see, it is hard to see what is going on visually so in the next step we will do separate plots for each species

import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# Initialize the Kaplan-Meier Fitter
kmf = KaplanMeierFitter()

# Initialize the plot
plt.figure(figsize=(12, 8))

# Define a color mapping for species
species_list = data['species'].unique()
color_map = {species: color for species, color in zip(species_list, plt.cm.tab10.colors)}

# Group data by species
species_groups = data.groupby('species')

# Loop through each species
for species, group in species_groups:
    # Get color for this species
    color = color_map[species]

    # Separate control and sleep-deprived groups
    sd_group = group[group['treatment'] == 'SD']
    control_group = group[group['treatment'] == 'C']

    # Fit and plot survival curve for the sleep-deprived group
    if not sd_group.empty:
        kmf.fit(sd_group['time'], event_observed=sd_group['survival_30_10'], label=f"{species} - Sleep-Deprived")
        kmf.plot_survival_function(linestyle='--', color=color, ci_show=False)  # Dashed line, no CI

    # Fit and plot survival curve for the control group
    if not control_group.empty:
        kmf.fit(control_group['time'], event_observed=control_group['survival_30_10'], label=f"{species} - Control")
        kmf.plot_survival_function(linestyle='-', color=color, ci_show=False)  # Solid line, no CI

# Add title, labels, and legend
plt.title("Survival Analysis by Species and Treatment Group", fontsize=16)
plt.xlabel("Time (Days)", fontsize=14)
plt.ylabel("Survival Probability", fontsize=14)
plt.legend()
plt.show()

### The effect of sleep deprivation on the survival of 5 different species of fruit flies

import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# Initialize the Kaplan-Meier Fitter
kmf = KaplanMeierFitter()

# Get the list of unique species
species_list = data['species'].unique()

# Number of species
num_species = len(species_list)

# Define the layout for subplots (2 rows, 3 columns if there are 5 species)
rows = 2
cols = 3 if num_species > 3 else num_species

# Create the figure for subplots
fig, axes = plt.subplots(rows, cols, figsize=(16, 10))

# Flatten axes for easy indexing
axes = axes.flatten()

# Define a color map for consistency
color_map = {species: color for species, color in zip(species_list, plt.cm.tab20.colors)}

# Loop through each species and create a plot
for idx, species in enumerate(species_list):
    ax = axes[idx]  # Get the corresponding subplot axis
    group = data[data['species'] == species]

    # Separate control and sleep-deprived groups
    sd_group = group[group['treatment'] == 'SD']
    control_group = group[group['treatment'] == 'C']

    # Plot for the sleep-deprived group
    if not sd_group.empty:
        kmf.fit(sd_group['time'], event_observed=sd_group['survival_30_10'], label="Sleep-Deprived")
        kmf.plot_survival_function(ax=ax, linestyle='--', color=color_map[species], ci_show=False)

    # Plot for the control group
    if not control_group.empty:
        kmf.fit(control_group['time'], event_observed=control_group['survival_30_10'], label="Control")
        kmf.plot_survival_function(ax=ax, linestyle='-', color=color_map[species], ci_show=False)

    # Customize each subplot
    ax.set_title(f"Species: {species}", fontsize=14)
    ax.set_xlabel("Time (Days)", fontsize=12)
    ax.set_ylabel("Survival Probability", fontsize=12)
    ax.legend(fontsize=10)

# Hide unused subplots (if species < total grid size)
for i in range(num_species, len(axes)):
    fig.delaxes(axes[i])

# Adjust layout
plt.tight_layout()
plt.show()

### Number of fruit flies alive from day 0 to day 9

!pip install scipy statsmodels

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Group data by species, treatment, and time
grouped = data.groupby(['species', 'treatment', 'time'])['survival_30_10'].sum().reset_index()

# Filter for Day 0 and Day 9
filtered = grouped[grouped['time'].isin([0, 9])]

# Get the unique species
species_list = data['species'].unique()

# Loop through each species and plot
for species in species_list:
    # Filter data for the current species
    species_data = filtered[filtered['species'] == species]

    # Extract survival data for statistical tests
    day_0_c = species_data[(species_data['time'] == 0) & (species_data['treatment'] == 'C')]['survival_30_10'].values
    day_0_sd = species_data[(species_data['time'] == 0) & (species_data['treatment'] == 'SD')]['survival_30_10'].values
    day_9_c = species_data[(species_data['time'] == 9) & (species_data['treatment'] == 'C')]['survival_30_10'].values
    day_9_sd = species_data[(species_data['time'] == 9) & (species_data['treatment'] == 'SD')]['survival_30_10'].values

    # Perform t-tests
    ttest_day_0 = ttest_ind(day_0_c, day_0_sd, equal_var=False)
    ttest_day_9 = ttest_ind(day_9_c, day_9_sd, equal_var=False)

    # Create the bar positions and labels
    bar_positions = ['Day 0 (C)', 'Day 0 (SD)', 'Day 9 (C)', 'Day 9 (SD)']
    bar_heights = [
        day_0_c[0], day_0_sd[0], day_9_c[0], day_9_sd[0]
    ]

    # Initialize the plot
    plt.figure(figsize=(10, 6))

    # Plot the bar chart for the current species
    ax = sns.barplot(
        x=bar_positions, 
        y=bar_heights, 
        palette=None  # Remove palette
    )

    # Color bars individually
    bar_colors = ["blue", "orange", "blue", "orange"]
    for bar, color in zip(ax.patches, bar_colors):
        bar.set_facecolor(color)

    # Customize the plot
    plt.title(f"Alive Flies for {species} at Days 0 and 9", fontsize=20)
    plt.xlabel("Time and Treatment", fontsize=16)
    plt.ylabel("Number of Alive Flies", fontsize=16)
    plt.xticks(rotation=45, fontsize=14)  # Rotate x-axis labels for clarity
    plt.yticks(fontsize=14)

    # Add significance annotations
    if ttest_day_0.pvalue < 0.05:
        ax.text(0.5, max(day_0_c[0], day_0_sd[0]) + 1, '*', ha='center', fontsize=16, color='red')

    if ttest_day_9.pvalue < 0.05:
        ax.text(2.5, max(day_9_c[0], day_9_sd[0]) + 1, '*', ha='center', fontsize=16, color='red')

    # Show the plot
    plt.tight_layout()
    plt.show()

