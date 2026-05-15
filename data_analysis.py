import pandas as pd 

sales = [
    {"order_id": 1, "customer": "Ana", "category": "Laptops", "price": 900, "quantity": 1, "date": "2024-01-05"},
    {"order_id": 2, "customer": "Marko", "category": "Accessories", "price": 50, "quantity": 2, "date": "2024-01-10"},
    {"order_id": 3, "customer": "Jelena", "category": "Phones", "price": 700, "quantity": 1, "date": "2024-02-01"},
    {"order_id": 4, "customer": "Ana", "category": "Accessories", "price": 30, "quantity": 3, "date": "2024-02-15"},
    {"order_id": 5, "customer": "Petar", "category": "Laptops", "price": 1100, "quantity": 1, "date": "2024-03-01"},
    {"order_id": 6, "customer": "Marko", "category": "Phones", "price": 650, "quantity": 1, "date": "2024-03-10"},
    {"order_id": 7, "customer": "Jelena", "category": "Accessories", "price": 40, "quantity": 2, "date": "2024-03-20"},
]

df = pd.DataFrame(sales)
print(df)

#dodavanje kolone revenue

df['revenue'] = df['price'] * df['quantity']
print(df)

#pretvaranje date u datetime 

df['date'] = pd.to_datetime(df['date'])

#dodavanje kolone month 

df['month'] = df['date'].dt.month
print(df)

#ukupna zarada 

total_revenue = df['revenue'].sum()
print('Total revenue:',total_revenue,"dollars")

#revenue po kategoriji

revenue_per_category = df.groupby('category')['revenue'].sum().reset_index()
print('Revenue per category:',revenue_per_category)

#top customer 

top_customer = df.groupby('customer')['revenue'].sum().sort_values(ascending = False).head(1)
print('Top customer:',top_customer)

#revenue po mesecu 

revenue_per_month = df.groupby('month')['revenue'].sum().reset_index()
print('Revenue per month:',revenue_per_month)

#vizualizacija revenue per category

import matplotlib.pyplot as plt
import seaborn as sns 


plt.figure(figsize = (10,6))
sns.barplot(data = revenue_per_category,x = "category",y = "revenue")
plt.title('Revenue per category')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.show()

#revenue po mesecima 

plt.figure(figsize=(10,6))
plt.plot(revenue_per_month['month'],revenue_per_month['revenue'],marker = "o")
plt.title('Revenue per month')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.show()