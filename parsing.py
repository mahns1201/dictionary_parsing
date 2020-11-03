key_words = ['---', '---']
contents = ['<content>', '<p>', '</p>', '</content>']

def delete_non(line):
    NON_COUNT = line.count('')
    
    if NON_COUNT == 0:
        return
        
    while NON_COUNT > 0:
        NON_COUNT -= 1
        line.remove('')

def main():
    SPLIT_NUM = 0

    with open("./input/test.md", 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))

        delete_non(lines)

        for i in range(len(lines)):
            if lines[i] == "## Contents":
                break

            key_words.insert(-1, lines[i])
            SPLIT_NUM = i + 1
        
        print('key words: ', key_words)

        for j in range(SPLIT_NUM, len(lines)):
            contents.insert(-2, lines[j])
        
        print('contents: ', contents)


main()







