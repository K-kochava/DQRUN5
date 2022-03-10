import csv


class wordReader:
    def word_reader(text):
        text = text.lower()
        list = str(len(text.split()))
        return list

    def generate_csv(target, list, ext):
        filename = str(target + 'count_word' + ext)
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            header = 'Word Count'
            file.write(header)
            file.write('\n')
            file.write(str(list))
            file.write('\n')
        return file