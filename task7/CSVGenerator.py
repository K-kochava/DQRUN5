import csv


class CSVGenerator:
    def generate_csv(target, list, ext):
        filename = str(target + 'letter_count' + ext)
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            header = "'letter', 'count_all', 'count_uppercase', 'count_percent'"
            file.write(header)
            file.write('\n')
            for line in list.split('\n'):
                file.write(line)
                file.write('\n')
        return writer
