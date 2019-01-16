import json
data = dict()
with open("dictionary2.json", encoding="utf8") as f:
	data = json.load(f)

# mod_dict = dict()

# for word in data:
# 	t = word.lower()
# 	mod_dict[t.upper()] = data[word] 

# print(mod_dict)

lines = []
with open("common.txt") as f:
	lines = f.readlines()

new_dictionary = dict()

for word in lines:
	t = word.strip()
	if t in data:
		new_dictionary[t.upper()] = data[t]

s = json.dumps(new_dictionary)
print(s)