import ConfigParser
import io
import re
class ConfigurationProvider:
	def __init__(self, cfgFilename="config.cfg"):
		self._cfgFileName = cfgFilename
	
		
	def readSection(self, section, parameter):
		tmpList = []
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.read(self._cfgFileName)
		
		inputAnalysisFile = config.get(section, parameter)
		splitInputAnalysisCfg = re.split(',',inputAnalysisFile)
		for strKey in splitInputAnalysisCfg:
			tmpList.append(strKey.strip())
		return tmpList