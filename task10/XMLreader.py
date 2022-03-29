import glob
import xml.etree.ElementTree as ET


class XMLreader:
    def parseXML(path):
        files = glob.glob(path + "/*.xml")
        newsitems = str('')
        if files:
            for filename in files:
                with open(filename) as xml_file:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    for item in root.findall('ad'):
                        newsitems = newsitems.__add__('\n' + str(item.tag) + '\n')
                        for child in item:
                            if child.tag == 'text':
                                newsitems = newsitems.__add__(str(child.text.lstrip(' ')) +'\n')
                            if child.tag == 'date':
                                newsitems = newsitems.__add__(str(child.text.lstrip(' ')) +'\n')
                            else:
                                ()
                    for item in root.findall('news'):
                        newsitems = newsitems.__add__('\n' + str(item.tag) + '\n')
                        for child in item:
                            if child.tag == 'text':
                                newsitems = newsitems.__add__(str(child.text.lstrip(' ')) +'\n')
                            if child.tag == 'city':
                                newsitems = newsitems.__add__(str(child.text.lstrip(' ')) +'\n')
                            else:
                                ()
                    for item in root.findall('forecast'):
                        newsitems = newsitems.__add__('\n' + str(item.tag) + '\n')
                        for child in item:
                            if child.tag == 'city':
                                newsitems = newsitems.__add__(str(child.text.lstrip(' ')) +'\n')
                            else:
                                ()
        return newsitems.strip()
