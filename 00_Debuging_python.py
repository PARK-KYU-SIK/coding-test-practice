n1 = [1, 1, 1, 1, 1]    # 5
n2 = [4, 1, 2, 1]       # 2

t1 = 3
t2 = 4

n = n1, n2
t = t1, t2

import numpy as np

def quiz_03(numbers, t) :

    answer = 0
    ls = 2 ** len(numbers)
    ns = len(numbers)
    ar = np.ones(shape=(ls,ns))

    for j, number in enumerate(numbers) :
        cnt = 1
        for i in range(ls) :
            if i == (((2)**(ns-j-1)) * cnt) - 1 :
                cnt += 1
                ar[i,j] = ar[i,j] * number * ((-1)** (cnt + 1))
            else :
                ar[i,j] = ar[i,j] * number * ((-1)** (cnt + 1))
        
     
    for i in range(ls) :
        if sum(ar[i]) == t :
            answer += 1

    return answer

# for input in zip(n,t) :
#     num, tar = input
#     print(quiz_03(num, tar))