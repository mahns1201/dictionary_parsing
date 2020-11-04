key_words = ['---', '---']
contents = ['<content>', '</content>']
reserved_words = {'title' : '', 'label' : '', 'relation' : '', 'slug' : ''}

def delete_non(line):
    NON_COUNT = line.count('')
    
    if NON_COUNT == 0:
        return
        
    while NON_COUNT > 0:
        NON_COUNT -= 1
        line.remove('')


def make_reserved_word(reserved_words, key_words):
    key_words_str = ''
    label_original = ['[Common]', '[Backend]', '[Frontend]', '[Database]', '[Devops]']
    
    # reserved words list
    title = ''
    label = ''
    relation = ''
    slug = ''

    for i in range(len(key_words)):
        key_words_str += key_words[i]
    
    LABEL_SPLIT = key_words_str.find('[라벨]')
    RELATION_SPLIT = key_words_str.find('[관련 기술]')

    title = key_words_str[5 : LABEL_SPLIT]
    label_temp = key_words_str[LABEL_SPLIT + 4 : RELATION_SPLIT]
    
    slug = title[0].upper() + '/' + title
    
    #    ==== relation 처리 =====
    relation_original = key_words_str[RELATION_SPLIT + 7 : -3]
    relation_temp = []
    relation_temptemp = []
    temp = ''

    relation_temp = relation_original.split('</a>')
    del relation_temp[-1]

    for i in range(len(relation_temp)):
        SPLIT_NUM_TEMP = relation_temp[i].find('#')
        temp = relation_temp[i]
        relation_temptemp.append(temp[SPLIT_NUM_TEMP : ])

    for q in range(len(relation_temptemp)):
        relation += relation_temptemp[q]
    #    ========================

    #    ==== label 처리 =====
    for j in label_original:
        if label_temp.find(j) == -1:
            label_original.remove(j)
    
    for k in range(len(label_original)):
        label += label_original[k]

    reserved_words['title'] = title
    reserved_words['label'] = label
    reserved_words['relation'] = relation
    reserved_words['slug'] = slug
    #    =====================
    '''    
    title = key_words[1]

    reserved_words['title'] = title[2:]
    reserved_words['label'] = key_words[3]
    reserved_words['relation'] = key_words[5]

    slug = title[2].upper() + '/' + title[2:]    # slug의 첫 문자는 대문자
    reserved_words['slug'] = slug
    '''

    return reserved_words

def preprocess():
    SPLIT_NUM = 0

    with open("./input/script.md", 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))

        delete_non(lines)

        for i in range(len(lines)):
            if lines[i] == "## Contents":
                break

            key_words.insert(-1, lines[i])
            SPLIT_NUM = i + 2
        
        # print('key words: ', key_words)

        for j in range(SPLIT_NUM, len(lines)):
            contents.insert(-1, lines[j])
        
        return contents
        


def main(reserved_words, contents):
    file_title = reserved_words['title'].capitalize() + '.md'
    file_path = './' + reserved_words['slug'][0] + '/' + file_title

    with open(file_path, 'w') as f:
        f.write(key_words[0] + '\n')
        f.write('title: ' + reserved_words['title'] + '\n')
        f.write('label: ' + reserved_words['label'] + '\n')
        f.write('relation: ' + reserved_words['relation'] + '\n')
        f.write('slug: ' + reserved_words['slug'] + '\n')
        f.write(key_words[-1] + '\n')
        # f.write(contents)

        for i in range(len(contents)):
            f.write(contents[i] + '\n')

        f.close()


preprocess()
make_reserved_word(reserved_words, key_words)
main(reserved_words, contents)










