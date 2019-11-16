import clean_wiki as rsw


if __name__ == '__main__':
    file_path = 'C:/Users/psyji/Dropbox/AI_Course_NLP/__project1__/news_extraction/'
    input_file = 'news_texts_origin.json'
    texts_original = rsw.open_texts(file_path+input_file)
    texts_pure = rsw.remove_symbles(texts_original)
    tokens = rsw.cut_texts(texts_pure)
    print(tokens)
    output_file = '../data/news_texts_tokens.json'
    rsw.save_content(output_file,tokens)


