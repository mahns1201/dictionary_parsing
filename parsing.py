each_data = []

script = open("./input/test.md", 'r', encoding = 'utf-8')

data = script.readlines()
each_data.append(data).remove('\n')


print(each_data)


script.close()