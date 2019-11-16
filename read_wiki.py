import json

def extract_texts(file):
    texts = ''
    with open(file, encoding='utf-8') as f:
        # each line in the file is a wiki page
        for line in f:
            # read the line as valid json and select text field
            text = json.loads(line)['text']
            texts += text
    return texts

def save_content(content_list):
    with open('wiki_texts_{}.json'.format(number),'w') as tx:
        json.dump(content_list,tx)
    return

def open_texts(json_file):
    return json.loads(open(json_file, 'r', encoding='utf-8').read())

if __name__ == '__main__':
    numbers = ['test', '00', '01']
    number = numbers[0]
    input_file = 'C:/Users/psyji/Dropbox/data/wikiextractor/cnwiki/AA/wiki_{}'.format(number) #test,small
    texts = extract_texts(input_file)
    save_content(texts)
    # texts = open_texts('texts_{}.json'.format(number))