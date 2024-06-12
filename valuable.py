num = 100
print(num)
# 100

# PEP8
score = 90
score01 = 80
score_01 = 70

print(score)
print(score01)
print(score_01)

# 90
# 80
# 70

# 間違った変数
#point-01 = 10
#01point
#point$01

#予約語は変数にできない
# return = 1
# print(return)


# 予約後を調べる方法
import keyword

print(keyword.iskeyword('return'))
print(keyword.iskeyword('Return'))
#True
#False

a = 100
b = 1
a = 200
print(a)
print(b)

# 200
# 1


a = 10
print(id(a))
b = a
a = 20
print(id(b))
print(id(a))
# 4381025800
# 4381025800
# 4381026120