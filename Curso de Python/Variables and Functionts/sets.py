# -*- coding: utf-8 -*-

s = set([1,2,3])

t = set([3,4,5])

print(s.union(t))

print(s.intersection(t))

print(t.difference(s))
print(s.difference(t))

print(1 in t)