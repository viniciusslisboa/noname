import ast
import os

fileName = "src/cache/storage.txt"
values = {}

try:
  os.makedirs('src/cache', exist_ok=True)
  f = open(fileName, "a")
  f.close()
except OSError as error:
  print(error)



def setItem(key, value):
  write = open(fileName, 'w', newline='')

  values[key] = value

  write.write(str(values))
  write.close()


def getItems():
  with open(fileName, "r") as f:
    read = f.read()
    if(not read):
      return  
      
    res = ast.literal_eval(read)
  return res

def deleteItems():
  write = open(fileName, 'w', newline='')

  write.write('')
  write.close()
