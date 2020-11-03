# list내에 ''삭제

def delete_non(line):
    NON_COUNT = line.count('')
    
    if NON_COUNT == 0:
        return
        
    while NON_COUNT > 0:
        NON_COUNT -= 1
        line.remove('')

line = ['---', '# Title', '[라벨]', '![Common](../input/image/Label_Common.png)![Backend](../input/image/Label_Backend.png)![Frontend](../input/image/Label_Frontend.png)![Database](../input/image/Label_Database.png)![Devops](../input/image/Label_Devops.png)', '[관련 기술]', '<a herf = "https://www.naver.com/">#예시</a> <a herf = "https://www.naver.com/">#예시2</a>', '---']

delete_non(line)

print(line)

