import pandas as pd
import numpy as np
import math



data=pd.read_csv('data\\train.csv')
cols=['LotArea','SalePrice']           		#Required Columns for this program

col_area=np.array(data['LotArea']) 			#array storing LotArea Column's all values
col_price=np.array(data['SalePrice'])		#array array storing SalePrice Column's all values


prices=[] 									#New  column with prices of houses having price
area=[]										#New  column with area of houses having price 
for i in range(len(col_area)):		
					
	area.append([1,col_area[i]])		#I'm adding the bias constant(whose value is always 1) column to the matrix too
	prices.append(col_price[i])

data_new={'Area':area,'Price':prices}		#Create new dataset with  features (area and price of houses)

X=np.array(area)
y=np.asmatrix(prices).T




# theta_best is the optimum value of theta for inimum cost/loss function

theta_best = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)  #Formula for optimum value of theta 
print('The optimal value of Parameters(Theta) are:\n')


theta_best=np.matrix.flatten(theta_best)


t_bias=np.ravel(theta_best[0])[0]		#theta for bias variable i.e. 1

t_area=np.ravel(theta_best[0])[1]		#theta for area variable



print('Bias Parameter= '+str(t_bias)+'\n')
print('Parameter for second Parameter(Area)= ' + str(t_area))


#Now, ask user for the Area and give them the best price for their house using the value of theta.



input_area=input("\n\n\nEnter Area of your House:")
input_area=int(input_area)

best_price= t_bias+ t_area*input_area


print("\n\n\n\nThe best price for your house is: $" + str(best_price))

print('\n\n\n\n\n\n\n')
print('================================================================================')
input('Press enter to exit :) ')
