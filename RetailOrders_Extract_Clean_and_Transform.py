
#import libraries
#installing kaggle
!pip install kaggle
import kaggle


#downloading dataset usig kaggle api

import kaggle
!kaggle datasets download ankitbansal06/retail-orders -f orders.csv


#extract file from zip file

import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


#read data and handel null

import pandas as pd
df = pd.read_csv('orders.csv', na_values=['Not Available', 'unknown'])
df['Ship Mode'].unique()


#rename column name with lower case and underscore for space

#df.rename(columns={'Order ID' : 'order_id', 'Sub Categore' : 'sub_category})
#df.columns=df.columns.str.lower()
#df.columns=df.columns.str.replace(' ','_')
df.head(5)


#new columns for discount

df['discount']=df['list_price']*df['discount_percent']*.01
df.head(5)


#new columns for sale price

df['sales_price']=df['list_price']-df['discount']
df.head(5)


#new columns for profit

df['profit']=df['sales_price']-df['cost_price']
df.head(5)


#convert data type for order date

df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
df.dtypes


#drop the columns that are not required

df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


#load the data into sql server

import sqlalchemy as sal
engine = sal.create_engine('mssql://Gaurav\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()
#connection created


#load the data into sql server using append option

#df.to_sql('df_orders', con=conn, index=False, if_exists = 'replace')
df.to_sql('df_orders', con=conn, index=False, if_exists = 'append')


df.columns




