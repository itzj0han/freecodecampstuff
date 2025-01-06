import pandas as pd
import numpy as np
df=pd.read_csv('adult.data', header=None)
df.columns=['age','workingclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','salary']
print(df['race'].value_counts())#1
df['sex']=df['sex'].str.strip()
averageage=df[df['sex']=='Male']['age'].mean()
print("The Average Age of Men is", averageage)#2
df['education'].str.strip
peoplewithbachelors=df['education'].value_counts()[' Bachelors']
percentageofbachelors=(peoplewithbachelors/len(df['education'])*100)#3
print("Percentage of people with bachelors is" ,percentageofbachelors)
salarystuff = df[(df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])) & (df['salary']==' >50K')]#4
peoplestuff=df['education'].isin([' Bachelors', ' Masters', ' Doctorate']).sum()
percentageofstuff="People who make more than 50k with advanced education is",len(salarystuff)/peoplestuff*100
print(percentageofstuff)
salarystuff2 = df[(~df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])) & (df['salary']==' >50K')]
peoplestuff2=(~df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])).sum()
percentageofstuff2="People who make more than 50k without any advanced degree",len(salarystuff2)/peoplestuff2*100
print(percentageofstuff2)#5
print("Minimum number of hours worked:",df['hours-per-week'].min())#6
min_hours=df['hours-per-week'].min()
people_min_hours=df[df['hours-per-week']==min_hours]
min_time_earners=len(people_min_hours[people_min_hours['salary']==" >50k"])
print("Minimum time earners",min_time_earners)#7
people_from_each_country = df['native-country'].value_counts()
top_earners_each_country = df[df['salary'] == ' >50K']['native-country'].value_counts()
percentage_of_top_earners = (top_earners_each_country / people_from_each_country) * 100
percentage_of_top_earners = percentage_of_top_earners.fillna(0)
highest_percentage_country = percentage_of_top_earners.idxmax()
highest_percentage_value = percentage_of_top_earners.max()
print(f"The country with the highest percentage of people earning >50K is {highest_percentage_country} with {highest_percentage_value:.2f}%.")
highest_earners_india=df[df['salary']==" >50k"&df['native-country']==' India']
most_popular_occupation = highest_earners_india['occupation'].value_counts().idxmax()
print(most_popular_occupation)
#print(df.head)
