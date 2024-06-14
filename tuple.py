# tupleはlistと違って変更、追加、削除ができない
#メソッドがindexとcountのみ　　listはいろんなメソッドがある=

#書き方
#a = ('データ','データ2')

animal = ('犬','猫','猿')
print(animal)
#('犬', '猫', '猿')

#タプルへのアクセス
print(animal[0])
print(animal[1])
print(animal[2])

# 犬
# 猫
# 猿

#tupleでは変更できない
# animal = ('犬','猫','猿')
# animal[1] = 'ライオン'
# print(animal)

#エラー



#タプルのスライス
#変数[開始:終了]

num = [0,1,2,3,4]

print(num[1:4])
print(num[2:])
print(num[:2])
# [1, 2, 3]
# [2, 3, 4]
# [0, 1]

#ステップして取得
#変数[::終了]
a = (0,1,2,3,4,5)

print(a[::2])
print(a[::-3])
#(0, 2, 4)
#(5, 2)

#多次元タプル
name = (('ダルビッシュ','大谷'),('エムバペ','ハーランド'))
print(name[0][0])
print(name[0][1])
print(name[1][0])
print(name[1][1])
# ダルビッシュ
# 大谷
# エムバペ
# ハーランド

#タプルの足し算、引き算
animal = ('犬','猫','猿')

a = animal + ('ライオン','リス')
print (a)
#('犬', '猫', '猿', 'ライオン', 'リス')

animal = ('犬','猫','猿')* 2
print(animal)
#('犬', '猫', '猿', '犬', '猫', '猿')


#タプルのメソッド
#indexメソッド
animal = ('犬','猫','猿')

print(animal.index('犬'))
#print(animal.index('雉'))
#0
#エラー

#countメソッド
#要素数取得
animal = ('犬','猫','猿')
print(animal.count('犬'))
#1

#タプルの情報取得
#組み込み関数
#in演算子　　
animal = ('犬','猫','猿')
print('猫' in animal)
print('虎' in animal)
#True  存在している
#False　　存在していない

a = (3,2,5,4,1)
print(sorted(a))
#[1, 2, 3, 4, 5]

#大きい順に並べる
a = (3,2,5,4,1)
a = (sorted(a,reverse=True))
print(a)
#[5, 4, 3, 2, 1]

#tupleの最大値、最小値
a = (3,2,5,4,1)
print(max(a))
print(min(a))
#5
#1

#タプルへの変換
#tuple関数使用
l = ['a','b','c']
a = tuple(l)

print(a)
print(type(a))
# ('a', 'b', 'c')
# <class 'tuple'>


s = 'python'
a = tuple(s)

print(a)
print(type(a))
#('p', 'y', 't', 'h', 'o', 'n')
#<class 'tuple'>