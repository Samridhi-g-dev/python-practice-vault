from difflib import SequenceMatcher

def get_similarity_ratio(word1, word2):
    return SequenceMatcher(None, word1.lower(), word2.lower()).ratio()*100

def clean_entire_dataset(dirty_list, correct_words, threshold=60):
    cleaned_list = []
    for typo in dirty_list:
        best_match = typo
        highest_sim = 0
        for correct_word in correct_words:
            sim = get_similarity_ratio(correct_word, typo)
            if sim > highest_sim:
                highest_sim = sim
                best_match = correct_word
        if highest_sim >= threshold:
            cleaned_list.append(best_match)
        else:
            cleaned_list.append(typo)
    return cleaned_list



dirty_words = [
    "Tatooine",      # 1. Perfectly correct word
    "Coruscant",     # 2. Perfectly correct word
    "Corusoine",     # 3. Hybrid typo (Coruscant + Tatooine)
    "X-Winger",      # 4. Close to X-Wing, but has extra letters
    "TIE-Wing",      # 5. Hybrid typo (TIE Fighter + X-Wing)
    "Hippogriff",    # 6. Perfectly correct word
    "Hippoflyer"     # 7. Hybrid typo (Hippogriff + Firebolt)
]
correct_words = ["Tatooine", "Coruscant", "X-Wing", "TIE Fighter", "Hippogriff", "Firebolt"]

cleaned_words = clean_entire_dataset(dirty_words, correct_words)
print(f"Original list: {dirty_words}")
print(f"Cleaned list: {cleaned_words}")
word_set = set()
for word in cleaned_words:
    word_set.add(word)
print(f"Cleaned & sorted set: {sorted(word_set)}")
