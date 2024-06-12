#数字型
num01 = 150
num02 = 1.45

print(num01)
print(num02)

# 150
# 1.45

print(type(num01))
print(type(num02))
# <class 'int'>
# <class 'float'>

# 文字型
string_a = 'Python学習'

print(string_a)
print(type(string_a))

#Python学習
# <class 'str'>

# bool型
a = 100
b = 1

bool02 = (a < b)
print(bool02)
print(type(bool02))
#False
#<class 'bool'>

# list型
a = [1,2,3, 'list']
print(type(a))
#<class 'list'>

# tuple型
#tuple型は1度代入した要素を書き換えることができない
b = (1,2,3,'tuple')
print(type(b))
#<class 'tuple'>


#辞書型
z = {'a':1,'b':2,'c':3,'d':'dict'}
print(type(z))
#<class 'dict'>


#set型
s1 = {1,2,3}
s2 = {1,2,3,4}

print(s1)
print(s2)
print(type(s1))
print(type(s2))
