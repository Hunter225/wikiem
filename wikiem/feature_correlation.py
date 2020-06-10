from wikiem.word_embedder import WordEmbedder
from util.nlp_math import cos_sim
import datetime


def sim(word1, word2, lang):
    word_embedder1 = WordEmbedder(lang)
    word_embedder1.lcs_extraction(word1)
    word_embedder1.transform_lcs_set_to_bow()
    word_embedder1.generate_word_vec()

    word_embedder2 = WordEmbedder(lang)
    word_embedder2.lcs_extraction(word2)
    word_embedder2.transform_lcs_set_to_bow()
    word_embedder2.generate_word_vec()

    similarity = cos_sim(word_embedder1.word_vec, word_embedder2.word_vec)

    return similarity


def en_sim(word1, word2):
    en_similarity = sim(word1, word2, 'en')
    return en_similarity

def zh_sim(word1, word2):
    zh_similarity = sim(word1, word2, 'zh')
    return zh_similarity

def bilingual_sim(word1, word2):

    bilingual_similarity = en_sim(word1, word2) + zh_sim(word1, word2)

    return bilingual_similarity