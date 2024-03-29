import json
import os
from time import time

def extract_texts(file):
    texts = ''
    with open(file, encoding='utf-8') as f:
        # each line in the file is a wiki page
        row = 0
        for line in f:
            # read the line as valid json and select text field
            print('reading the {} line text'.format(row))
            text = json.loads(line)['text']
            texts += "".join(text)
            row += 1
    return texts

def save_content(output_file,content):
    with open(output_file,'w',encoding='utf-8') as tx:
        tx.write(str(content))
    return

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder 'data' created !  ---")
    return

if __name__ == '__main__':
    begin = time()
    numbers = ['test', '00', '01']
    number = numbers[2]
    input_file = 'C:/Users/psyji/Dropbox/data/wikiextractor/cnwiki/AA/wiki_{}'.format(number) #test,small
    texts = extract_texts(input_file)
    output_file = '../data/wiki_texts_{}_origin.txt'.format(number)
    mkdir('../data')
    save_content(output_file,texts)
    end = time()
    print("wiki-01 procesing time: %d seconds" % (end - begin))
