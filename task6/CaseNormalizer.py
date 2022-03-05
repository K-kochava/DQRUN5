class CaseNormalizer:
    def proper(sentence, sep1, sep2):
        if sentence:
            new_words = sentence.split(sep1)
            j = ''
            for t in new_words:
                new_t = t.split(sep2)
                new_t = sep2.join([t.capitalize() for t in new_t])
                j = j + new_t
            return j