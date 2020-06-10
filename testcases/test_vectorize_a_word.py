from wikiem.word_embedder import WordEmbedder

def main():
    en_word_embedder = WordEmbedder('en')
    en_word_embedder.lcs_extraction('whisky')
    en_word_embedder.transform_lcs_set_to_bow()
    en_word_embedder.generate_word_vec()
    print(en_word_embedder.word_vec)

    zh_word_embedder = WordEmbedder('zh')
    zh_word_embedder.lcs_extraction('whisky')
    zh_word_embedder.transform_lcs_set_to_bow()
    zh_word_embedder.generate_word_vec()
    print(zh_word_embedder.word_vec)

if __name__ == '__main__':
    main()