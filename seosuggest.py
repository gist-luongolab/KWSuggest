import sys

#Local library
from suggest import SuggestKeywords
from configurationProvider import ConfigurationProvider

def storeOnFile(filename, kws):
	out_file = open(filename,"w")
	
	for kw in kws:
	 	out_file.write(kw + "\n")
		print kw
	
	out_file.close()

def getRecursiveCorrelationKw(kwcorr, kws_suggest, deep = 2):
		if deep == 0:
			return kws_suggest
		
		for kwcor in kwcorr:
			kws_suggest.append(kwcor)
			kws = SuggestKeywords.getKeywordFromGoogleSuggest(kwcor)
			kws_suggest += kws
		deep -=1
		return getRecursiveCorrelationKw(kwcorr, kws_suggest, deep)



def main (argv):
	
	cfg = ConfigurationProvider()
	keywords = cfg.readSection('main_configuration','keywords')
	deep = cfg.readSection('main_configuration', 'profondita');
	
	kws_suggest = []
	for keyword in keywords:
		
		filename = "kwcr_%s.txt" % (keyword.replace(' ', '_'))
		print filename
		kwcorr = SuggestKeywords.getKeywordFromGoogleSuggest(keyword)
		kws_suggest += getRecursiveCorrelationKw(kwcorr, kws_suggest, int(deep[0]))

		storeOnFile(filename, kws_suggest)
		
		
	
	

if __name__ == '__main__':
    main(sys.argv)
    


