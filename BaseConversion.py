'''
By Michael Vartan
michael.vartan@student.csulb.edu
23 January 2012
'''

import math;

'''
decimalToBase(num,base)
converts a number from base ten to another base (max: base 36)
'''
def decimalToBase(num,base):
	charList = "0123456789abcdefghijklmnopqrstuvwxyz"
	newNum = ""
	while True:
		newNum = charList[int(num)%base]+newNum;
		num=math.floor(num/base);
		if(num<1):
			break;
	return newNum;
'''
decimalFromBase(num,base)
#converts a number from any base to base ten. (max: base 36)
'''
def decimalFromBase(num,base):
	newNum=0
	num=str(num)
	for a in range(0,len(num)):
		if(num[a].isdigit()):
			val=int(num[a])
		else:
			val=ord(num[a].lower())-87
		newNum+=val*math.pow(base,len(num)-a-1);
	return newNum;
'''
convertNumberRadices(num,base1,base2
#converts any number in any base to any other base (max: base 36)
'''
def convertNumberBase(num,base1,base2):
	return decimalToBase(decimalFromBase(num,base1),base2)

print decimalToBase(10,2)