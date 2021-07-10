# list vs strings
# strings are immutable
# immutabel ---> we can not change the original string
# lists are mutable
# mutable---> after applying any function to list it will originally change


s  ="string"
t=s.title()
print(t)
# we cant add characters after string is defined

l=['word1','word2','word3']
l.pop()
print(l)
l.append("word3")
print(l)