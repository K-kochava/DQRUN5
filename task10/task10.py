from SQLoutput import SQLoutput
from XMLreader import XMLreader
import counter
from CaseNormalizer import CaseNormalizer
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


t = str(outputText.output(counter.Counter.counter((CaseNormalizer.proper(feedCreator.create_feed(XMLreader.parseXML(path)),
                                                      sep1, sep2))),
                          upperCount.upper((CaseNormalizer.proper(feedCreator.create_feed(XMLreader.parseXML(path)),
                                                      sep1, sep2))), percentCounter.percentage((CaseNormalizer.proper(feedCreator.create_feed(XMLreader.parseXML(path)),
                                                      sep1, sep2))))).replace(": [",
                                                                                                    ", ").replace("], ",
                                                                                                                  "\n").replace(
        "]}", '').replace('{', '')



if __name__ == '__main__':
    SQLoutput.create_connection_wcount(r"C:\sqlite\db\pythonsqlite.db",(wordReader.word_reader(CaseNormalizer.proper(feedCreator.create_feed(XMLreader.parseXML(path)),
                                                      sep1, sep2))))
    SQLoutput.create_connection_letter_count(r"C:\sqlite\db\pythonsqlite.db",t)
