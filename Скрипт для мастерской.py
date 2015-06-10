# -*- coding=utf-8 -*-
import os, codecs, re
verbs = []
verbs2 = []
verbs3 = []
verbs_context = {}
samemodel = []
verbs_constr= {}
same_constr = {}
results = {}
words = []

def xhtml(path):
    global verbs, words
    nearwords = []
    f1 = codecs.open('result.csv','w','utf-8-sig')
    f1.write('verb_1;verb_2;same_constr;same_contex\r\n')
    for root,dirs,files in os.walk(path):
        for x in files:
            if x.endswith('.xhtml'):
                f = codecs.open(root + '\\' + x, 'r', 'utf-8-sig')
                for line in f:
                    k = re.findall(u'[А-ЯЁа-яё]+',line.lower())
                    for u in range(0,len(k)):
                        if k[u].lower() in same_constr and u == len(k)-1 and u == 0:
                            break

                        if k[u].lower() in same_constr and u < len(k)-2:
                            words.append(k[u-2].lower())
                            words.append(k[u-1].lower())
                            words.append(k[u].lower())
                            words.append(k[u+1].lower())
                            words.append(k[u+2].lower())
                        if k[u].lower() in same_constr and u == len(k)-1 and u != 0:
                            break
                        if k[u].lower() in same_constr and u == len(k) - 2:
                            break
                        if k[u].lower in same_constr and u == 0:
                            break
                        if k[u].lower in same_constr and u == 1:
                            break






    for verb in same_constr:
        nearwords = []

        for word in range(0,len(words)):
            if words[word] == verb and words[word-2]+' ' +words[word-1]+' '+words[word+1]+' '+ words[word+2] not in nearwords:
                blocknearwords = []
                blocknearwords.append(words[word-2]+' ' +words[word-1]+' '+words[word+1]+' '+ words[word+2])
                nearwords.append(blocknearwords)
        verbs_context[verb] = nearwords


    for verb2 in same_constr:
        verbss = []
        for verb3 in same_constr[verb2]:
            point = 0
            cont = []
            if verb2 != verb3:
                for context in verbs_context[verb2]:
                    for context2 in verbs_context[verb3]:
                        print verb2,verb3
                        if context == context2 and context not in cont:
                            point += 1
                            cont.append(context)
                            if point == 5 and verb3 not in verbss:
                                f1.write(verb2+';'+verb3+';'+ u'Да;'+ str(point) +u'\r\n')
                                verbss.append(verb3)
    f1.close()



def apresjan(file):
    global verbs_constr
    k = 0
    f1 = codecs.open(file,'r','utf-8-sig')
    verbs3 = []
    constr = []
    for line in f1:
        line =  line.split(';')
        if line[15] != u'':
            if line[3] not in verbs3:
                verbs3.append(line[3])
                verbs_constr[verbs3[k-1]] = constr
                constr = []
                k += 1
            if line[3] in verbs3 and line[15] not in constr:
                constr.append(line[15])


    for i in verbs_constr:
        same = []
        for ii in verbs_constr:
            if i != ii:
                for constr1 in verbs_constr[i]:
                    for constr2 in verbs_constr[ii]:
                        if constr1 == constr2 and ii not in same:
                            same.append(ii)
        same_constr[i] = same

    f1.close()





apresjan('ApresianPallBerd.csv')
xhtml('.')
