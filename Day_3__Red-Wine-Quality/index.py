import pandas as pd
import numpy as np
import math



data=pd.read_csv('winequality-red.csv')
print(data.keys())

cols=['fixed acidity','density','pH','quality']
df=df=pd.DataFrame(data, columns=cols)


col_acidity=np.array(df['fixed acidity'])

col_density=np.array(df['density'])
col_ph=np.array(df['pH'])


col_quality=np.array(df['quality'])


features=[]
for i in range(len(col_acidity)):
	features.append([1,col_acidity[i],col_density[i],col_ph[i]])  #adds value 1 as the bias variable to every row

X=np.asarray(features)
y=np.asmatrix(col_quality).T

print(X)
print(y)
input()

theta_best=np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)  #Formula for optimum value of theta 
print(theta_best)

t_bias=np.ravel(theta_best[0])[0]
t_acidity=np.ravel(theta_best[1])[0]
t_density=np.ravel(theta_best[2])[0]
t_ph=np.ravel(theta_best[3])[0]

theta=np.asmatrix([t_bias,t_acidity,t_density,t_ph])  #matrix of values  of thetas

i_acidity=float(input('Acidity= '))
i_density=float(input('Density= '))
i_ph=float(input('pH= '))

m_input=np.asmatrix([1,i_acidity,i_density,i_ph]).T     #coverts  input values into matrix

out=theta.dot(m_input)
print(out)
input()
    