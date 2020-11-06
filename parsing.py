import os

key_words = ['---', '---']
contents = ['<content>', '</content>']
reserved_words = {'title' : '', 'label' : '', 'relation' : '', 'slug' : ''}

def preprocess():
    SPLIT_NUM = 0
    CONTENTS_SPLIT = 0

    with open("./DIC/_script.md", 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))

        delete_non(lines)

        '''
        for i in range(len(lines)):
            if lines[i] == "## Contents":
                break

            key_words.insert(-1, lines[i])
            SPLIT_NUM = i + 2
        '''
        

        # contents 추가

        for i in range(len(lines)):
            if lines[i].find('---') != -1:
                CONTENTS_SPLIT = i

            
                break

            key_words.insert(-1, lines[i])
   
        for i in range(CONTENTS_SPLIT + 1, len(lines)):

            contents.insert(-1, lines[i])
        

        
     
def delete_non(line):
    NON_COUNT = line.count('')
    
    if NON_COUNT == 0:
        return
        
    while NON_COUNT > 0:
        NON_COUNT -= 1
        line.remove('')


def make_reserved_word(reserved_words, key_words):
    key_words_str = ''
    

    # reserved words list
    title = ''
    slug = ''
    
    title = key_words[1]
    title = title[1:].strip()
    slug = title[0].upper() + '/' + title    # slug의 첫 문자는 대문자
    reserved_words['title'] = title
    reserved_words['slug'] = slug



    #    ==== label 처리 =====
    label_original = ['[Common]', '[Backend]', '[Frontend]', '[Database]', '[Devops]']
    label_original_temp = ['[Common]', '[Backend]', '[Frontend]', '[Database]', '[Devops]']
    label_list_temp = []
    label = []
    label_temp = ''
    label_str_temp = ''

    LABEL_COUNT_TEMP = 0
    LABEL_COUNT = 0

    for i in range(len(key_words)):
        label_list_temp = key_words[i]
        count_temp = label_list_temp.find('![')
    
        if count_temp != -1:
            LABEL_COUNT += 1


    if LABEL_COUNT == 0:
        reserved_words['label'] = ''
    
    else:
        for i in range(2, 2 + LABEL_COUNT):
            label_temp += key_words[i]

        for j in label_original:
            if label_temp.find(j) == -1:
                label_original_temp.remove(j)
        
        for k in range(len(label_original_temp)):
            label.append(label_original_temp[k])
        
        for i in label:
            label_str_temp += i
        
        label_str_temp = label_str_temp.replace('][', ', ')
        
        reserved_words['label'] = label_str_temp
    

    #    ========== relation ===========
    for i in range(len(key_words)):
        key_words_str += key_words[i]

    RELATION_COUNT = 0
    RELATION_COUNT = key_words_str.count('<a href')
    relation_temp_list = []
    relation = []

    if RELATION_COUNT == 0:
        reserved_words['relation'] = ''
    
    else:
        relation_temp_list = key_words_str.split('<a href')
        del relation_temp_list[0]
        

        for i in relation_temp_list:
            RELATION_SPLIT = i.find('>#')
                
            relation.append(i[RELATION_SPLIT + 2 : i.find('</a>')])
        
        reserved_words['relation'] = relation

        print(reserved_words)
def main(reserved_words, contents):
    file_title = reserved_words['title'].capitalize() + '.md'
    file_path = './output/' + reserved_words['slug'][0] + '/' + file_title
    # dic_directory = './DIC/' + reserved_words['slug'][0]
    complete_directory = './output/' + reserved_words['slug'][0]

    # folder 없을 시, 생성
    try:
        '''
        if not os.path.exists(dic_directory):
            os.makedirs(dic_directory)
        '''

        if not os.path.exists(complete_directory):
            os.makedirs(complete_directory)
        
    except OSError:
        print("Failed to create directory.")
    
    # _script 복사'
    
    '''
    origin_src = "./DIC/_script.md"
    copy_src = dic_directory
    copy_script_name = dic_directory + '/_script.md'
    
    shutil.copy2(origin_src, copy_src)
    current_path = os.getcwd()

    os.chdir(dic_directory)
    
    file_names = os.listdir()

    for i in file_names:
        if i == file_title:
            os.remove(file_title)

    os.rename('_script.md', file_title)
    os.chdir(current_path)
    '''


    with open(file_path, 'w') as f:
        f.write(key_words[0] + '\n')
        f.write('title: ' + reserved_words['title'] + '\n')
        f.write('label: ' + reserved_words['label'] + '\n')
        f.write('relation: ' + str(reserved_words['relation']) + '\n')
        f.write('slug: ' + reserved_words['slug'] + '\n')
        f.write(key_words[-1] + '\n')

        for i in range(len(contents)):
            f.write(contents[i] + '\n')

        f.close(),


preprocess()
make_reserved_word(reserved_words, key_words)
main(reserved_words, contents)



