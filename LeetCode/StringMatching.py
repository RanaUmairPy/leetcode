
#1 solution
def stringmatching(words):
    arr = " ".join(words)
    sub = []
    for i in words:
        if arr.count(i)>=2:
            sub.append(i)
    return sub



words = ["mass","as","hero","superhero"]
print(stringmatching(words))


#2 solution
def string(words):
    arr = " ".join(words)
    subStr = [word for word in words if arr.count(word) > 1]
    return subStr

words = ["mass", "as", "hero", "superhero"]
print(string(words))


#3 solution
ax = ["i","am","umair","saeed"]
arrjoin = " ".join(ax)
arrcount = [arrjoin.count(i) for i in ax]
print(arrjoin,arrcount)