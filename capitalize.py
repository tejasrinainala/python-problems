class TextCap:
    def __init__(self):
        self.text = ""

class CapFirLastChar(TextCap):
    def inputText(self):
        self.text = input("Enter text: ")

    def displayCharCap(self):
        words = self.text.split()  
        result = []
        for word in words:
            if len(word) > 1:
                word = word[0].upper() + word[1:-1] + word[-1].upper()
            elif len(word) == 1:
                
                word = word.upper()
            result.append(word)
        return ' '.join(result)


obj = CapFirLastChar()
obj.inputText()
output = obj.displayCharCap()
print("Result:", output)

