import time
import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def getComb(x):
    l = []
    x = str(x)
    l.append(x)
    tmp = list(x)
    i = 1
    while (len(x)>i):
        tmp.insert(0, tmp.pop())
        l.append(''.join(tmp))
        i+=1
    for xid, element in enumerate(l):
        l[xid]=int(element)
    return l

def main():
    start_time = time.time()
    howMuch = 0
    for i in range(2, 1000000):
        if isPrime(i):
            li = getComb(i)
            isCircular = True
            for x in li:
                if not isPrime(x):
                    isCircular = False
                    break
            if isCircular==True:
                print i
                howMuch+=1
    print "Number of circular primes: %s" % howMuch
    print 'Time: %s' % (time.time() - start_time)

if __name__ == '__main__':
    main()