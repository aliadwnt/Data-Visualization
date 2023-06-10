#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read the CSV file
data = pd.read_csv("data bank.csv")

#saving the figure 
plt.savefig("data bank.jpg")

# Printing the top 10 rows
print(data.head(10))


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("data bank.csv")

# Scatter plot
plt.scatter(data['job'], data['age'])

# Set labels for x and y axes
plt.xlabel('job')
plt.ylabel('age')

#saving the figure 
plt.savefig("scatterplot.jpg")

# Display the plot
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("data bank.csv")

#scc
plt.scatter(data["job"], data["age"], c=data['day'], s=data['previous'])

#judul
plt.title("Scatter Plot")

# Set labels for x and y axes
plt.xlabel('Job')
plt.ylabel('Age')

#saving the figure 
plt.savefig("photo2_scatterplot2.jpg")

# Display the plot
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("data bank.csv")

#scc
plt.plot(data["education"])
plt.plot(data["balance"])

#judul
plt.title("Line Chart")

# Set labels for x and y axes
plt.xlabel('Education')
plt.ylabel('Balance')

#saving the figure 
plt.savefig("photo3_linechart.jpg")

# Display the plot
plt.show()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("data bank.csv")

# Bar chart
plt.bar(data['education'], data['campaign'])

# Title
plt.title("Bar Chart")

# Set labels for x and y axes
plt.xlabel('Education')
plt.ylabel('Campaign')

#saving the figure 
plt.savefig("photo4_Barchart.jpg")

# Display the plot
plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("data bank.csv")

#total
plt.hist(data['age'])

#judul
plt.title("Histogram")

#saving the figure 
plt.savefig("photo5_histogram.jpg")

#add the leg
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("data bank.csv")

# INISIAL
education = ['secondary', 'tertiary', 'primary', '(unknow)']
age = [5476, 36689, 1500, 567]

# Pie chart
plt.pie(age, labels=education)

# Add title
plt.title("Bank Data")

#saving the figure 
plt.savefig("photo6_piechart.jpg")

# Display the plot
plt.show()


# In[ ]:




