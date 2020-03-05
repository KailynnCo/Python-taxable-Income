#Write a program that gives the taxable income 

Rate1 = 0.1
Rate2 = 0.15
Rate3 = 0.25
#define my numbers first so the process can be easier
Rate1Single = 8000 
Rate2Single = 32000

Rate1Married = 16000
Rate2Married = 64000 

tax1 = 0.0

print("What is your stauts, single or married?")
Status = str(input()) #single or married is a string

print("What is your income?:")
Income = float(input()) #make a float for # input

if Status == "single" :
 if Income > 0 and Income <= Rate1Single :
  TotalTax = Income * Rate1 #multiply the income 

 if Income > Rate1Single and Income <= Rate2Single:
  tax1 = Income - Rate1Single 
  TotalTax = (tax1 * Rate2) + 800 #make sure to add

 if Income > Rate2Single:
  tax1 = Income - Rate2Single #subtract here
  TotalTax = (tax1 * Rate3) + 4400 #add here

elif Status == "married": #work on the married section
  if Income > 0 and Income <= Rate1Married:
   TotalTax = Income * Rate1
 
  if Income > Rate1Married and Income <= Rate2Married: 
   tax1 = (Income - Rate1Married) 
   TotalTax = (tax1 * Rate2) + 1600 #move these around 
 
  if Income > Rate2Married:
   tax1 = Income - Rate2Married
   TotalTax = (tax1 * Rate3) + 8800
#TotalTax < change it to total tax so it can be the final #
print("Your total tax is:",TotalTax,)




#Erros I need to fix
#single to 9000 stops running - turns out i didnt tab it correclty
#single 33000 stops running and gives wrong # - once again did no tabb it correclty
#note to self: study the if,else,elif on tabbing 



