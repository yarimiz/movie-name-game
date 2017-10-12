# -*- coding: utf-8 -*-

import codecs
import random
from future_builtins import zip

def match(word1, word2):
    if len(word1) != len(word2):
        return False
    combo = zip(word1, word2)
    return any(c1 != c2 for c1, c2 in combo) and all(c1 == c2 for c1, c2 in combo)

def get_movie_list():
    with codecs.open('movie_list.txt', 'r', 'utf-8') as movies_file:
        return [x.strip() for x in movies_file.readlines()]

def get_words_list():
    with codecs.open('WORDS.txt', 'r', 'utf-8') as words_file:
        l = [x.strip() for x in words_file.readlines()]
        return sorted(l, key = lambda x: random.random())

def select_movie(movies_list):
    # return raw_input('Enter movie name: ')
    return random.choice(movies_list)

def get_new_name(movie_name, words_list):
    word_to_replace = random.choice(movie_name.split(' '))
    for word in words_list:
        if match(word, word_to_replace):
            return {
                'old_name' : movie_name,
                'new_name' : movie_name.replace(word_to_replace, word)
                }
    return None

movies = get_movie_list()
words = get_words_list()

RESULTS = []
for _ in range(1):
    selected_movie = select_movie(movies)
    new_name = get_new_name(selected_movie, words)
    if new_name:
        RESULTS.append(new_name)

for r in RESULTS:
    print '##########'
    print 'Old name:' + r['old_name'].encode("utf-8")
    print 'New name:' + r['new_name'].encode("utf-8")
