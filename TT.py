def taint1(msg):
  print(msg.upper())
 
def taint2(msg):
  a = msg + "2"
  print(a.index("arg0"))
 
def taint3(msg):
  a = msg + "2"
  b = a + "3"
  print(b.format("arg0", "arg1", "arg2"))
 
def taint4(msg):
  a = msg + "4"
  str.format(a, "B")
  
if __name__ == '__main__':
  taint1("t")
  taint2("t")
  taint3("t")
  taint4("t")
