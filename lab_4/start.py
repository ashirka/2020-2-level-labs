from lab_4.main import WordStorage, encode_text, LikelihoodBasedTextGenerator, decode_text
from lab_4.ngrams.ngram_trie import NGramTrie

if __name__ == '__main__':
    corpus = ('i', 'have', 'a', 'sister', '<END>',
              'her', 'name', 'is', 'kate', '<END>',
              'i', 'have', 'a', 'brother', 'too', '<END>',
              'his', 'name', 'is', 'samuel', '<END>',
              'her', 'name', 'is', 'kate', '<END>')

    storage = WordStorage() 
    storage.update(corpus)
    encoded_text = encode_text(storage, corpus)

    n_gram_trie = NGramTrie(3, encoded_text)
    context = (storage.get_id('i'),
               storage.get_id('have'),)
    generator = LikelihoodBasedTextGenerator(storage, n_gram_trie)
    generated_text = generator.generate_text(context, 3)

    RESULT = decode_text(storage, generated_text)
    print(RESULT)

    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT == ('I have a sister', 'Her name is kate', 'His name is kate'), 'Encoding not working'
