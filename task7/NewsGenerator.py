class NewsGenerator:
    def generate_feed(target, text, ext):
        filename = str(target + 'news_generated' + ext)
        outFile = open(filename, "w")
        outFile.write(str(text))
        outFile.close()
        return outFile

    def get_feed(outFile):
        path = str(outFile).strip("<_io.TextIOWrapper name=").strip("news_generated.txt' mode='w' encoding='UTF-8'>")
        return path
