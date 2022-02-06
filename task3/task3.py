import re
task = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


def fixspelling(task):
    taskfixed = task.lower()
    return(taskfixed)


def proper(sentence):
    new_words = sentence.split("\n  ")
    j = ''
    for t in new_words:
        new_t = t.split(". ")
        new_t = ". ".join([t.capitalize() for t in new_t])
        j = j + new_t
    return j


def fixis(sentence):
    nsentence = sentence.replace(" iz ", " is ")
    return nsentence


def lstword(sentence):
    new_sentence = ''
    words = sentence.split('.')
    for n in words:
        word = n.split(' ')
        lenw = len(word)
        new_sentence = new_sentence+' '+word[lenw-1]
    new_sentence = new_sentence.strip() + '.'
    new_sentence = new_sentence.capitalize()
    new_sentence = sentence +' '+new_sentence
    return new_sentence


def countspaces(sentence):
    count = 0
    for a in sentence:
        if a.isspace():
            count += 1
    return count


new_task = lstword(fixis(proper(task)))
print('1.Output of fixed text:' + new_task)
print('2. Number of whitespaces in the string: '+ str(countspaces(new_task))+'.')