test = '<a herf = "https://www.naver.com/">#예시</a> <a herf = "https://www.naver.com/">#예시2</a>'
test_temp = []
test_temp = test.split('<a herf =')
TEST_TEMP_ = 0
relation = ''

print(test_temp)

del test_temp[0]

for i in test_temp:
    TEST_TEMP_ = i.find('>#')
    
    if i == test_temp[len(test_temp) - 1]:
        relation += i[TEST_TEMP_ + 1 : -7]

    else:    
        relation += i[TEST_TEMP_ + 1 : -4]

#print(relation)
