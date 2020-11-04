test_list = []
aa = []
aaa = ''

test = '<a herf = "https://www.naver.com/">#예시</a> <a herf = "https://www.naver.com/">#예시2</a>'

test_list = test.split('</a>')
del test_list[-1]

print(test_list)
for i in range(len(test_list)):
    a = test_list[i].find('#')
    aaa = test_list[i]
    aa.append(aaa[a + 1 : ])

print(aa)
