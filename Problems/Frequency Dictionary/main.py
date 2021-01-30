# put your python code here
word_list = input().split()
count_dict = {word.lower(): 0 for word in word_list}

for word in word_list:
    count_dict[word.lower()] += 1

for key, value in count_dict.items():
    print(f'{key} {value}')
