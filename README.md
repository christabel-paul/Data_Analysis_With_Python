# Data Analysis With Python
Summary: This dataset from.... lists 7669 Movies and their corresponding features.
Dataset:

**Dataset Attributes:**  
name: Movie Title 
rating  
genre  
year  
released: full release date and Country (date (country))  
score: value from 0.0-10.0  
votes: number of IMDb user votes 
director  
writer  
star: starring actor  
country: Country of Release  
budget: film budget  
gross: film gross revenue  
company: Production company
runtime: runtime in minutes

## Analysis Steps
  1. Fill in null values
  2. FIX THIS Issue in dataset: the existing **country** and **year** attributes do not consistenly match the year and Country of the **released** attribute. Since the released attribute contains the correct values, extract the country and year from the released column and populate a new country and year field. 
  3. Boxplot of Gross Revenue to identify outlierss
  4. Scatterplot of Gross Revenue vs Budget **fix on graph **
  5. Regression plot of Gross Revenue vs film budget
  6. Generate correlations table for numeric features
  7. Generate heatmap based on correlations table
  8. 


## See [Python Script](https://github.com/christabel-paul/Data_Analysis_With_Python/blob/main/Movies.ipynb) for output figures.

