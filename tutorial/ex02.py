def arrayCheck(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

print(arrayCheck([1,1,2,3,4]));


def stringBits(str):
  value = ""
  for i in range(len(str)):
    if i % 2 == 0:
      value += str[i]
  return value

print(stringBits("heeololeo"))

def end_other(a, b):
  a = a.lower();
  b = b.lower();

  return a[-(len(b)):] == b or a == b[-len(a):]


def doubleChar(mystring):
  result = ""
  for char in mystring:
    result += char * 2

  return result

print(doubleChar('asdf'))


def no_teen_sun(a, b, c):
  
  return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n) :
  if n [13, 14, 17, 18, 19]:
    return 0
  return n

  print(no_teen_sun(1,3,5))