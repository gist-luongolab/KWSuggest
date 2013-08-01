import sys

#Local library
from suggest import SuggestKeywords
from configurationProvider import ConfigurationProvider

def getRecursiveCorrelationKw(kwcorr, kws_suggest, deep = 2):
		if deep == 0:
			return kws_suggest
		
		for kwcor in kwcorr:
			kws_suggest.append(kwcor)
			kws = SuggestKeywords.getKeywordFromGoogleSuggest(kwcor)
			kws_suggest += kws
		print "Deep %s" % (str(deep))
		deep -=1
		return getRecursiveCorrelationKw(kwcorr, kws_suggest, deep)



def main (argv):
	
	cfg = ConfigurationProvider()
	keywords = cfg.readSection('main_configuration','keywords')
	
	kws_suggest = []
	for keyword in keywords:
		
		filename = "kw_correlation_%s.txt" % (keyword.replace(' ', '_'))
		out_file = open(filename,"w")
		
		kwcorr = SuggestKeywords.getKeywordFromGoogleSuggest(keyword)
		kws_suggest += getRecursiveCorrelationKw(kwcorr, kws_suggest, 1)
		
		
	for kw in kws_suggest:
	 	out_file.write(kw + "\n")
		print kw
	
	out_file.close()

if __name__ == '__main__':
    main(sys.argv)
