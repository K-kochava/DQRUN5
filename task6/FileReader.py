from pathlib import Path
import glob


class FileReader:
    def read_file(path, output_path):
        files = glob.glob(path + "/*.txt")
        if files:
            for filename in files:
                f = open(filename)
                d = f.read()
                Path(filename).rename(output_path + "used.txt")
            return d
        else:
            print('Input file not found.')