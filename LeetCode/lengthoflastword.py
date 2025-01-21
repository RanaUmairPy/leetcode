def langth(s):
    end = len(s) - 1
    while s[end] == " ":
        end -= 1
    start = end
    while start >= 0 and s[start] != " ":
        start -= 1
        
    return end - start

s = "Hello World i am umair saeed bscs stud ent "
print(langth(s))