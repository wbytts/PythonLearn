'''
集合的创建使用符号   {}

 s = {1, 2, 3, 4, 5}
'''

s = {1, 2, 3, 4, 5}
print(type(s))

# 集合中的元素不能重复，如果创建时有重复的，会算一个
s = {1, 1, 2, 2, 3, 3}
print(s)
