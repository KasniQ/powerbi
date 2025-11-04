import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# BLINKIT DATA ANALYSIS IN PYTHON

df = pd.read_csv("C:/Users/kasni/Documents/GitHub/powerbi/Project2/Blinkit Data/BlinkIT Grocery Data.csv")

#print(df.head(10))              #df.head(10) <- first 10 records, this works only in jupyter notebook
                                #df.tail(15) <- last 15 records
#print("Size of Data: ", df.shape)                 #number of records and columns

#print(df.columns)          #column names

#print(df.dtypes)           #column datatypes

#print(df['Item Fat Content'].unique())              #unique values from particular column
df['Item Fat Content'] = df['Item Fat Content'].replace({'LF':'Low Fat', 'low fat' : 'Low Fat', 'reg' : 'Regular'}) #data cleaning
#print(df['Item Fat Content'].unique()) 



#BUSINESS REQUIREMENTS

#KPI's REQUIREMENTS

#Total Sales
total_sales = df['Total Sales'].sum()

#Average Sales
Average_sales = df['Total Sales'].mean()

#No of Items Sold
no_of_items_sold = df['Total Sales'].count()

#Average Ratings
avg_ratings = df['Rating'].mean()

#Display
    #print(f"Total Sales: ${total_sales:,.0f}")
    #print(f"Average Sales: ${Average_sales:,.0f}")
    #print(f"Number Of Items Sold: {no_of_items_sold:,.0f}")
    #print(f"Average Ratings: {avg_ratings:,.0f}")

#Charts Requirements

#Total Sales by Fat Content
sales_by_fat = df.groupby('Item Fat Content')['Total Sales'].sum()
plt.pie(sales_by_fat, labels = sales_by_fat.index, autopct = '%.0f%%', startangle = 90)
plt.title('Sales By Fat Content')
plt.axis('equal')
#plt.show()


#Total Sales by Item Type
sales_by_type = df.groupby('Item Type')['Total Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
bars = plt.bar(sales_by_type.index, sales_by_type.values)
plt.xticks(rotation=-90)
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Item Type')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():,.0f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
#plt.show()

#Fat Content by Outlet for Total Sales
grouped = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Total Sales'].sum().unstack()
grouped = grouped[['Regular', 'Low Fat']]

ax = grouped.plot(kind='bar', figsize=(8,5), title = 'Outlet Tier by Item Fat Content')
plt.xlabel('Outlet Location Tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
#plt.show()


#Total Sales by Outlet Establishment
sales_by_year = df.groupby('Outlet Establishment Year')['Total Sales'].sum().sort_index()

plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o')

plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.title('Total Sales by Outlet Establishment')

for x, y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x,y,f'{y:,.0f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
#plt.show()

#Total Sales by Outlet Size
sales_by_size = df.groupby('Outlet Size')['Total Sales'].sum()

plt.figure(figsize=(4,4))
plt.pie(sales_by_size, labels = sales_by_size.index, autopct='%1.0f%%', startangle=90)
plt.title('Total Sales by Outlet Size')
plt.tight_layout()
#plt.show()

#Total Sales by Outlet Location
sales_by_location = df.groupby('Outlet Location Type')['Total Sales'].sum().reset_index()
sales_by_location = sales_by_location.sort_values('Total Sales', ascending=False)

plt.figure(figsize=(8,3))
ax = sns.barplot(x='Total Sales', y='Outlet Location Type', data=sales_by_location)

plt.title('Total Sales by Location Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location Type')


plt.tight_layout()
plt.show()