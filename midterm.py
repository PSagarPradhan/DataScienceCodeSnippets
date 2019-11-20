# Southern Arkansas University
# Math & Computer Science Department
# MCIS-6273 Data Mining, Fall 2019
# Mid-Term: Dta analysis of Olympic games with Pandas
# Instructor: Xin Yang
# 10 questions in total
# Total Points: 100 Points (10 points each question)

#Your name:
#Xin Yang
#Your Student ID:
#99999

# There are ten questions about 120 years of Olympic history:
# athletes and results dataset in this task.
# Your task is to fill in the missing Python code
# and choose the correct answer.

#Download the file athlete_events.csv from the following Kaggle page:
#https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

#1. Import pandas
import pandas as pd

#2. read the dataset as dataframe and save to the variable data
data = pd.read_csv('athlete_events.csv')

#3. print out all the columns of the dataset

print(data.columns)

#4. print out the first 5 rows of the data to take a look the data
print(data.head())

#1. How old were the youngest male and female participants of the 1996 Olympics?
# 10 points (You can use the methods: .max(), .min())
print(data[(data['Sex'] == 'M') & (data['Year'] == 1996)].Age.min(),data[(data['Sex'] == 'F') & (data['Year'] == 1996)].Age.min())
#B
#A. 16 and 15
#B. 14 and 12
#C. 16 and 12
#D. 13 and 11

#Please write your code here


#2. How old were the oldest male and female participants of the 1996 Olympics?
# 10 points
#C
#A. 46 and 35
#B. 50 and 45
#C. 63 and 58
#D. 30 and 41

#Please write your code here
print(data[(data['Sex'] == 'M') & (data['Year'] == 1996)].Age.max(),data[(data['Sex'] == 'F') & (data['Year'] == 1996)].Age.max())

#3. What are the mean and standard deviation of height for female basketball players
# participated in the 2000 Olympics? Round the answer to the first decimal.
# 10 points (You can use the methods: .mean(), .std()
#D
#A. 178.5 and 7.2
#B. 179.4 and 10
#C. 180.7 and 6.7
#D. 182.4 and 9.1

#Please write your code here
print(data[(data['Sex'] == 'F') & (data['Sport'] == 'Basketball') & (data['Year'] == 2000)].Height.mean(),data[(data['Sex'] == 'F') & (data['Sport'] == 'Basketball')& (data['Year'] == 2000)].Height.std())

#4. What are the mean and standard deviation of height for male basketball players
# participated in the 2000 Olympics? Round the answer to the first decimal.
# 10 points
#B
#A. 178.5 and 7.2
#B. 199.5 and 9.0
#C. 180.7 and 6.7
#D. 182.4 and 9.1
print(data[(data['Sex'] == 'M') & (data['Sport'] == 'Basketball') & (data['Year'] == 2000)].Height.mean(),data[(data['Sex'] == 'M') & (data['Sport'] == 'Basketball')& (data['Year'] == 2000)].Height.std())
#Please write your code here

#5. How many silver medals in tennis did Australia (AUS) win at the 2000 Olympics?
# 10 points ()
#C
#A. 0
#B. 1
#C. 2
#D. 3

#Please write your code here
# silver, tennis, aus,200
print(data[(data['Team'] == 'Australia') & (data['Sport'] == 'Tennis') & (data['Year'] == 2000)& (data['Medal'] == 'Silver')].count())

#6. How many silver medals did India (IND) win at the 2016 Olympics?
# 10 points
# B
#A. 0
#B. 1
#C. 2
#D. 3

#Please write your code here
# silver, india, 2016
print(data[(data['Team'] == 'India')  & (data['Year'] == 2016)& (data['Medal'] == 'Silver')].count())

#7. How many medals (Gold, Silver and Bronze) did USA win in total at the 2016 Olympics?
# 10 points (You can use the method .count())

#A. 100
#B. 139
#C. 193
#D. 264

#Please write your code here


#8. What is the absolute difference between the number of unique sports at the
# 1995 Olympics and 2016 Olympics?
# 10 points (You can use the method .nunique())
# nunique, 1995, 2016
data[data['Year'] == 2016].Sport.nunique() - data[data['Year'] == 1995].Sport.nunique()
#D

#A. 16
#B. 24
#C. 26
#D. 34

#Please write your code here

#9. How many Gold medals and Silver medals did 'Michael Fred Phelps, II' win
# at the 2016 Olympics?

#D

# 10 points
#A. Gold 2, Silver 4
#B. Gold 3, Silver 3
#C. Gold 4, Silver 2
#D. Gold 5, Silver 1

#Please write your code here
data[(data['Name']=='Michael Fred Phelps, II') & (data["Year"] == 2016)].Medal.value_counts()

#10. Is it true that Switzerland won fewer medals than Serbia at the 2016 Olympics?
# Do not consider NaN values in Medal column.
# 10 points
#A Yes
#A. Yes
#B. No

#Please write your code here
# serbia, switzerland, 2016
data[(data['Year'] == 2016) & (data['Team'] == 'Serbia') ].Medal.count() >  data[(data['Year'] == 2016) & (data['Team'] == 'Switzerland') ].Medal.count() 
