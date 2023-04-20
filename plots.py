# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading csv file
df = pd.read_csv('Survey on Mess Food Usage by IITH Students.csv')

# Combining all three columns of skipping meals
count_meal_skip = df[['Roughly what would be the count of no of times you miss mess food in a week? (1-7)','Roughly what would be the count of no of times you miss mess food in a week? (8-14)','Roughly what would be the count of no of times you miss mess food in a week? (15-21)']].copy()
count_meal_skip = count_meal_skip.stack().reset_index(drop=True)
# print(count_meal_skip.to_string())

# Sorting how often student skip meal
skip_cagegory = df[['How often do you skip mess eating mess food?']].copy()
skip_cagegory = skip_cagegory.sort_values(by=['How often do you skip mess eating mess food?'])
# print(skip_cagegory.to_string())

# Sorting late and early night sleeping people
sleep_time = df[['You are?']].copy()
sleep_time = sleep_time.sort_values(by=['You are?'])
# print(sleep_time.to_string())

# Droping nan values since there were some students who doesn't skip meals

# Sorting veg and non-veg
veg_non = df[['Are you a vegetarian or non-vegetarian?']].copy()
veg_non = veg_non.sort_values(by=['Are you a vegetarian or non-vegetarian?']).dropna()
# print(veg_non.to_string())

# Sorting by possible reasons for skippin meals at mess
reason = df[['What are probable reason(s) for you to skip the mess?']].copy()
reason = reason.sort_values(by=['What are probable reason(s) for you to skip the mess?']).dropna()
# print(reason.to_string())

# Sorting by food preference
food_preference = df[['What\'s your food preference?']].copy()
food_preference = food_preference.sort_values(by=['What\'s your food preference?']).dropna()
# print(food_preference.to_string())

# Sorting by skipping of meal by breakfast, lunch and dinner
skip_meal = df[['Which meal do you usually skip in a day?']].copy()
skip_meal = skip_meal.sort_values(by=['Which meal do you usually skip in a day?']).dropna()
# print(skip_meal.to_string())

# Sorting by Gender
gender = df[['Gender :']].copy()
gender = gender.sort_values(by=['Gender :']).dropna()
# print(gender.to_string())

# Sorting by Age
age = df[['Age :']].copy()
age = age.sort_values(by=['Age :']).dropna()
# print(age.to_string())

# Sorting by Department
dept = df[['What department are you in?']].copy()
dept = dept.sort_values(by=['What department are you in?']).dropna()
# print(dept.to_string())

# Sorting by Degree
degree = df[['What degree are you pursuing in IITH?']].copy()
degree = degree.sort_values(by=['What degree are you pursuing in IITH?']).dropna()
# print(degree.to_string())

# Sorting by weekend/weekdays
pref_day = df[['What days of the week are you likely to skip?']].copy()
pref_day = pref_day.sort_values(by=['What days of the week are you likely to skip?']).dropna()
# print(pref_day.to_string())

# Sorting by fmaily income
fam_income = df[['Family Income (Per Annum)']].copy()
fam_income = fam_income.sort_values(by=['Family Income (Per Annum)']).dropna()
# print(fam_income.to_string())

# Sorting by will eat outside incase they skip meal
outside_mess = df[['Do you eat outside mess, in case you miss a meal?']].copy()
outside_mess = outside_mess.sort_values(by=['Do you eat outside mess, in case you miss a meal?']).dropna()
# print(outside_mess.to_string())

# Sorting by will eat outside incase they skip meal
alter_mess = df[["If yes, what's your alternative? "]].copy()
alter_mess = alter_mess.sort_values(by=["If yes, what's your alternative? "]).dropna()
# print(alter_mess.to_string())

''' Need to sort branches and degree of students who dont skip meals '''

# Sorting for students who dont skip meals
no_skip = df[['Username',"Why don't you skip mess food?"]].copy()
no_skip = no_skip.sort_values(by=["Why don't you skip mess food?"]).dropna()
# print(no_skip.to_string())
