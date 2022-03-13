from JSONreader import JSONreader
import counter
from CSVGenerator import CSVGenerator
from CaseNormalizer import CaseNormalizer
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


t = str(outputText.output(counter.Counter.counter((CaseNormalizer.proper(feedCreator.create_feed(JSONreader.parse_json(JSONreader.read_json(path, output_path))),
                                                      sep1, sep2))),
                          upperCount.upper((CaseNormalizer.proper(feedCreator.create_feed(JSONreader.parse_json(JSONreader.read_json(path, output_path))),
                                                      sep1, sep2))), percentCounter.percentage((CaseNormalizer.proper(feedCreator.create_feed(JSONreader.parse_json(JSONreader.read_json(path, output_path))),
                                                      sep1, sep2))))).replace(": [",
                                                                                                    ", ").replace("], ",
                                                                                                                  "\n").replace(
        "]}", '').replace('{', '')
NewsGenerator.get_feed((NewsGenerator.generate_feed(target,
                                CaseNormalizer.proper(feedCreator.create_feed(JSONreader.parse_json(JSONreader.read_json(path, output_path))),
                                                      '.', '\n'), '.txt')))

wordReader.generate_csv(target, wordReader.word_reader(CaseNormalizer.proper(feedCreator.create_feed(JSONreader.parse_json(JSONreader.read_json(path, output_path))),
                                                      sep1, sep2)), '.csv')
CSVGenerator.generate_csv(target,t,'.csv')
print(JSONreader.parse_json(JSONreader.read_json(path, output_path)))