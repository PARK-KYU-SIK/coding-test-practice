n1 = [1, 1, 1, 1, 1]    # 5
n2 = [4, 1, 2, 1]       # 2

t1 = 3
t2 = 4

n = n1, n2
t = t1, t2

import numpy as np

def quiz_03(numbers,target) :
    answer = []
    basic_ar = np.ones(shape=(1,int(len(numbers)))).tolist()[0]
    cnt = 0
    for times in range(-1,2,2) :
        for i,x in enumerate(basic_ar) :
            new_x = x * times
            basic_ar[i] = new_x
            check = int(sum(basic_ar))
            if check == target :
                cnt += 1
                answer.append(basic_ar)
            else :
                pass
    return cnt

quiz_03(n1,t1)

# for input in zip(n,t) :
#     num, tar = input
#     print(quiz_03(num, tar))