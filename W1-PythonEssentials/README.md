# <font color='Blue'>Print Statements
> Learning through experiments and data!

## What was the goal?
MovieLens is a company in the internet and entertainment domain that has an online database of information related to films, television series, online streaming content – including cast, production crew, trivia, ratings, and fan and critical reviews. You have been hired as a Data Scientist for the company. You have been provided with the following three datasets, asked to carry out a detailed analysis of the data, and come up with some meaningful insights which will help the company to address their users in a better way.<br>
<br>
- **movie.csv**: The file contains information related to the movies and their genres. Columns: movie id, movie title, release date, Action, Adventure, Animation, Children’s, Comedy, Crime, Documentary, Drama, Fantasy, Film-Noir, Horror, Musical, Mystery, Romance, Sci-Fi, Thriller, War, Western<br>
- **user.csv**: It contains information about the users who have rated the movies. Columns: user id, age, gender, occupation, zip code<br>
- **ratings.csv**: It contains information for ratings given by the users to a particular movie. Columns: user id, movie id, rating, timestamp<br>
<br>
One of the first steps to carry out any analysis is to import the necessary libraries that will help us to carry out various operations on the data. <br><br>**NumPy, Pandas** are the most widely used python libraries in data science. It provides high-performance, easy to use structures and data analysis tools. <br>So let us first import **NumPy and Pandas** so that we can utilize the functions available in these libraries to analyze our data better.
**Note**:
- After running the above cell, kindly restart the runtime (for Google Colab) or notebook kernel (for Jupyter Notebook), and run all cells sequentially from the next cell.
- On executing the above line of code, you might see a warning regarding package dependencies. This error message can be ignored as the above code ensures that all necessary libraries and their dependencies are maintained to successfully execute the code in ***this notebook***.
Now we have imported pandas as pd and numpy as np. Here 'as' is used as an alias.
Let's load all the three datasets using Pandas **read** function so that we can start with our analysis using them

## Why does this matter? (Business Context)
Placeholder: Why does this analysis matter for a business?

## Tech Stack
Google, NumPy, Pandas

## Stuff I used (Libraries)
google, numpy, pandas

## What did I notice?
The initial steps to understand any dataset is to:
- observe the first few rows of the dataset, to check whether the dataset has been loaded properly or not
- get information about the number of rows and columns in the dataset
- find out the data types of the columns to ensure that data is stored in the preferred format and the value of each property is as expected.
- check the statistical summary of the dataset to get an overview of the numerical columns of the data

## What I Found (Insights)
- Introduction to Numpy and Pandas
- Overview of the datasets
- Getting Familiar with Pandas functions
- Extracting useful insights from the data
The movie rating system that film buffs know today has been around for over 50 years. Over the years, the cultural standards and norms have changed and so have movie ratings. However, even today the process of rating a film remains a closely guarded industry secret.

## What I Learned
Placeholder: What was the biggest takeaway?

## How did it do? (Results)
Placeholder: Final model scores or summary.

## Wrapping up
Placeholder: Final thoughts.

## Exercises
- [Exercise 1](./Exercise 1/README.md)
- [Debugging](./Exercise 2/README.md)
- [PreReq](./PreReq/README.md)

