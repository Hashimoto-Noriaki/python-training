#listとは
#複数のデータを格納できるデータ型
#変数が1つのデータしか入れられない箱ならリストは複数のデータが入るロッカー
#1つ1つの箱がデータ

#List作り方
# a = ['要素1','要素2']
name = ['ルフィ','悟空','花道']

print(name[0])
print(name[1])
print(name[2])
# ルフィ
# 悟空
# 花道

name = ['ルフィ','悟空','花道']
name[1] = ' 炭治郎'

print(name[0])
print(name[1])
print(name[2])
# ルフィ
# 炭治郎
# 花道

name = ['ルフィ','悟空','花道']

print(name[-1])
print(name[-2])
# 花道
# 悟空

name = [0,1,2,3,4,5]

print(name[1:4])
print(name[2:])
print(name[:2])
# [1, 2, 3]
# [2, 3, 4, 5]
# [0, 1]

name = [0,1,2,3,4,5]

print(name[::2])
print(name[::-3])
# [0, 2, 4]
#[5, 2]

name = [['ダルビッシュ','大谷'],['エムバペ','ハーランド']]

print(name[0][0])
print(name[0][1])
print(name[1][0])
print(name[1][1])
# ダルビッシュ
# 大谷
# エムバペ
# ハーランド

animal = ['犬','猫','猿']

animal = animal + ['ライオン','リス']
print (animal)
#['犬', '猫', '猿', 'ライオン', 'リス']

animal = ['犬','猫','猿']* 2

print(animal)
#['犬', '猫', '猿', '犬', '猫', '猿']


#listの末尾に要素を追加 append
animal = ['犬','猫','猿']
animal.append('馬')
print(animal)
#['犬', '猫', '猿', '馬']

#extend リスト内の要素を分解して要素として末尾に追加
animal = ['犬','猫','猿']
animal.extend(['ハムスター','ゾウ'])
animal.extend('ハムスター')
print(animal)
#['犬', '猫', '猿', 'ハムスター', 'ゾウ']
#['犬', '猫', '猿', 'ハムスター', 'ゾウ', 'ハ', 'ム', 'ス', 'タ', 'ー']

#insert リストに要素追加
animal = ['犬','猫','猿']
animal.insert(0,'鹿')
print(animal)
# ['鹿', '犬', '猫', '猿']

#リストの要素削除
animal = ['犬','猫','猿']
del animal[1]
print (animal)
#['犬', '猿']

# リストの要素を削除して追加
animal = ['犬','猫','猿']

print (animal.pop(1))
print(animal)
#猫
#['犬', '猿']

animal = ['犬','猫','猿']

#()の場合は1番最後を削除
print (animal.pop())
print(animal)
#猿
#['犬', '猫']


#指定した要素を検索し削除
animal = ['犬','猫','猿']

animal.remove('猫')
print(animal)
#['犬', '猿']

# 全ての要素を削除
animal = ['犬','猫','猿']
animal.clear()
print(animal)
#[]

animal = ['犬','猫','猿']
print('犬' in animal)  # 出力: True
print('トナカイ' in animal)  # 出力: False

#True
#False


# リストの要素を検索した数を取得
animal = ['犬','猫','猿','リス']
print(animal.count('犬'))
#1

#リストの要素のインデックス取得
animal = ['犬','猫','猿','リス']

print(animal.index('犬'))
print(animal.index('猫'))
#0
#1

#リスト要素の並び替え
number = [3,2,1,5,4]
number.sort()
print(number)
#[1, 2, 3, 4, 5]

#大きい順
number = [3,2,1,5,4]
number.sort(reverse=True)
print(number)
#[5, 4, 3, 2, 1]


# reverse リストの要素を逆に変更
animal = ['犬','猫','猿']
animal.reverse()
print(number)
#['猿', '猫', '犬']

#リストの最大値、最小値
number = [8,4,5,6,7,3]
print(max(number))
print(min(number))
#8
#3

#最大値のindex
print(number.index(max(number)))
#0


#リストの要素数 len
number = [8,4,5,6,7,3]
print(len(number))
#6

