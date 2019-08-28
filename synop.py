import re

class synop(object):
    def __init__(self, rawsynop):
        raw = re.split('\s+', rawsynop)
        self.all = raw    #ËùÓÐ×Ö¶Î
        self.idt = raw[0]    #±¨¸æ±êÊ¶
        self.day = int(raw[1][0:2])    #ÈÕÆÚ
        self.hour = int(raw[1][2:4])    #Ð¡Ê±£¨¹ú¼ÊÊ±£©
        windunit_d = {'0':'¹À²â·ç£¨m/s£©','1':'·çËÙ¼Æ²â·ç£¨m/s£©','3':'¹À²â·ç£¨kt£©','4':'·çËÙ¼Æ²â·ç£¨kt£©','/':'ÎÞ·çËÙÖµ'}
        self.windunit = raw[1][4]    #·çµÄ±êÊ¶Âë
        self.windunit_e = windunit_d.get(self.windunit)
        self.station = raw[2]    #Õ¾ºÅ
        ispre_d = {'0':'1/3¶Î¾ù±à±¨','1':'1¶Î±à±¨','2':'3¶Î±à±¨','3':'ÒòÎÞ½µË®²»±à±¨','4':'ÒòÈ±²â²»±à±¨'}
        self.ispre = raw[3][0]    #ÊÇ·ñ±à±¨½µË®Á¿µÄÖ¸Ê¾Âë
        self.ispre_e = ispre_d.get(self.ispre)
        isweather_d = {'1':'ÈË¹¤Õ¾±à±¨','2':'ÈË¹¤Õ¾²»±à±¨£¨ÎÞÌìÆø£©','3':'ÈË¹¤Õ¾²»±à±¨£¨È±²â£©','4':'×Ô¶¯Õ¾±à±¨£¨ÍêÕû£©',
                        '5':'×Ô¶¯Õ¾²»±à±¨£¨ÎÞÌìÆø£©','6':'×Ô¶¯Õ¾²»±à±¨£¨È±²â£©','7':'×Ô¶¯Õ¾±à±¨£¨²¿·Ö£©'}
        self.isweather = raw[3][1]
        self.isweather_e = isweather_d.get(self.isweather)


sy = synop('AAXX 31211 51526 31/57 92903 11203 21250 40440 57004 705// 333 05153')
print(sy.isweather_e)
