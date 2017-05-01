from sys import stdout 
scale = 10000 
maxarr = 2800 
arrinit = 2000 
carry = 0 
arr = [arrinit] * (maxarr + 1) 
for i in xrange(maxarr, 1, -14): 
  total = 0 
  for j in xrange(i, 0, -1): 
    total = (total * j) + (scale * arr[j]) 
    arr[j] = total % ((j * 2) - 1) 
    total = total / ((j * 2) - 1) 
  stdout.write("%04d" % (carry + (total / scale))) 
  carry = total % scale 