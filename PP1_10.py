'''
lesson 1.10
created by leo xu
created on oct 2
'''

import math

def q1(): 
  #Write Assignment code here
  ans1 = input("Input a number: ")
  ans1 = float(ans1)
  print(math.sqrt(ans1))

def q2(): 
  #Write Assignment code here
  ans2 = input("Input a number: ")
  ans2 = int(ans2)
  ans2 = math.isqrt(ans2)
  print(ans2)
def q3(): 
  #Write Assignment code here
  ans3 = input("Input a number: ")
  ans3 = float(ans3)
  print(math.floor(ans3))

def q4(): 
  #Write Assignment code here
  ans4 = input("Input a number: ")
  ans4 = float(ans4)
  print(math.ceil(ans4))

def q5(): 
  #Write Assignment code here
  ans5 = input("Input a number: ")
  ans5 = int(ans5)
  ans6 = input("Input another number: ")
  ans6 = int(ans6)
  ans7 = ans5 * ans6
  ans7 = ans7 // 2
  print(math.ceil(ans7))

#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()
# q4()
# q5()
