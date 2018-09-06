class Bibli():
    def __init__(self, base_dir):
        path_langu = base_dir + "/SpellChecker/fr_lang"
        f= open(path_langu,"r")
        contents = f.read()
        f.close()
        self.list_words = contents.split("\n")
    def check(self, word):
               
        return word in self.list_words