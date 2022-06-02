import turtle as tr
from random import randrange
tr.speed(10)

def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

def isHigher(cur):
    global k,b
    if (cur[1] - k*cur[0] - b) > 0: 
        return(1)
    if (cur[1] - k*cur[0] - b) < 0:
        return(2)
    if (cur[1] - k*cur[0] - b) == 0:
        return(3)
    
def printSpace(mas):
    for i in mas:
        tr.up()
        tr.goto(i[0],i[1])
        tr.dot()
        tr.home()

# set = []
# asize = 30
# for i in range(asize):
#   set.append([randrange(-400, 400),randrange(-400, 400)])

set = [[0,-500],[-450,100],[-300,300],[-150,100],[0,-500],[150,100],[300,300],[450,100],[0,300]]

# set = [[100,100],[100,-100],[-100,100],[-100,-100],[130,0],[-130,0],[0,-130],[0,130],[-130,-130],[130,130]]

set = sorted(set, key = lambda k : [k[0],k[1]])

pLeft = set[0]
pRight = set[-1]

k = (pLeft[1]-pRight[1])/(pLeft[0] - pRight[0])
b = pRight[1] - k*pRight[0]

lowPart = [pLeft]
upPart = [pLeft]


for i in range (1, len(set)):
    match isHigher(set[i]):
        case 1:
            while len(upPart) >= 2 and rotate(upPart[-2],upPart[-1],set[i])>0:
               del upPart[-1]
            upPart.append(set[i])
        case 2:
            while len(lowPart) >= 2 and rotate(lowPart[-2],lowPart[-1],set[i])<0:
               del lowPart[-1]
            lowPart.append(set[i])
        case 3:
            if len(upPart) >= 2 and rotate(upPart[-2],upPart[-1],set[i])>0:
               del upPart[-1]
            upPart.append(set[i])
            if len(lowPart) >=2 and rotate(lowPart[-2],lowPart[-1],set[i])<0:
               del lowPart[-1]
            lowPart.append(set[i])

del upPart[0]
del upPart[-1]

upPart.reverse()

ans = lowPart + upPart

printSpace(set)


tr.goto(ans[0][0],ans[0][1])
tr.down()

for i in range(len(ans)):
    if (i != len(ans)-1):
        tr.goto(ans[i+1][0],ans[i+1][1])
    else:
        tr.goto(ans[0][0],ans[0][1])

input()
