# coding=gbk
import re

filename = 'F:/data/synop/2019/DM/DM010100.ABJ'
f = open(filename, 'r')
data = f.read()
f.close()
resynop = re.compile(r'(AAXX)\s+(\d{5})\s+(.*?)NNNN', re.S)
syblock = re.findall(resynop, data)
for s in syblock:
    row = re.split('=\n+', s[2])
    for r in row:
        rn = r.replace('\n', ' ')
        if len(rn)>5 and not(re.match('.*[A-Z]', rn)):  #舍去NIL和字母开头站点
            item = s[0]+' '+s[1]+' '+rn.strip()
            print(item)

