# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string
what = input("хештег: ")
what = what.title()
result = ""
# elif any (el in string.punctuation and el == " " for el in what
for el in what :
    if el not in string.punctuation and el != " ":
        result += el
result = "#" + result
result = result[:140]
print(result)
print(len(result))