from HTMLParser import HTMLParser

# create a subclass and override the handler methods
def chat_check(data):
    a = data.find(' to ')
    b = data.find('+')
    c = data.find('-')
    print(a,b,c)
    if a!=-1:
        if b!=-1:
            print('num = '+data[b:a])
            print('person = '+data[a+4:])
        elif c!=-1:
            print('num = '+data[c:a])
            print('person = '+data[a+4:])

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
		print(data)
        chat_check(data)

parser=MyHTMLParser()
parser.feed('<font color="#16569E"><font size="2">(12:52:36 PM)</font> <b>n00dles:</b></font> +2 to beans  <br/><font color="#16569E"><font size="2">(12:52:46 PM)</font> <b>beans:</b></font> +100 to n00dles  <br/>')