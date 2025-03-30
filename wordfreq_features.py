from wordfreq import word_frequency

def extract_features_from_word(word):
    word = word.lower()
    vowels = sum(1 for c in word if c in 'aeiou')
    rare_letters = sum(1 for c in word if c in 'qzxjk')
    has_duplicates = int(len(set(word)) < len(word))
    frequency = word_frequency(word, 'en')

    return {
        'frequency': frequency,
        'vowel_count': vowels,
        'rare_letter_count': rare_letters,
        'has_duplicates': has_duplicates
    }