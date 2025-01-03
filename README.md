# My project - Investigating the impact of sleep deprivation on different species of fruit flies
### Background
##### This project involves looking at 5 different species of fruit files *Drosophila erecta, Drosophila melanogaster, Drosophila sechellia, D simulans and D yakuba*. 
##### All of the data from this project was collected over the space of 9 days, using the aforementioned species. The fruit flies were sleep deprived using an ethoscope.
##### Ethoscopes are machines which can provide different behavioural stimuli in different formats. The stimuli used in this experiment was a motor device (Geissman et al, 2017).
##### In this experiment, there were controls (C) which were not sleep deprived (SD) and the experimental subjects which were sleep deprived (SD).
##### Those that were sleep deprived, were kept awake using the motor device in the ethoscope which rotated after every 30 seconds of inactivity of the fly.
### What the script does
##### The script I have developed looks at the impact of sleep deprivation on survival
1. **Processing of the metadata**
##### The script starts by reading in the data from the Github repository (versioned_dir) and does the following:
##### - Reads the dataset (Metadata_1.xlsx) using pandas.
##### - Converts the data in survival_30_10 to numerical values: 0 = alive, 1 = dead.
##### - Removes any invalid data in the time and survival_30_10 column
2. **Kaplan-Meier survival analysis**
##### The lifelines packages is used to create the survival curves with survival probability on the y-axis and time in days on the x. This is done for all of the species together and then each of the different species separately - comparing between the SD groups and the C groups in the individual graphs as well as any species differences in the graph where all species are plotted.
3. **Bar charts showing the number of flies alive from day 0-9**
##### This part of the script is because I thought it may be more easier to understand and visualise what is going on using a bar chart plot. It allows you to see the number of flies alive at the start of the experiment (day 0) and compare it to the end of the experiment (day 9).
4. **Statistical analysis of the bar chart data**
##### A two-sample t-test was used on the bar charts to identify if there is any statistical difference between the SD groups and the C groups.
### Installs and imports
##### To succesfully run the script these libraries are required. The script does include code which will automatically import them for you but they will need to be installed if they are not already. To do so you can run: pip install pandas matplotlib seaborn lifelines scipy 
##### - pandas - allows data to be loaded, manipulated and analysed
##### - matplotlib - for visuals
##### - seaborn - generates the bar charts
##### - KaplanMeierFitter from lifelines - for the Kaplan Meier analysis
##### - ttest_ind from scipy.stats
### References
##### Geissmann, Q., et al. (2017). Ethoscopes: An open platform for high throughput analysis of behaviour. https://pmc.ncbi.nlm.nih.gov/articles/PMC5648103/
