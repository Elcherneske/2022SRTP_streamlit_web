from dataBase import mDatabase
from user_module import userManagement
from baseParameter import parameters

s = mDatabase("localhost","root","fanggroup","srtp2022")
result = s.select_all_value("10_2023_03_05_20_51_52")
print(result)

#print(result[0][0])

#a = [(1,2),(3,4),(5,6)]
#b = a[0:3:1]
#print(b)

