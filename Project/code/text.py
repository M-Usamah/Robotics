import os
# PrePath = os.getcwd()
# print(PrePath,"\n")
# Path = os.chdir("..\\")
# Path
# print(os.chdir("/data"),"\n")
# print(os.chdir("../"),"\n")

print("Current working directory before")
print(os.getcwd())
os.chdir('code')
print(os.getcwd())
print('\n')
os.chdir('../data')
print(os.getcwd())
print(os.dir())