class HTMLGenerator:
    def __init__(self, title = ''):
        #self.html = ''
        self.html = '<!DOCTYPE html>\n<html>\n<head>\n<title>' + str(title) + '</title>\n</head>\n<body>\n'
        self.ending = '</body>\n</html>'
    
    def addHeading1(self, h1):
        self.html += '<h1>' + str(h1) + '</h1>\n'
    def addHeading2(self, h2):
        self.html += '<h2>' + str(h2) + '</h2>\n'
    def addHeading3(self, h3):
        self.html += '<h3>' + str(h3) + '</h3>\n'
    def addHeading4(self, h4):
        self.html += '<h4>' + str(h4) + '</h4>\n'
    
    def addParagraph(self, p):
        self.html += '<p>' + str(p) + '</p>\n'

    def addLink(self, link, info):
        self.html += '<a href="' + str(link) + '">' + str(info) + '</a>\n'

    def getHTML(self):
        return self.html + self.ending

'''      
h = HTMLGenerator('Hi!')
h.addHeading1('Ovo je heading 1')
h.addHeading3('A ovo je heading 3..')
h.addLink('www.nestonesto.org', 'tvoja keva buras')
h.addParagraph('blabla')
'''
'''
f = open('test.html', 'w')
f.write(h.getHTML())
f.close
'''