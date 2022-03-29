import string


class percentCounter:
    def percentage(text):
        total = len(text)
        text = text.lower()
        alphabet_string = string.ascii_lowercase.lower()
        result = {}
        for i in alphabet_string:
            counter = 0
            for c in range(len(text)):
                if text[c] == i:
                    counter += 1
                    percent = (counter / total) * 100
            result[i] = percent
        return result