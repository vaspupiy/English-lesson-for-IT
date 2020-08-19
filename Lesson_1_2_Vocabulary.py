from playsound import playsound
from random import choice

vocabulary = {}
with open('vocabulary.txt', 'r', encoding='utf8') as f:
    for line in f:
        vocabulary[line.rstrip('\n').split(' - ')[0]] = line.rstrip('\n').split(' - ')[1]

print("level 0")
list_vocabulary = list(vocabulary.keys())
while list_vocabulary:
    study_word = choice(list_vocabulary)
    playsound(f'lesson_1_Vocabulary/{study_word}.mp3')
    playsound(f'lesson_1_Vocabulary/{study_word}_translate.mp3')
    print(f'Изучаем слово - "{study_word}", перевод - "{vocabulary[study_word]}"')
    if study_word == input('введите слово на английском: '):
        print(f'Верно, осталось выучить {len(list_vocabulary) - 1} слов(а/о)\n')
        list_vocabulary.remove(study_word)
    else:
        print(f'На этот раз не верно, осталось выучить {len(list_vocabulary)} слов(а/о)\n')
