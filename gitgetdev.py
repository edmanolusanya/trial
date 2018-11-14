#import os
#import csv
#import pandas as pd



#data = pd.read_csv("c:/Users/ekpo eddy/Documents/gitgetdev/getdev.csv")

#data.head()



import csv
#open and read csv file 
with open('c:/Users/ekpo eddy/Documents/gitgetdev/getdev.csv', 'r') as f:
#put into a variable
  reader = csv.reader(f, delimiter=',')
  your_list = list(reader)
  for row in your_list:
      for column in row:
          R1col1="Get"
          R2col2="dev"
          R3col3="is"
          R4col4="the"
          R5col5="future"
          R6col6="and"
          R7col7="the"
          R8col8="future"
          R9col9="is"
          R10col10="now"
          if(column==R1col1):
              print(R1col1)
              
          if(column==R2col2):
              print(column)
              
          if(column==R3col3):
              print(column)

          if(column==R4col4):
              print(column)

          if(column==R5col5):
              print(column)          

          if(column==R6col6):
              print(column)

          if(column==R7col7):
              print(column)
              
          if(column==R8col8):
              print(column)

          if(column==R9col9):
              print(column)

          if(column==R10col10):
              print(column)










