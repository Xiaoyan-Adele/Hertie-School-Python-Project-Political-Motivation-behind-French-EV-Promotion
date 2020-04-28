import unittest
from Team_Project_Topic_Modeling_LDA import remove_stopwords

class TestRemove_stopwords(unittest.TestCase):
    def setUp(self):
        self.remove_stopwords = remove_stopwords()
    
    from spacy.lang.fr.stop_words import STOP_WORDS
    tokens = ["c'est", 'un','plaisir']
    
    def remove_stopwords(tokens):
        filtered_list =[]
        for it in tokens:
            temp = []
        for word in it:
            if(word not in STOP_WORDS):
                temp.append(word)
        filtered_list.append(temp)
        temp=[] 
    return filtered_list

    tokens.assertEqual(filtered_list,tokens)

        
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()