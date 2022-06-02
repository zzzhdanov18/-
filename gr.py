import turtle as tr

def printSpace(mas):
    for i in mas:
        tr.up()
        tr.goto(i[0],i[1])
        tr.dot()
        tr.home()

def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

def searchShell(A):
  n = len(A) 
  P = list(range(n))
  for i in range(1,n):
    if A[P[i]][0]<A[P[0]][0]: 
      P[i], P[0] = P[0], P[i] 
  for i in range(2,n): 
    j = i
    while j>1 and (rotate(A[P[0]],A[P[j-1]],A[P[j]])<0): 
      P[j], P[j-1] = P[j-1], P[j]
      j -= 1
  S = [P[0],P[1]]
  for i in range(2,n):
    while rotate(A[S[-2]],A[S[-1]],A[P[i]])<0:
      del S[-1]
    S.append(P[i])
  return S

a = [[100,100],[150,150],[200,100],[33,30],[67,150],[76,345],[-30,-56],[-100,-200],[0,-40],[-90,0],[-50,50],[-50,100],[-30,-10],[-100,-100],[-200,200]]

S = searchShell(a)

printSpace(a)

tr.goto(a[S[0]][0],a[S[0]][1])
tr.down()

for i in range(len(S)):
    if (i != len(S)-1):
        tr.goto(a[S[i+1]][0],a[S[i+1]][1])
    else:
        tr.goto(a[S[0]][0],a[S[0]][1])

input()