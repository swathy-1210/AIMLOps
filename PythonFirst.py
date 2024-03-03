import pdb
a=20
def func():
  global a
  a=100
  print(a)
func()
print(a)