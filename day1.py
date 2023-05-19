'''#variable naming rules
#1. You can not start with digit
#2. You can not use any special character except underscore
#3. You can not have space in between
#4. Variable naming is case sensitive

#Bellow are data types
#1. Integer such as 14,123,5446456
#2. Float which has to do with decimal point such as 1.0,20.2
#3. String data type: "sjgsd", 'hfdas'
#4. Booleans : True or False'''


age=24
gpa=4.29
name="Samuel"
distinction=True

print(gpa)
'''#number1=input('Enter the value of the fist number')
#age_1= float(input('Provide Your Age'))
#age_2=int(input('Provide Second age:'))'''


'''
To display special character like ' you have to use escape which is back slash \
for example We\'re'''

word='we\'re brothers from another mother'
print (word)

'''
New line
To break words into new lines u use: \n'''

word2= 'Python is fin\nPython is easy\nPython is great\nPython is easy to learn'

print(word2)

'''Multiline string has three quotes at the begining and the ending just like the way i do comment'''
word3='''Ptyhon is fun
Python is easy
Python is lovely
Python is bae
'''
print(word3)

print ('Hello' + ' ' + 'World' + ' ' +'##')
print ('Hello' + ' ' + name + ' ' +'to Python class')
print ('Hello' , name, 'to Python class')

'''
String formating'''

price1=45000
price2=15000
price3=85000
report='I sold 4 shirt for {}, a suit for {} and shoe for {}'
report2='I sold 4 shirt for {3}, a suit for {1} and shoe for {2}'
print (report.format(price3,price2,price1))
print(f'I sold for shirts for {price2}, a suit for {price1}, and a shoe for {price3}')

'''string metthod'''

word1='python'
word2='PYTHON'
word3='python is fun'
word4='   info'

print(word1.upper())
print(word2.lower())
print(word3.capitalize())
print(word3.title())
print(word3.split())
print(word4.strip())
print('My name is James'.upper())
state='I\'m from a well-known village with good culture in kogi state'
print (state)
totalmoney=1000
quantity=3
amount=4500
feedback='I have {0}, dollars so i can buy {1} football for {2}.00 dollars'
print(feedback.format(totalmoney,quantity,amount))
poem='''i am a little boy
i love farming
i love palmwine
we use to drink palmwine while we were small
i miss my childhood
'''
print(poem.upper())

num1=float(458)
print (num1)
names=input('Ether three names:')
print(names.split())









