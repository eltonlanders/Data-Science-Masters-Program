# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here

#Reading the file
data=pd.read_csv(path)

#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()

#Plotting bar plot
plt.bar(loan_status.index, loan_status)
plt.show()

#Code ends here


# --------------
#Code starts here

#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

#Changing the x-axis label
plt.xlabel('Property_Area')

#Changing the y-axis label
plt.ylabel('Loan_Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

#Code ends here


# --------------
#Code starts here
education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan status')
plt.xticks(rotation=45)


# --------------
#Code starts here

graduate=data[data['Education']=='Graduate']
graduate['LoanAmount'].plot(kind='density',label='Graduate')


not_graduate=data[data['Education']=='Not Graduate']
not_graduate['LoanAmount'].plot(kind='density',label='Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1,figsize=(20,10))
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
#ax_1.title(ApplicantIncome)
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
#ax_2.title(CoapplicantIncome)
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
#ax_3.title(TotalIncome)
plt.show()


