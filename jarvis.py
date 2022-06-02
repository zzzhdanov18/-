import turtle as tr
from random import randrange

def printSpace(mas):
    for i in mas:
        tr.up()
        tr.goto(i[0],i[1])
        tr.dot()
        tr.home()

def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

def jarvismarch(A):
  n = len(A)
  P = list(range(n))
  # start point
  for i in range(1,n):
    if A[P[i]][0]<A[P[0]][0]:
      P[i], P[0] = P[0], P[i]
  S = [P[0]]
  del P[0]
  P.append(S[0])
  while True:
    right = 0
    for i in range(1,len(P)):
      if rotate(A[S[-1]],A[P[right]],A[P[i]])<0:
        right = i
    if P[right]==S[0]:
      break
    else:
      S.append(P[right])
      del P[right]
  return S

#b = [[100,100],[150,150],[200,100],[33,30],[67,150],[76,345],[-30,-56],[-100,-200],[0,-40],[-90,0],[-50,50],[-50,100],[-30,-10],[-100,-100],[-200,200]]

tr.speed(10)
a = []
asize = 30
for i in range(asize):
  a.append([randrange(-400, 400),randrange(-400, 400)])

S = jarvismarch(a)

printSpace(a)

tr.goto(a[S[0]][0],a[S[0]][1])
tr.down()

for i in range(len(S)):
    if (i != len(S)-1):
        tr.goto(a[S[i+1]][0],a[S[i+1]][1])
    else:
        tr.goto(a[S[0]][0],a[S[0]][1])

screen = tr.Screen()
screen.listen()
screen.onkey(lambda: tr.bye(), 'space')
tr.done()
