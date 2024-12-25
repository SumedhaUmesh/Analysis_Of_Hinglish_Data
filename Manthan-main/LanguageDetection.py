import enchant

d = enchant.Dict('en')


def remove_punc(txt):
    punc = '•.,:;!@#$%&*•?()-\"'
    for each in txt:
        if each in punc:
            txt = txt.replace(each, "")
    return txt


def langDet(doc, cw):
    res = []
    con = 0

    for i, each in enumerate(doc):
        if each in cw:
            nxt = ''

            if len(doc) != i + 1:
                if doc[i + 1] in cw:
                    nxt = 'hi'
                elif d.check(doc[i + 1]):
                    nxt = 'en'
                else:
                    nxt = 'hi'
            if nxt == 'hi':
                res.append('hi')
            else:
                if res:
                    res.append(res[-1])
                else:
                    res.append('hi')
        else:
            if d.check(each):
                res.append("en")
                con += 1
            else:
                res.append("hi")

    return (res, con)
