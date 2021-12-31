from bs4 import BeautifulSoup #deixar o html mais clean
import requests #fazer requisao http
import operator #operadores 
from collections import Counter # ajudar na manipulação de listas e tuplas

def start(url):

    wordlist = [] #armazenas o conteudo do site
    source_code = requests.get(url).text 



    soup = BeautifulSoup(source_code, 'html.parser') #pegar a requisao e transformar em html

    
    for each_text in soup.findAll('div', {'class': 'entry-content'}): #procura td com div em class no html
        content = each_text.text #transformar em string
				


        words = content.lower().split() # vai armazenar td dentro da words em letra minuscula e separado por linhas


        for each_word in words:
            wordlist.append(each_word)

        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    """
	Remove Simbolos na wordlist
    """
    clean_list=[]
    for word in wordlist:
        symbols = '!@#$%¨&*()_-+={[]{|/;:"<>?\., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_wordlist(word)

    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}
	
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1




    for key, value in sorted(word_count.items(),
                            key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)



start("")


