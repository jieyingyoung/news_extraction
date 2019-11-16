import json
import os

def extract_texts(file):
    texts = ''
    with open(file, encoding='utf-8') as f:
        # each line in the file is a wiki page
        for line in f:
            # read the line as valid json and select text field
            text = json.loads(line)['text']
            texts += text
    return texts

def save_content(output_file,content):
    with open(output_file,'w') as tx:
        json.dump(content,tx)
    return

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder 'data' created !  ---")
    return

if __name__ == '__main__':
    numbers = ['test', '00', '01']
    number = numbers[0]
    input_file = 'C:/Users/psyji/Dropbox/data/wikiextractor/cnwiki/AA/wiki_{}'.format(number) #test,small
    texts = extract_texts(input_file)
    output_file = '../data/wiki_texts_{}.json'.format(number)
    mkdir('../data')
    save_content(output_file,texts)
