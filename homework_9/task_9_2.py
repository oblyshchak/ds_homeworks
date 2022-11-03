class TextProcessor:
    def __init__(self):
        self.__flag = False
        
    def get_clean_string(self, sentence):
        result = ""
        for i in sentence:
            if not self.__is_punctuation(i):
                result += i
        return result
 
    def __is_punctuation(self, letter):
        if letter.isalnum():
            self.__flag = False
        else:
            self.__flag = True
        return self.__flag
        
                
first = TextProcessor()
print(first.get_clean_string('...8755jk---&&&111??jgg'))

class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ""
        
    @property
    def clean_string(self):
        print("Printing clean string")
        return self.__clean_string
        
    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

loader = TextLoader()
loader.set_clean_text('sdfsdf----sdf-???')

print(loader.clean_string)

class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()
        
    def process_text(self, list_strings: list):
        for sentece in list_strings:
            self._text_loader.set_clean_text(sentece)
            print(self._text_loader.clean_string)
            
data = DataInterface()
data.process_text(['!!!kll', '//uuu', 'ppdd6776z///,,..'])

