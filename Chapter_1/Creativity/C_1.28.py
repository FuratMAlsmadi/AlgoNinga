from unittest import result


def p_norm(v,p):
    sqr_sum = 0
    for i in v:
        sqr_sum += (i**p)
    return (sqr_sum)**(1/p)



print(p_norm((4,3),2))
        