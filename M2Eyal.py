#A

def reverse(sentence, reverse_word):
 try:
    new = sentence
    if reverse_word in sentence:
            word_len = len(reverse_word)
            word_index = new.index(reverse_word)
            part1 = new[:word_index]
            part2 = new[word_len + word_index:]
            r = reverse_word[::-1]
            end = part1 + r + part2
            return (end)
    else:
            return ("The word was not found")
 except:
     return "invalid input"

reverse("I like apples and I also like bananas", "like")

