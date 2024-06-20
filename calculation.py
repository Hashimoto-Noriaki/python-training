#演算子
x = 10
y = 2

print(x + y)
#12

#後は他の言語と同じ

#割り算の商
print(x // y)
#5

#関係演算子
x = 10
y = 2

print(x > y)
#True

print(x <= y)
print(x >= y)
#False
#True

#等価
print(x == y)
print(x != y)
# False
# True


#論理演算子
x = 8
y = 3

print(x >= 5 and x <= 10)
print(y >= 5 and y <= 10)
# True
# False

print(x == 3 or y == 3)
print(y == 1 or y == 1)
# True
# False


#代入演算子
x = 5
y = 10
z = 15

x += 10  #15
z += y   #25


#is演算子
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
l3 = l1
print("l1 == l2 :", l1 == l2)
print("l1 is l2 :", l1 is l2)
print("l1 == l3 :", l1 == l3)
print("l1 is l3 :", l1 is l3)

# l1 == l2 : True
# l1 is l2 : False
# l1 == l3 : True
# l1 is l3 : True


#id オブジェクト確認
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
l3 = l1
print("l1_id :", id(l1))
print("l1_id :", id(l2))
print("l3_id :",id(l3))

# l1_id : 4452512128
# l1_id : 4452508608
# l3_id : 4452512128

#is演算子途中まで



#isnot演算子　　今回は省略


#in演算子　今回は省略

# not in 演算子は今回は省略

#ビッド演算子　今回は省略
