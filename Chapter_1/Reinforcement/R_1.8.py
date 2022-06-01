"""Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?"""
n = [1, 2, 3, 4, 5]
k = -4
print('n[k]: ', n[k])

j = k + len(n) # should return 3
print('n[j]: ', n[j]) #should print same value as n[k]
