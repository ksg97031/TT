def taint1(msg):
  print(msg.upper())
 
def taint2(msg):
  print(msg.index("arg0"))
 
def taint3(msg):
  print(msg.format("arg0", "arg1", "arg2"))
