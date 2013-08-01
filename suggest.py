from random import random
import time
from urllib	import urlopen
from urllib import urlencode

from bs4 import BeautifulSoup
import re
import json
import html5lib
from html5lib import sanitizer
from html5lib import treebuilders

from HTMLParser import HTMLParseError

class SuggestKeywords:
	""" Get Google and Bing correlation keywords """
	_GOOGLE_SUGGEST_URL = 'http://www.google.it/complete/search?output=toolbar&q='
	_BING_SUGGEST_URL = 'http://api.bing.com/osjson.aspx?query='
	_LETTERS = "a"	
	
	@staticmethod
	def getKeywordFromGoogleSuggest(keyword = ""):
		query = keyword.replace(' ','+')
		
		for letter in SuggestKeywords._LETTERS:
			strSearch = query +  "+" + letter 
			print " KW correlata: %s " % (strSearch)
			suggestKwFirstQr = SuggestKeywords.modifyCombinationQuery(strSearch)
			
			strSearch = letter + "+" +  keyword 
			suggestKwSecondQr = SuggestKeywords.modifyCombinationQuery(strSearch)


		return set(suggestKwFirstQr + suggestKwSecondQr)

	@staticmethod
	def modifyCombinationQuery(query):
		wait = random() * 10
		time.sleep(wait);
		parser = BeautifulSoup(urlopen(SuggestKeywords._GOOGLE_SUGGEST_URL + query.encode('utf-8')))
		suggestKeywords = []
		for suggest in parser.find_all('suggestion'):
			suggestKeywords.append(suggest['data'])
			
		return suggestKeywords
		
	@staticmethod
	def getKeywordFromBingSuggest(keyword = ""):
		keywordSuggestion = []
		for letter in SuggestKeywords._LETTERS:
			strSearch = keyword +  "+" + letter 
			page = urlopen(SuggestKeywords._BING_SUGGEST_URL + strSearch)
			data = page.read()
			decode_data = json.load(data)
			for suggest in parser.find_all('p'):
				 print suggest
		return keywordSuggestion
	
	
	
