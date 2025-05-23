# -*- coding: utf-8 -*-
"""Board.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fpn1g2UF9YWBraCPO6aLnb2hfojXwLua
"""

# 士兵
checkerboard = [
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0] ]

position1 = input().split()
position2 = input().split()

x1,y1 = int(position1[0]),int(position1[1])
x2,y2 = int(position2[0]),int(position2[1])

# 原地、有障礙物

if(x1 == x2 and y1 == y2) or (checkerboard[x2][y2] == 1):
  print("No")
elif(x2 == x1 + 1 and y1 == y2):
  print("Yes")
else:
  print("No")

#　騎士
checkerboard = [
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0] ]

position1 = input().split()
position2 = input().split()

x1,y1 = int(position1[0]),int(position1[1])
x2,y2 = int(position2[0]),int(position2[1])

# 原地、有障礙物

if(x1 == x2 and y1 == y2) or (checkerboard[x2][y2] == 1):
  print("No")
elif(abs(x2-x1)==2 and abs(y2-y1)==1)or(abs(y2-y1)==2 and abs(x2-x1)==1):
  print("Yes")
else:
  print("No")

#　國王
checkerboard = [
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0] ]

position1 = input().split()
position2 = input().split()

x1,y1 = int(position1[0]),int(position1[1])
x2,y2 = int(position2[0]),int(position2[1])

# 原地、有障礙物

if(x1 == x2 and y1 == y2) or (checkerboard[x2][y2] == 1):
  print("No")
elif(abs(x2-x1)<=1 and abs(y2-y1)<=1):  # <=1
  print("Yes")
else:
  print("No")

# 皇后
checkerboard = [
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]
]

# 讀取位置 x1, y1 and x2, y2 split()
# slice for all four
# not the same, no obstacle
# not straight line or diagonal
# c1, c2 one by one set up max 1 by abs, reachable = True
# while loop and print out reachable

position1 = input().split()
position2 = input().split()

x1, y1 = int(position1[0]), int(position1[1])
x2, y2 = int(position2[0]), int(position2[1])
# why not int(x2), int(y2) = position2[0], position2[1]

if (x1 == x2 and y1 == y2) and (checkerboard[x2][y2] == 1):
    print("No")
elif not (x2 == x1 or y2 == y1 or abs(x2 - x1) == abs(y2 - y1)):
    print("No")
else:
    dx = (x2 - x1) // max(abs(x2 - x1), 1) # max防止分母為0(有設定至少為1)，移動可以是0，但是不能0/0
    dy = (y2 - y1) // max(abs(y2 - y1), 1)  # 不適用來看x移動是否等於y，而是為了準備判斷每移動以格是否合法
    reachable = True
    cx, cy = x1 + dx, y1 + dy

    while (cx != x2 or cy != y2): # 還沒到目的地就繼續檢查，因為不能一次就到，目的地沒有終點可能有
        if checkerboard[cx][cy] == 1:
            reachable = False
            break
        cx += dx
        cy += dy

    if reachable:
        print("Yes")
    else:
        print("No")