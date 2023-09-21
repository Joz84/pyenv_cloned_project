import matplotlib.pyplot as plt
import seaborn as sns
import platform

if platform.python_version() != '3.7.17':
   raise Exception("Python 3.7.17 is required.")

sns.set_theme(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

# Plot the responses for different events and regions
plt.subplots(figsize=(6, 6))
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)
plt.show()