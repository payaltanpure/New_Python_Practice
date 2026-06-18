import math

print(math.sqrt(5))
print(math.factorial(5))
print(math.ceil(45.89))
print(math.floor(45.89))
print(math.pi)
print(math.pow(2,3))


import random as r
print(r.randint(1,10)) #gives any random no from 1 to 10, no float whole nos returned
print(r.randrange(0,10,2))  #given any random no but according to step value last value 0 to 10 is range here it returns even no always randomlt becoz setp value is 2 and staring range is 0 so 0+2= 2
print(r.random())#gives values betwwen 0.0 to 1.0
print(r.uniform(1,9))#floating type random nos from 1 to 9 range

f= ["apple", "mango", "chikko"]
print(r.choice(f)) #gives any random value from the list, returns single value 
print(r.choices(f, k=2)) #gives any random values from list equal to k value from list, returns multiple values according to k

# real life use of randint 
#to create otp which is always random meand different
otp= r.randint(0000, 9999) #4 digitd becoz otp is of 4 digit always
print(otp)


import datetime as dt
print(dt.datetime.now()) # current date, time 

#only date
print(dt.date.today())

#only time
dl= dt.datetime.now()
print(dl.time())
 
#day month year separatly print
dl= dt.datetime.now()
print(dl.day)
print(dl.month)
print(dl.year)


#own add  date
print(dt.date(2020,10,12))

#date format --yy/mm/dd--> dd/mm/yy
x= dt.datetime.now()
print(x.strftime("%d/ %m/ %y")) #format date
print(x.strftime("%S-%M-%H"))  # format time

#difference between dates

#diff bet current date and past date, how many days passed
cudate= dt.date(2026,5,19)
birthdate= dt.date(2005,5,26)
print(cudate-birthdate)

#future data from current date
cudate= dt.datetime.now()
future= cudate+d.time
