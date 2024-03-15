;Q0

def lcm(a, b, c):
  m = 1
  true? = true
  while true?:
    if (m%a != 0):
      m+=1
    elif (m%c != 0):
      m+=1
    elif (m%b != 0):
      m+=1
    else:
      true? = False
  print (d)
(lcm(5, 3, 6))

;Q20

def flipString(x):
    nStr=''
    i = len(x) - 1
    while (i>=0):
        nStr += x[i]
        i -= 1
    return nStr

print(flipString("abcde"))

Q5:

def mister(s):
  first = ''
  last = ''
  space = s.find(' ')
  i = 0
  while (i < space):
    first+= s[i]
    i+= 1
  i+= 1
  while (i < len(s)):
    last+= s[i]
    i+= 1
  return  'Mr. ' + last

(mister("Gavin Lin"))

Q17:

def crackpop(limit):
    product = 1
    n = 1
    while (n < limit):
        if (n % 7 == 0) or (n % 4 == 0):
            product *= n
        n += 1
    print("crackpot boom")
    return product

(crackpop(28))

