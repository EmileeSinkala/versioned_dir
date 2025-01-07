# **My project - Investigating the Impact of Sleep Deprivation on Different Species of Fruit Flies**
### Background
This project involves looking at 5 different species of fruit files *Drosophila erecta, Drosophila melanogaster, Drosophila sechellia, Drosophila simulans and Drosophila yakuba*. 
All of the data from this project was collected over the space of 9 days, using the aforementioned species. The fruit flies were sleep deprived using an ethoscope.

Ethoscopes are machines which can provide different behavioural stimuli in different formats. The stimuli used in this experiment was a motor device (Geissman et al, 2017).

In this experiment:
- **Controls (C)** were not sleep deprived.
- **Sleep-deprived (SD)** the experimental subjects kept awake using a motor device in the ethoscope which rotated after every 30 seconds of inactivity of the fly. 

### What the Script Does
The script I have developed looks at the impact of sleep deprivation on survival. Before running the script, make sure all of the files are in the same directory (Metadata_1 and project.py). I have found that sometimes opening project.py wont open it directly so if you have this same issue, open the script on a text editor such as notepad, copy and paste the script and run it in a Jupyter lab notebook (this can be accessed via ANACONDA.NAVIGATOR).
1. **Processing of the metadata**
##### The script starts by reading in the data from the Github repository (versioned_dir) and does the following:
- Reads the dataset (Metadata_1.xlsx) using pandas.
- Converts the data in survival_30_10 to numerical values: 0 = alive, 1 = dead.
-  Removes any invalid data in the time and survival_30_10 column
2. **Kaplan-Meier survival analysis**
 The lifelines packages is used to create the survival curves with survival probability on the y-axis and time in days on the x.
- This is done for all of the species combined and then each of the different species separately - comparing between the SD groups and the C groups in the individual graphs as well as any species differences in the graph where all species are plotted.
3. **Bar charts showing the number of flies alive from day 0-9**
##### This part of the script is because I thought it may be easier to understand and visualise what is going on using a bar chart plot. It allows you to see the number of flies alive at the start of the experiment (day 0) and compare it to the end of the experiment (day 9).
4. **Statistical analysis of the bar chart data**
A two-sample t-test was applied to the bar charts to identify if there is any statistical difference between the SD groups and the C groups.

### Installs and imports
 To successfully run the script these libraries are required. The script does include code which will automatically import them for you but they will need to be installed if they are not already. To do so you can run: pip install pandas matplotlib seaborn lifelines scipy 
- pandas - allows data to be loaded, manipulated and analysed
+ matplotlib - for visuals
+ seaborn - generates the bar charts
+ KaplanMeierFitter from lifelines - for the Kaplan-Meier analysis
+ ttest_ind from scipy.stats
### **<u>Conclusion<u/>**
The Kaplan-Meier survival analysis showed that for some species of fruit fly, particularly *D. Yakuba*, sleep deprivation led to a decrease in survival probability. The other 4 species investigated showed smaller decreases in survival in the SD group or not at all. However, none of the following trends were statistically significant.  The bar chart data showed no statistical differences between the groups as shown by the absence of asterisks. D_mel and D_erecta appeared to be the only species that had a noticeable decrease in alive flies but no statistical significance was found for this. Despite the lack of statistical significance in the data, sleep deprivation visually showed that it was reducing their survival but further study is required. Increasing sample size would allow us to investigate if this really is the case. Additionally, prior studies have found that impacting the circadian rhythms of fruit flies reduces their longevity (Thompson et al, 2020). This suggests that the impact of sleep deprivation is dependent on the flies natural sleep length which would explain the differences in survival between the different species that were investigated. A prior study found that flies that naturally have shorter sleep cycles have increased longevity in comparison to longer sleep cycles (Thompson et al, 2020). This suggests that the species which were impacted the least by the SD may have already had shorter sleep lengths to begin with. One way to improve the study would be to create a new genotype of flies that are not able to sleep at all. This would ensure that total sleep deprivation is occuring.
### **<u>References</u>**
- Geissmann, Q., et al. (2017). Ethoscopes: An open platform for high throughput analysis of behaviour. https://pmc.ncbi.nlm.nih.gov/articles/PMC5648103/
+ Thompson, J., et al. (2020). Effects of circadian rhythm disruption on fruit fly longevity. https://journals.biologists.com/bio/article/9/9/bio054361/225803/Sleep-length-differences-are-associated-with
