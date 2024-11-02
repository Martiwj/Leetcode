class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.strip().split()

        if len(sentence) == 1:
            return sentence[0][0] == sentence[0][-1]

        i = sentence[0][-1]

        for word in sentence[1:]: 
            j = word[0]
            if i != j:
                return False
            i = word[-1]

        return i == sentence[0][0]