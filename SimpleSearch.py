import nltk
# nltk.download('averaged_perceptron_tagger')




gform_access_issue = 'omit'
form_purchase_request = 'omit'
subitup_duty_calendar = 'omit'
googlesite_duty = 'omit'
googlesite_care = 'omit'
drive_pdf_assigning_care = 'omit'        

# Tags 
tag_dict = {
        gform_access_issue: ['key', 'access', 'issue', "can't", 'starrez'],
        googlesite_care: ['care', 'housing'],
        drive_pdf_assigning_care: ['care', 'housing', 'guide', 'assign']
        }


# Function copied from StackOverflow
# Source: https://stackoverflow.com/questions/40419276/python-how-to-print-text-to-console-as-hyperlink
def convert_link(uri, label=None):
        if label is None: 
                label = uri
        parameters = ''

        # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
        escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'
        return escape_mask.format(parameters, uri, label)

def filter_nouns(word_list:list):
        """Filter out all nouns from a list of words."""
        # Must uncomment nltk.download if this function is used.
        tagged_sentence = nltk.pos_tag(words)
               



def search_for_tag(tag):
        matches = {}

        for key, tags in tag_dict.items():
                if tag in tags:
                        matches = increment_match(key, matches)

        return highest_match(matches)
                

class BasicSearch:
        def search_sentence(self, sentence):
                self._matches = {}
                self._sentence = sentence
                self.generate_word_list()
                for word in self._word_list:
                        self._count_matches(word)
                return self.get_highest_match()



        def generate_word_list(self):
                """Splits a sentence into a list of lowercase words."""
                self._sentence.lower()
                self._word_list = self._sentence.split()


        def _increment_match(self, key):
                """Creates entry for non-existing key.  If key exists.  Increments the number associated with key instead."""
                if key not in self._matches:
                        self._matches[key] = 1
                else:
                        self._matches[key] += 1


        def _count_matches(self, tag):
                """Counts the number of times each result matches the tag."""
                for key, tags in tag_dict.items():
                        if tag in tags:
                                self._increment_match(key)
                

        def get_highest_match(self):
                """Return the dictionary entry with the highest value."""
                return max(self._matches, key=self._matches.get)
                


def main():
        search = BasicSearch()
        while True:
                print("What are you looking for?")
                query = input()
                result = search.search_sentence(query)
                print(result)
                input()
                break





if __name__ == "__main__":
        main()
