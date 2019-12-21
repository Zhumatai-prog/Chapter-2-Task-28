list_ = input("Enter numbers: ")

new_list = []
old_list = list_.split(",")
for i in old_list:
	new_list.append(int(i))

print(new_list)

for i in range(0,len(new_list)):
	if new_list[i] > 0:
		new_list[i] = 1
	elif new_list[i] < 0:
		new_list[i] = -1
	else:
		new_list[i] = 0

print(new_list)



