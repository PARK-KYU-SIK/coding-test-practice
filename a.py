op1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]    # [0,0]
op2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] #[333, -45]

def sol(x) :

    a = []

    for op in x :
        o, num  = op.split(sep = ' ')
        if o == 'I' :
            a.append(num)
            a.sort()
        else :
            if len(a) == 0 :
                continue
            else :
                if num == '1' :
                    del a[-1]
                else :
                    del a[0]

    if len(a) == 0 :
        answer = [0,0]
    else :
        answer = [max(a), min(a)]

    return answer


print(sol(op2))