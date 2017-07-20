import jieba.analyse as analyse

lines = open("NBA.txt").read()
print " ".join(analyse.extract_tags(lines, topK=20, withWeight=False, allowPOS=()))
l = analyse.extract_tags(lines, topK=20, withWeight=True, allowPOS=())
# for one, two in l:
    # print one + " " + two wrong!!!!!
for ll in l:
    print "%s, %s" % (ll[0], ll[1])


