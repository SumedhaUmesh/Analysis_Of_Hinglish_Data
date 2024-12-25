from scraperModule import scrape
from slangDetection import slang
from LanguageDetection import langDet, remove_punc
from Transliteration import trans
from Translation import translate
import demoji
import emoji
import pandas as pd
import string


def output(text):
    out = ""
    with open("Confusion_words.txt", 'r') as f:
        cw = f.readline()
    cw = cw.split()
    text = slang(text.splitlines())

    text = text.lower()
    per = []
    emojid = demoji.findall(text)
    emojiout = '('
    for key, value in emojid.items():
        emojiout = emojiout + key + ": " + value + "  "
    emojiout = emojiout + ')'
    #thank you 🙌❤️ Face reveal 😂😂
    
    text = emoji.get_emoji_regexp().sub("",text)

    for sent in text.split('\n'):
        if sent:

            avg = []
            sent = remove_punc(sent)
            sent = sent.split()
            res, con = langDet(sent, cw)
            Txt1, con = trans(sent, res, con)
            out += Txt1 + "\n"
            per.append(con/len(sent))

            conf = (sum(per)/len(per))*100
            avg.append(conf)

    a = sum(avg)/len(avg)

    if len(emojiout) != 2:
        return [translate(out) + emojiout, a]
    return [translate(out), round(a,2)]


def instaOutput(url):
    scrape(url)
    captionfile = open("insta_caption.txt", "r", encoding='utf-8')
    commentfile = open("insta_comments.txt", "r", encoding='utf-8')
    caption = captionfile.readlines()
    comment = commentfile.readlines()
    correctedcaption = slang(caption)
    correctedcomments = slang(comment)
    return "Caption :\n" + output(correctedcaption)[0] + "\n\nComments :\n" + \
           output(correctedcomments)[0]

def senti(text):
    translation_table = str.maketrans("", "", string.punctuation)
    sentiments = ''
    df = pd.read_csv("sDataset.csv")
    text = text.translate(translation_table)
    text = text.splitlines()
    for sentence in text:
        val = 0
        for each in sentence.split():
            each = each.lower()
            list_ind = list(df[df['Word'] == str(each)].index)
            if len(list_ind) != 0:
                temp = df['Label'].values[list_ind[0]]
                val = val + int(temp)
        if val <= -6:
            sentiments += "Highly Negative\n"
        elif val < 0:
            sentiments += "Negative\n"
        elif val > 0:
            sentiments += "Positive\n"
        else:
            sentiments += "Neutral\n"
    return sentiments
# print(senti(output("""mein tujhe maar dunga
# # mein bahot khush hun""")))