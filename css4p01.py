# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:16:42 2024

@author: Tanja Eksteen
"""

# Import pandas library to work with data sets using a data frame
import pandas as pd

# Load the data file movie_dataset.csv as a data frame keep the index column because the first column is rating and not an identifier
df = pd.read_csv("movie_dataset.csv")

# print file to view information in the movie file to see if the file can be read
print(df)

"""
     Rank                    Title  ... Revenue (Millions) Metascore
0       1  Guardians of the Galaxy  ...             333.13      76.0
1       2               Prometheus  ...             126.46      65.0
2       3                    Split  ...             138.12      62.0
3       4                     Sing  ...             270.32      59.0
4       5            Suicide Squad  ...             325.02      40.0
..    ...                      ...  ...                ...       ...
995   996     Secret in Their Eyes  ...                NaN      45.0
996   997          Hostel: Part II  ...              17.54      46.0
997   998   Step Up 2: The Streets  ...              58.01      50.0
998   999             Search Party  ...                NaN      22.0
999  1000               Nine Lives  ...              19.64      11.0

[1000 rows x 12 columns]

"""

# to access more information about the data you can view the summary using file.info
print(df.info())

"""
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None
"""
# when looking at the information of the data one can see that the column names thus variables doen not conform to good variables naming practics.
# Fix Variable names
# Note that the data type for all the variables looks correct
# Rename variable 7 Runtime and 10 Revenue

df = df.rename(columns={'Runtime (Minutes)':'Runtime_Minutes','Revenue (Millions)':'Revenue_Millions'})

# check if the column name change was completed
print(df.info())

# look at the descriptive statistic for the data frame to make insighitfull decisions 

print(df.describe()) 

"""
              Rank         Year  ...  Revenue_Millions   Metascore
count  1000.000000  1000.000000  ...        872.000000  936.000000
mean    500.500000  2012.783000  ...         82.956376   58.985043
std     288.819436     3.205962  ...        103.253540   17.194757
min       1.000000  2006.000000  ...          0.000000   11.000000
25%     250.750000  2010.000000  ...         13.270000   47.000000
50%     500.500000  2014.000000  ...         47.985000   59.500000
75%     750.250000  2016.000000  ...        113.715000   72.000000
max    1000.000000  2016.000000  ...        936.630000  100.000000

[8 rows x 7 columns]
 
"""
# Review all the variables for data cleaning drop NaNs (remove rows)
df.dropna(inplace=True)

# NaNs succesfully removed
print(df.info())

"""
Index: 838 entries, 0 to 999
Data columns (total 12 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Rank              838 non-null    int64  
 1   Title             838 non-null    object 
 2   Genre             838 non-null    object 
 3   Description       838 non-null    object 
 4   Director          838 non-null    object 
 5   Actors            838 non-null    object 
 6   Year              838 non-null    int64  
 7   Runtime_Minutes   838 non-null    int64  
 8   Rating            838 non-null    float64
 9   Votes             838 non-null    int64  
 10  Revenue_Millions  838 non-null    float64
 11  Metascore         838 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 85.1+ KB
None
"""
# Question 1

#find the highest value in rating column

Highest_Rating = df['Rating'].idxmax()

Movie_Title = df.at[Highest_Rating, 'Title']

# Print the result
print("The highest rating in Rating is:", df.at[Highest_Rating, 'Rating'])
print("The movie name for the highest rating is:", Movie_Title)

# Question 2

average_revenue_1 = df['Revenue_Millions'].mean()
print("The average revenue is:", average_revenue_1)

# Question 3

Movies_From_2015 = 2015
Movies_To_2017 = 2017

# Filter the DataFrame for movies from 2015 to 2017
filtered_df = df[(df['Year'] >= Movies_From_2015) & (df['Year'] <= Movies_To_2017)]

# Calculate the average for column 'B' in the filtered DataFrame
Average_Revenue = filtered_df['Revenue_Millions'].mean()

# Print the average
print("Average revenue from 2015 to 2017 is", Average_Revenue)

# Question 4 get 198 with two different methods

# count_2016 = (df['Year'].2016).sum()

# Print the count
# print("Number of occurrences of '2016' in the 'Year' column:", count_2016)

# Count the occurrences of each unique value in the 'Year' column
counts = df['Year'].value_counts()

# Get the count for the specific value '2016'
count_2016 = counts.get(2016, 0)  # If '2016' is not present, default to 0

# Print the count
print("Number of occurrences of '2016' in the 'Year' column:", count_2016)

# Question 5 

# Count if movie is directed by Christopher Nolan

count_Nolan = df['Director'].str.contains('Christopher Nolan').sum()

# Print the count
print("Number of movies directed by Christopher Nolan is:", count_Nolan)


# Question 6 when removing the NaNs it gives you 70

least = 8.0

# Count the number of ratings greater than 8.0
count_greater_than_least = df[df['Rating'] >= least]['Rating'].count()


# Print the count
print("Number of values greater than", least, "for ratings':", count_greater_than_least)

# Question 7

# Filter the DataFrame to include only movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating for movies directed by Christopher Nolan
median_rating_nolan = nolan_movies['Rating'].median()

# Print the median rating
print("Median rating for movies directed by Christopher Nolan:", median_rating_nolan)


# Question 8

# Group the DataFrame by 'Year' and calculate the average rating for each year
average_ratings_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_ratings_by_year.idxmax()
highest_average_rating = average_ratings_by_year.max()

# Print the result
print("Year with the highest average rating:", year_highest_average_rating)
print("Highest average rating:", highest_average_rating)

# Question 9

# Calculate the total number of movies made in 2006
total_movies_2006 = (df['Year'] == 2006).sum()

# Calculate the total number of movies made in 2016
total_movies_2016 = (df['Year'] == 2016).sum()

# Calculate the percentage increase
percentage_increase = ((total_movies_2016 - total_movies_2006) / total_movies_2006) * 100

# Print the result
print("Percentage increase in number of movies made between 2006 and 2016:", percentage_increase)

# Question 10

# Split the 'Actors' column to separate individual actors
actors_split = df['Actors'].str.split(', ')

# Flatten the list of actors
all_actors = [actor for sublist in actors_split for actor in sublist]

# Count the occurrences of each actor
actor_counts = pd.Series(all_actors).value_counts()

# Find the most common actor
most_common_actor = actor_counts.idxmax()

# Print the result
print("The most common actor in all the movies is:", most_common_actor)

# Question 10

# Split the genres in the 'Genre' column and create a list of all genres
all_genres = [genre.strip() for sublist in df['Genre'].str.split(',') for genre in sublist]

# Create a set of unique genres
unique_genres = set(all_genres)


# Count the number of unique genres
num_unique_genres = len(unique_genres)

# Print the result
print("Number of unique genres in the dataset:", num_unique_genres)

# Question 11

import matplotlib.pyplot as plt
import seaborn as sns

# Exclude non-numeric columns before performing correlation analysis
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Perform correlation analysis
correlation_matrix = numeric_df.corr()

# Visualize correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()



