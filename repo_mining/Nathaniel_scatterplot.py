import numpy as np 
import matplotlib.pyplot as plt 

input_names = open("name.txt", 'r')
name = input_names.read()
nameList = name.split("\n")
input_names.close()

input_date = open("date.txt", 'r')
date = input_date.read()
dateList = date.split("\n")
input_date.close()

input_files = open("files.txt", 'r')
file = input_files.read()
fileList = file.split("\n")
input_files.close()

plt.scatter(fileList, dateList)
plt.show()