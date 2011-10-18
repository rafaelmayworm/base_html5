import sublime, sublime_plugin, sys, os, zipfile, re
from os.path import *
sys.path.append('lib')
import source_tools
from xml.etree.ElementTree import ElementTree



class Actionscript3Complete(sublime_plugin.EventListener):
	"""Autocomplete for AS3"""
	
	def on_query_completions(self, view, prefix, locations):
		
		AS3suggestions = []

		# Project reference
		st = source_tools.SourceTools(view.file_name(), os.path.join(sublime.packages_path(), 'ActionScript3'))
				
		is_swc = re.compile('\.swc$')

		for p in st.config["library-path"]:
			lib_path = os.path.join(st.project_path, p) 
			for swc in os.listdir(lib_path):
				# Only swcs
				if not is_swc.search(swc): continue
				#need to get the libs folder and find all the swc files in it
				#as well as the src folders
				myzip = zipfile.ZipFile(os.path.join(lib_path, swc), 'r')
				catalogFile = myzip.open('catalog.xml')
				xmlns = '{http://www.adobe.com/flash/swccatalog/9}'
				tree = ElementTree(file=catalogFile)
				library = tree.find(xmlns+'libraries/'+xmlns+'library')
				libIterator = library.getiterator(xmlns+'script');
				
				for script in libIterator:
					defs = script.findall(xmlns+'def')
					for x in defs:
						fullClassName = x.attrib['id']
						if len(fullClassName) <= 0:
							continue
						temp = str.split(fullClassName,':')
						className = temp[1] if len(temp) > 1 else temp[0]
						description = className + ' - ' + os.path.basename(swc) 
						AS3suggestions.append((description , className))
				
		
		extension_re = re.compile('\\.(as|mxml)$')
		source_paths = [join(st.project_path, p) for p in st.config['source-path']]
		for path in source_paths:
			# all files
			for w in os.walk(path, followlinks=True):
				for f in w[2]:
					# Found something! Check if it's exact or partial...
					package_name = re.sub(extension_re, '', join(w[0], f).replace(path+'/', '').replace('/','.'))
					AS3suggestions.append((re.sub(extension_re, '', f), re.sub(extension_re, '', f)))
		return AS3suggestions


