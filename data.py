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


#データ型変換
#list() リスト型変換
a = [1,2,3, 'list']
b = list(a)
print(a)
print(type(a))
print(b)
print(type(b))

# tuple型に変換
a = '1234'
b = int(a)
print(a)
print(type(a))
print(b)
print(type(b))

# 1234
# <class 'str'>
# 1234
# <class 'int'>


# 計算
a = 123
b = '123'

c = a + 7
d = b + 'だー'

print(c)
print(type(c))
print(d)
print(type(d))

# 130
# <class 'int'>
# 123だー
# <class 'str'>

a = 567
b = str(a) + '8910'
print(b)
# 5678910