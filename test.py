def arrange(seq, curr=0):
    if curr == len(seq)-1:
        return
    else:
        if seq[curr] % 2 == 0:
            arrange(seq, curr=curr+1)
        else:
            seq[curr], seq[curr+1] = seq[curr+1], seq[curr]
            arrange(seq, curr=curr+1)


seq = [1, 2, 3, 8, 9]
arrange(seq)
print(seq)
