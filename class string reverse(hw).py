class SentenceReverser:
    def __init__(self, sentence):
        self.__sentence = sentence
    def __split_words(self):  
        return self.__sentence.split()
    def __reverse_words(self, words):
        return words[::-1]
    def get_reversed_sentence(self):
        words = self.__split_words()
        reversed_words = self.__reverse_words(words)
        return ' '.join(reversed_words)
def main():
    user_input = input("Enter a sentence to reverse (word by word): ")
    reverser = SentenceReverser(user_input)
    reversed_sentence = reverser.get_reversed_sentence()
    print("Reversed sentence:", reversed_sentence)
main()
