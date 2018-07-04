import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

orders = pd.read_csv('instacart_2017_05_01/orders.csv')
products = pd.read_csv('instacart_2017_05_01/products.csv')
order_products = pd.read_csv('instacart_2017_05_01/order_products__prior.csv')

#print(orders.count()['order_id'])
#print(orders['order_id'].count())
#print(products['product_id'].count())
#print(orders['user_id'].drop_duplicates().count())

#print(order_products['order_id'].value_counts().sort_index())
#plt.plot(order_products['order_id'].value_counts().sort_index())
#plt.xlabel('order id')
#plt.ylabel('number of products')
#plt.show()

orders_by_person = orders.groupby('user_id').count()
print(orders_by_person.mean()['order_id'])