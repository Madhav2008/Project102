import threading

def printit():
  threading.Timer(2.0, printit).start()
  print("Hello !")
  print(" ")
  print("How Are You ?")
  print(" ")
  print("Madhav Arora This Side")
  print(" ")
  
printit()
