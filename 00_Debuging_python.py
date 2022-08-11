r1, c1, q1 = 6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]            # [8, 10, 25]
r2, c2, q2 = 3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]  # [1, 1, 5, 3]
r3, c3, q3 = 100, 97, [[1,1,100,97]]                             # [1]

rs = r1,r2,r3
cs = c1,c2,c3
qs = q1,q2,q3

import numpy as np

def make_ar(row, col) :
    ar = np.arange(1,row * col +1).reshape(row,col)
    return ar

# def find_min(m1,m2,m3,m4) :
#     minimum = min(min(m1), min(m2), min(m3), min(m4))
#     return minimum

def move_min(org_ar, new_ar,r1,c1,r2,c2) :
    new_ar[r1-1,c1:c2] = org_ar[r1-1,c1-1:c2-1]     # row 1 행 우측 이동
    # [1, 2:4] = [1, 1:3] 
    m1 = new_ar[r1-1,c1:c2]
    new_ar[r1:r2,c2-1] = org_ar[r1-1:r2-1,c2-1]     # col 2 열 아래 이동
    # [2:5, 3] = [1:4, 3]
    m2 = new_ar[r1:r2+1,c2-1]
    new_ar[r2-1,c1-1:c2-1] = org_ar[r2-1,c1:c2]     # ro2 2 행 좌측 이동
    # [4, 1:3] = [4, 2;4]
    m3 = new_ar[r2-1,c1-1:c2-1]
    new_ar[r1-1:r2-1,c1-1] = org_ar[r1:r2,c1-1]     # col 1 열 위로 이동
    # [1:4, 1] = [2:4, 1]
    m4 = new_ar[r1-1:r2,c1-1]
    minimum = int(min(min(m1), min(m2), min(m3), min(m4)))
    return new_ar, minimum

def quiz_02(row, col, q) :
    org_ar = make_ar(row,col)
    new_ar = org_ar * 1
    answer = []
    # cnt = 0
    # print('org : {}\n'.format(cnt),org_ar)
    for i in q :
        # cnt += 1
        row1,col1,row2,col2 = i
        new_ar, minimum = move_min(org_ar,new_ar,row1,col1,row2,col2)
        answer.append(minimum)
        org_ar = new_ar * 1
        # print('new : {}\n'.format(cnt),new_ar)
    return answer

for input in zip(rs,cs,qs) :
    row, col, q = input
    print(quiz_02(row, col, q))