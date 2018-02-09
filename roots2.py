import numpy as np
import csv
import sys


def fibonacci(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

listy=[fibonacci(k) for k in range(10)]

def polynomial_generate(alpha, beta, k,n):
    g0=np.poly1d([alpha])
    g1=np.poly1d([1,beta])
    xk=np.poly1d([int(k==0) for k in range(k+1)])
    if n==0:
        return g0
    if n==1:
        return g1
    return xk*polynomial_generate(alpha,beta,k,n-1)-polynomial_generate(alpha,beta,k,n-2)




with open('k_of_' + sys.argv[1] + 'next' '.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter= ',')
    spamwriter.writerow(['a']  + ['b'] + ['15 roots'] + [' '] + [' '] +  [' '] +[' '] +[' '] + [' '] + [' '] +  [' '] +[' '] +[' ']+[' '] + [' '] +  [' '] +[' '] +[' '] + [' '] + [' '] +  [' '] +[' ']+ ['16 roots'] + [' '] +[' '] +[' '] +[' '] +[' '] + [' '] + [' '] +  [' '] +[' '] +[' '] +  [' '] + [' '] +  [' '] +[' '] +[' '] + [' '] + [' '] +  [' '] +[' ']  )

    k_pow = int(sys.argv[1])    

    for i in range(81):
        print(i / 10.0  -4)
        for n in range(81):

            #print("a = " + str(i/10.0 - 4))
            #print("b = " + str(n/10.0 - 4))
            #print("15:")
            p=polynomial_generate(i/10.0 -4, n/10.0 -4 ,k_pow,15)
            
            for x in range(k_pow):
                p = p.deriv()

            r = np.roots(p)
            g = r[np.isreal(r)]
            #print("16:")
            p=polynomial_generate(i/10.0 -4,n/10.0 -4 ,k_pow,16)

            for e in range(k_pow):
                p = p.deriv()

            h = np.roots(p)
            l = h[np.isreal(h)]
            row = []
            row.append(i / 10.0 - 4)
            row.append(n / 10.0 - 4)
            c =  0
            for q in range(g.size):
	        row.append(float(g[q]))
                c+=1
            for y in range(20-c):
                row.append(' ') 
            c =  0
            for t in range(l.size):
	        row.append(float(l[t]))
                c+=1
            for u in range(20-c):
                row.append(' ') 
            spamwriter.writerow(row)







