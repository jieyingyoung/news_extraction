import re
import sys
import json
import re
import jieba
from opencc import OpenCC

def open_texts(json_file):
    return json.loads(open(json_file, 'r', encoding='utf-8').read())

# one way of cleaning the texts
def remove_symbles(texts):
    texts_without_symbles =re.findall(r'(\w+)',texts)
    texts_without_digits = [re.sub(r'\d+','',line) for line in texts_without_symbles]
    texts_without_English = [re.sub("[a-zA-z]+","",line) for line in texts_without_digits]
    return texts_without_English

'''
# another way of cleaning the texts to take only the Chinese
def remove_symbles(texts):
    context = texts.decode("utf-8")  # convert context from str to unicode
    filtrate = re.compile(u'[^\u4E00-\u9FA5]')  # non-Chinese unicode range
    context = filtrate.sub(r'', context)  # remove all non-Chinese characters
    context = context.encode("utf-8")  # convert unicode back to str
    return context
'''

#繁体转换为简体
def convert_chinese(string,config):
    # config: 's2t' 是简体转繁体，'t2s' 是繁体转简体
    cc = OpenCC(config)
    return cc.convert(string)

# to cut into tokens
def cut_texts(string):
    return list(jieba.cut(str(string).strip()))


def save_content(output_file,content_list):
    with open(output_file, 'w') as tx:
        json.dump(content_list, tx)
    return

if __name__ == '__main__':
    # input_file = sys.argv[0]
    numbers = ['test', '00', '01']
    number = numbers[0]
    file_path = 'C:/Users/psyji/Dropbox/AI_Course_NLP/__project1__/news_extraction/'
    file = 'wiki_texts_{}.json'.format(number)
    texts_with_symbles = open_texts(file_path+file)
    texts_pure = remove_symbles(texts_with_symbles)
    texts_simple = convert_chinese(str(texts_pure),'t2s')
    tokens = cut_texts(texts_simple)
    print(tokens)
    output_file = '../data/wiki_texts_{}_tokens.json'.format(number)
    save_content(tokens)

