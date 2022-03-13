import glob
import json
import shutil


class JSONreader:
    def read_json(path,output_path):
        files = glob.glob(path + "/*.json")
        if files:
            for filename in files:
                with open(filename) as json_file:
                    data = json.load(json_file)
            return data
        else:
            print('Input json file not found.')

    def parse_json(text):
        output = str(text).lower().replace(':','\n').replace('},','\n\n').replace("'text'",'').replace("'city'",'').replace("'date'",'').replace('{','').replace('}','\n').replace("'feed'",'').replace("', ",'').replace("'",'').replace("'\n", "")
        output = output.replace('forecast\n','forecast').replace('news\n','news').replace('ad\n','ad').replace(' \n','\n').replace('\n ','\n').strip()
        return output