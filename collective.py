# 集合とは
# ある条件を満たす集まり
#要素に順番　なし、重複に意味なし


#集合の作り方
c = {0,3,4,2,6}
print(c)
print(type(c))
# {0, 2, 3, 4, 6}
#<class 'set'>


c = {123,1.23,(1,2,3),123,1.23}
print(c)
#{1.23, 123, (1, 2, 3)}


c = {0,3,4,2,6}
s = set(c)
print(s)
#{0, 2, 3, 4, 6}


#空集合
s1 = set()
s2 = {}

print(type(s1))
print(type(s2))

# <class 'set'>
# <class 'dict'>

#追加
s = {0,1,2}
s.add(3)
print(s)
#{0, 1, 2, 3}


#削除
s = {0,1,2}
s.remove(1)
print(s)
#{0, 2}


#全削除
s = {0,1,2}
s.clear()
print(s)
#set()


#frozenset関数
#要素の削除、追加できない集合
c = {0,3,4,2,6}
s = frozenset(c)
# s.add(8)  追加できない
#s.clear() 全削除できない
print(c)
#{0, 2, 3, 4, 6}


c1 = {0,3,4}
c2 = {3,4,5}

c3 = c1 | c2
print(c3)
#{0, 3, 4, 5}

c4 = c1.union(c2)
print(c4)
#{0, 3, 4, 5}


#積集合
c1 = {0,3,4}
c2 = {3,4,5}
c3 = {4,5,6}

c4 = c1 & c2 & c3
print(c4)

c5 = c1.intersection(c2 & c3)
print(c5)
# {4}
# {4}


#差集合
c1 = {0,1,2}
c2 = {1,2,3}
c3 = {2,3,4}

c4 = c1 & c2 &c3
print(c4)

c5 = c1.intersection(c2,c3)
print(c5)

# {2}
# {2}


#対象差集合



# 集合の関係


# 要素の存在確認


# 要素の取得
s = {4,3,2,1}
for i in s:
    print(i)

# 1
# 2
# 3
# 4



#集合をリストに変換
s = {4,3,2,1}
l = list(s)

print(l[0])
#1