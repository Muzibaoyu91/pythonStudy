height = 1.75
weight = 20
bmi = weight/pow(height,2)
a = '';
if bmi < 18.5:
	a = '过轻'
elif bmi >= 18.5 and bmi < 25:
	a = '正常'
elif bmi >= 26 and bmi < 28:
	a = '过重'
elif bmi >= 28 and bmi < 32:
	a = '肥胖'
elif bmi >= 32:
	a = '严重肥胖'
print('小明的BMI是%s' % a)
		