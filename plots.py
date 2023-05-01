# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# Labels of pie charts
label_pref = lambda val : f'{val / 100 * len(pref_day):.0f}\n{val:.0f}%'
label_skip = lambda val : f'{val / 100 * len(skip_cagegory):.0f}\n{val:.0f}%'
label_sleep = lambda val : f'{val / 100 * len(sleep_time):.0f}\n{val:.0f}%'
label_veg = lambda val : f'{val / 100 * len(veg_non):.0f}\n{val:.0f}%'
label_pref = lambda val : f'{val / 100 * len(food_preference):.0f}\n{val:.0f}%'
label_income = lambda val : f'{val / 100 * len(fam_income):.0f}\n{val:.0f}%'
label_gender = lambda val : f'{val / 100 * len(gender):.0f}\n{val:.0f}%'
label_degree = lambda val : f'{val / 100 * len(degree):.0f}\n{val:.0f}%'

# Loading csv file
df = pd.read_csv('Survey on Mess Food Usage by IITH Students.csv')

# Combining all three columns of skipping meals
count_meal_skip = df[['Roughly what would be the count of no of times you miss mess food in a week? (1-7)','Roughly what would be the count of no of times you miss mess food in a week? (8-14)','Roughly what would be the count of no of times you miss mess food in a week? (15-21)']].copy()
count_meal_skip = count_meal_skip.stack().reset_index(drop=True)
count_meal_skip.plot.hist(edgecolor = "black",title='No of times Student miss mess food in a week')
plt.xlim(0, 21)
plt.xticks(range(1, 22, 2))
plt.savefig('histogram_meal_skip.png')
plt.close()
# print(count_meal_skip.to_string())

# Sorting how often student skip meal
skip_cagegory = df[['How often do you skip mess eating mess food?']].copy()
skip_cagegory = skip_cagegory.sort_values(by=['How often do you skip mess eating mess food?'])
skip_cagegory.groupby('How often do you skip mess eating mess food?').size().plot(kind='pie', autopct=label_skip, textprops={'fontsize': 14}, colors=['violet', 'lime','gold', 'skyblue'] )
plt.savefig('pie_skip_categoty.png',bbox_inches="tight")
plt.close()
# print(skip_cagegory.to_string())

# Sorting late and early night sleeping people
sleep_time = df[['You are?']].copy()
sleep_time = sleep_time.sort_values(by=['You are?'])
sleep_time.groupby('You are?').size().plot(kind='pie', autopct=label_sleep, textprops={'fontsize': 18}, colors=['skyblue', 'lime'] )
plt.savefig('pie_sleep_categoty.png',bbox_inches="tight")
plt.close()
# print(sleep_time.to_string())

# Droping nan values since there were some students who doesn't skip meals

# Sorting veg and non-veg
veg_non = df[['Are you a vegetarian or non-vegetarian?']].copy()
veg_non = veg_non.sort_values(by=['Are you a vegetarian or non-vegetarian?']).dropna()
veg_non.groupby('Are you a vegetarian or non-vegetarian?').size().plot(kind='pie', autopct=label_veg, textprops={'fontsize': 18}, colors=['lime','gold'] )
plt.savefig('pie_veg_non-veg.png',bbox_inches="tight")
plt.close()
# print(veg_non.to_string())

# Sorting by possible reasons for skippin meals at mess
reason = df[['What are probable reason(s) for you to skip the mess?']].copy()
reason = reason.sort_values(by=['What are probable reason(s) for you to skip the mess?']).dropna()
# print(reason.to_string())

# Sorting by food preference
food_preference = df[['What\'s your food preference?']].copy()
food_preference = food_preference.sort_values(by=['What\'s your food preference?']).dropna()
food_preference.groupby('What\'s your food preference?').size().plot(kind='pie', autopct=label_pref,colors=['lime','tomato','violet', 'gold', 'skyblue'],textprops={'fontsize': 12} )
plt.savefig('pie_food_pref.png',bbox_inches="tight")
plt.close()
# print(food_preference.to_string())

# Sorting by skipping of meal by breakfast, lunch and dinner
skip_meal = df[['Which meal do you usually skip in a day?']].copy()
skip_meal = skip_meal.sort_values(by=['Which meal do you usually skip in a day?']).dropna()
skip_meal.groupby('Which meal do you usually skip in a day?').size().plot(kind='bar')
plt.savefig('bar_timing_skip.png',bbox_inches='tight')
plt.close()
# print(skip_meal.to_string())

# Sorting by Gender
gender = df[['Gender :']].copy()
gender = gender.sort_values(by=['Gender :']).dropna()
gender.groupby('Gender :').size().plot(kind='pie', autopct=label_gender,colors=['lime','tomato','violet'],textprops={'fontsize': 12} )
plt.savefig('pie_gender.png',bbox_inches="tight")
plt.close()
# print(gender.to_string())

# Sorting by Age
age = df[['Age :']].copy()
age = age.sort_values(by=['Age :']).dropna()
age.plot(kind='box')
plt.savefig('box_age.png')
plt.close()
# print(age.to_string())

# Sorting by Department
dept = df[['What department are you in?']].copy()
dept = dept.sort_values(by=['What department are you in?']).dropna()
dept.groupby('What department are you in?').size().plot(kind='bar')
plt.savefig('bar_department.png',bbox_inches='tight')
plt.close()
# print(dept.to_string())

# Sorting by Degree
degree = df[['What degree are you pursuing in IITH?']].copy()
degree = degree.sort_values(by=['What degree are you pursuing in IITH?']).dropna()
degree.groupby('What degree are you pursuing in IITH?').size().plot(kind='pie', autopct=label_degree,colors=['lime','tomato','violet'],textprops={'fontsize': 12} )
plt.savefig('pie_degree.png',bbox_inches="tight")
plt.close()
# print(degree.to_string())

# Sorting by weekend/weekdays
pref_day = df[['What days of the week are you likely to skip?']].copy()
pref_day = pref_day.sort_values(by=['What days of the week are you likely to skip?']).dropna()
pref_day.groupby('What days of the week are you likely to skip?').size().plot(kind='pie', autopct=label_pref, textprops={'fontsize': 18}, colors=['violet', 'lime'] )
plt.savefig('pie_plot_weekdays.png',bbox_inches="tight")
plt.close()
# print(pref_day.to_string())

# Sorting by fmaily income
fam_income = df[['Family Income (Per Annum)']].copy()
fam_income = fam_income.sort_values(by=['Family Income (Per Annum)']).dropna()
fam_income.groupby('Family Income (Per Annum)').size().plot(kind='pie', autopct=label_income, textprops={'fontsize': 18}, colors=['violet', 'lime','tomato'] )
plt.savefig('pie_income.png',bbox_inches="tight")
plt.close()
# print(fam_income.to_string())

# Sorting by will eat outside incase they skip meal
outside_mess = df[['Do you eat outside mess, in case you miss a meal?']].copy()
outside_mess = outside_mess.sort_values(by=['Do you eat outside mess, in case you miss a meal?']).dropna()
# print(outside_mess.to_string())

'''Need to break options and take intersections'''
# Sorting by will eat outside incase they skip meal
alter_mess = df[["If yes, what's your alternative? "]].copy()
alter_mess = alter_mess.sort_values(by=["If yes, what's your alternative? "]).dropna()
# print(alter_mess.to_string())

''' Need to sort branches and degree of students who dont skip meals '''

# Sorting for students who dont skip meals
no_skip = df[['Username',"Why don't you skip mess food?"]].copy()
no_skip = no_skip.sort_values(by=["Why don't you skip mess food?"]).dropna()
# print(no_skip.to_string())
