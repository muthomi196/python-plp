marks=int(input('enter the marks:'))
print ('you have entered marks', marks)
print(type(marks))
if marks >= 90:
    print(marks, 'A')
elif marks >= 80:
    print(marks,'B')
else:
    print(marks,'fail.')