from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import pandas as pd
import string


df_hi = pd.read_csv("hinglish-hindi.csv")


def trans(txt, res, con):
    transliterated = ''
    for index, i in enumerate(txt):
        if res[index] == 'hi':
            flag = False
            i = i.translate(str.maketrans('', '', string.punctuation)).lower()  # removing punctuation
            for j in range(df_hi.shape[0]):
                Hing = df_hi['Hinglish'].values[j]
                if i.lower() == Hing:
                    transliterated += df_hi['hindi'].values[j] + " "
                    con += 1
                    flag = True
                    break

            if not flag:
                each = transliterate(i, sanscript.ITRANS, sanscript.DEVANAGARI)
                transliterated += each + " "
        else:
            transliterated += i + " "

    return (transliterated, con)
