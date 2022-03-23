class outputText:
    def output(range1, range2, range3):
        output = {}
        for a in range1:
            if a in output:
                output[a].append(str(range1[a]))
            else:
                list = []
                list.append(str(range1[a]))
                output[a] = list
        for b in range2:
            output[b].append(str(range2[b]))
        for c in range3:
            output[c].append(str(range3[c]))
        return output