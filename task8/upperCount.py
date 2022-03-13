import string


class upperCount:
    def upper(text):
        alphabet_string = string.ascii_lowercase.lower()
        result = {}
        for i in alphabet_string:
            counter = 0
            for c in range(len(text)):
                if text[c] == i.upper():
                    counter += 1
            result[i] = counter
        return result