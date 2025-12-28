class WordReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


sentence = "Table Tennis is undoubtedly the best sport to ever exist"
reverser = WordReverser(sentence)
print(reverser.reverse_words())