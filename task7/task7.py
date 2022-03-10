import counter
from CSVGenerator import CSVGenerator
from CaseNormalizer import CaseNormalizer
from FileReader import FileReader
from NewsGenerator import NewsGenerator
from feedCreator import feedCreator
from outputText import outputText
from percentCounter import percentCounter
from upperCount import upperCount
from wordReader import wordReader

path = '/Users/kseniya_kochava/Documents/projects/input/'
target = '/Users/kseniya_kochava/Documents/projects/output/'
output_path = '/Users/kseniya_kochava/Documents/projects/input/oldfiles/'
sep1 = '.'
sep2 = '\n'

path1 = NewsGenerator.get_feed((NewsGenerator.generate_feed(target,
                                CaseNormalizer.proper(feedCreator.create_feed(FileReader.read_file(path, output_path)),
                                                      '.', '\n'), '.txt')))
k = FileReader.read_file(path1,output_path)
t = str(outputText.output(counter.Counter.counter(k),
                          upperCount.upper(k), percentCounter.percentage(k))).replace(": [",
                                                                                                    ", ").replace("], ",
                                                                                                                  "\n").replace(
        "]}", '').replace('{', '')
CSVGenerator.generate_csv(target, t, '.csv')
wordReader.generate_csv(target, wordReader.word_reader(k), '.csv')