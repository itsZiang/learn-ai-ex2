# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...

with open('story.txt', 'r') as f:
    word_list = f.read().split()

remove_list = []

for i in range(len(word_list)):
    word_list[i] = word_list[i].lower().strip()
    if "'s" in word_list[i]:
        word_list[i] = word_list[i].replace("'s", "")

for i in range(len(word_list)):
    if not word_list[i].isalpha() and not word_list[i].isdigit():
        remove_list.append(word_list[i])

for i in remove_list:
    word_list.remove(i)

for i in range(len(remove_list)):
    for char in remove_list[i]:
        if not char.isdigit() and not char.isalpha():
            remove_list[i] = remove_list[i].replace(char, "")

temp1 = []

for i in range(len(remove_list)):
    if "â" in remove_list[i]:
        temp2 = remove_list[i].split("â")
        for j in temp2:
            temp1.append(j)

rm = []
for i in remove_list:
    if "â" in i:
        rm.append(i)

for i in rm:
    remove_list.remove(i)

for i in temp1:
    if not i == "":
        remove_list.append(i)

for i in remove_list:
    if "www" in i or i == '':
        remove_list.remove(i)

for i in remove_list:
    if not i == "":
        word_list.append(i)

d = dict()
for word in word_list:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
sortedByFrequently = sorted(d.items(), key=lambda x: x[1], reverse=True)
converted_dict = dict(sortedByFrequently)

count = 0
for key in list(converted_dict.keys()):
    count = count + 1
    if count > 100:
        break
    print(f'{key}: {converted_dict[key]}')
