from difflib import SequenceMatcher

def get_similarity_ratio(word1, word2):
    return SequenceMatcher(None, word1.lower(), word2.lower()).ratio()*100

# This works with sets of typos and a target word. It returns a new set where typos 
# that are similar enough to the target word (based on the threshold) are replaced with the target word.
def clean_typo_list(target_word, typo_list, threshold=60):
    cleaned_list = []
    for typo in typo_list:
        sim = get_similarity_ratio(target_word, typo)
        if sim >= threshold:
            cleaned_list.append(target_word)
        else:
            cleaned_list.append(typo)
    return cleaned_list

print(f"chair vs table: {get_similarity_ratio('chair', 'table'):.1f}%")
# (Note) .1f% formats the similarity ratio to one decimal place
print(f"Slytherin vs Slitherin: {get_similarity_ratio('Slytherin', 'Slitherin'):.1f}%")
# practical example of cleaning a list of house names with typos
dirty_house_list = ["Gryffindor", "crinffindor", "drifindor", "Slythrin", "grifindoor", "Slytheren", "huflepoof", "rivenclaw", "ravenclaw", "Ravenclaw"]
correct_words = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
for correct_word in correct_words:
    clean_house_list = clean_typo_list(correct_word, dirty_house_list)
    dirty_house_list = clean_house_list

houses = set()
for word in clean_house_list:
    houses.add(word)

print(f"Original list: {dirty_house_list}")
print(f"Cleaned list: {sorted(clean_house_list)}")
print(f"Cleaned list: {sorted(houses)}")