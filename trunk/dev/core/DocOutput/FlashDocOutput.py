#######################################################################
#AS2docGenerator - documentation generator for actionscript2 classes
#Copyright (C) Tanja Pislar
#
#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
######################################################################

import XMLFilter, StringIO

#flashDocHtml template
#still in the workings..
#requires XMLFilter module from http://www.shearersoftware.com/software/developers/xmlfilter/
# maybe better to change it and use xml.dom instead?


HTML_TEMPLATE_HEAD = """
<html>
<head>
<title>%(title)s</title>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<script language="JavaScript" src="../../_sharedassets/pages.js"></script>
</head>
<body>
"""
HTML_TEMPLATE_TABLE_START="""
<table class="nav" width="100%" border="0" cellpadding="0" cellspacing="0"><tr><td width="100%" align="left"></td>
"""
HTML_TEMPLATE_NAV="""
<td><a href="%(previous)s"><img src="../../_sharedassets/previous.gif" alt="Previous"></a><img src="../../_sharedassets/shim.gif" width="10"  height="1"><a href="%(next)s"><img src="../../_sharedassets/next.gif" alt="Next"></a></td></tr>
"""
HTML_TENPLATE_NAV_END="""
<tr><td colspan="2"><img src="../../_sharedassets/shim.gif" height="4" width="1"></td></tr><tr><td colspan="2"><img src="../../_sharedassets/pixel.gif" height="1" width="100%"></td></tr><tr><td colspan="2"><img src="../../_sharedassets/shim.gif" height="11" width="1"></td></tr></table>
"""
HTML_TEMPLATE_BODY="""
<h1>%(title)s</h1>
%(description)s
"""
HTML_TEMPLATE_TABLE_END="""
<table class="nav" width="100%" border="0" cellpadding="0" cellspacing="0"><tr><td colspan="2"><img src="../../_sharedassets/shim.gif" height="6" width="1"></td></tr><tr><td colspan="2"><img src="../../_sharedassets/pixel.gif" height="1" width="100%"></td></tr><tr><td colspan="2"><img src="../../_sharedassets/shim.gif" height="4" width="1"></td></tr><tr><td width="100%" align="left"></td>
"""
HTML_TEMPLATE_NAV2 = """
<td><a href="%(previous)s"><img src="../../_sharedassets/previous.gif" alt="Previous"></a><img src="../../_sharedassets/shim.gif" width="10"  height="1"><a href="%(next)s"><img src="../../_sharedassets/next.gif" alt="Next"></a></td></tr></table>
"""
HTML_TEMPLATE_FOOT="""
</body>
</html>
"""

xml_toc_Output = StringIO.StringIO()
xml_toc_Handler = XMLFilter.XMLGenerator(xml_toc_Output)
xml_search_Output = StringIO.StringIO()
xml_search_Handler = XMLFilter.XMLGenerator(xml_search_Output)

htmls = []

class FLASHdocGenerator:
	def __init__ (self, theDocumentation):
		self.documentation = theDocumentation
	
	def generateDoc (self, bookName):		
		#create a help_toc.xml and help_search_index.html
		#counter to keep track of generated htmls
		counter = 0
		xml_toc_Handler.startDocument()
		xml_toc_Handler.startElement('book', {'title':bookName, 'directory':bookName, 'language':"en", 'version':"1", 'sort':"mm_5"})
		xml_toc_Handler.startElement('level1', {'name':self.documentation['class']['name']})
		xml_toc_Handler.startElement('level2', {'href':self.documentation['class']['name']+str(counter)+".htm", 'name':self.documentation['class']['name']+" description"})
		xml_toc_Handler.endElement('level2')

		xml_search_Handler.startDocument()
		xml_search_Handler.startElement('book', {'title':bookName, 'directory':bookName})
		xml_search_Handler.startElement('page', {'href':self.documentation['class']['name']+str(counter)+".htm", 'title':self.documentation['class']['name']+" description", 'text':self.documentation['class']['description']})
		xml_search_Handler.endElement('page')

		classDescrHTML = {"url":self.documentation['class']['name']+str(counter)+".htm",
							"previous":"#",
							"next":self.documentation['class']['name']+str(counter+1)+".htm",
							"title":self.documentation['class']['name'],
							"description":self.documentation['class']['description']
						}
		htmls.append(classDescrHTML)

		if self.documentation["methods"]:
			xml_toc_Handler.startElement('level2', {'name':self.documentation['class']['name']+" methods"})	
			for meth in self.documentation["methods"]:
				counter += 1
				xml_toc_Handler.startElement('level3', {'href':self.documentation['class']['name']+str(counter)+".htm", 'name':meth['name']})
				xml_toc_Handler.endElement('level3')
				xml_search_Handler.startElement('page', {'href':self.documentation['class']['name']+str(counter)+".htm", 'title':meth['name'], 'text':meth['description']})
				xml_search_Handler.endElement('page')

				tempHtml = {"url":self.documentation['class']['name']+str(counter)+".htm",
							"previous":self.documentation['class']['name']+str(counter-1)+".htm",
							"next":self.documentation['class']['name']+str(counter+1)+".htm",
							"title":meth['name'],
							"description":"<p>" + meth['description'] + "</p>"
							}
				htmls.append(tempHtml)

			xml_toc_Handler.endElement('level2')
		
		if self.documentation['properties']:
			xml_toc_Handler.startElement('level2', {'name':self.documentation['class']['name']+" properties"})	
			for prop in self.documentation["properties"]:
				counter += 1
				xml_toc_Handler.startElement('level3', {'href':self.documentation['class']['name']+str(counter)+".htm", 'name':prop['name']})
				xml_toc_Handler.endElement('level3')
				xml_search_Handler.startElement('page', {'href':self.documentation['class']['name']+str(counter)+".htm", 'title':prop['name'], 'text':prop['description']})
				xml_search_Handler.endElement('page')

				tempHtml = {"url":self.documentation['class']['name']+str(counter)+".htm",
							"previous":self.documentation['class']['name']+str(counter-1)+".htm",
							"next":self.documentation['class']['name']+str(counter+1)+".htm",
							"title":prop['name'],
							"description":prop['description']
							}
				htmls.append(tempHtml)

			xml_toc_Handler.endElement('level2')

		xml_toc_Handler.endElement('level1')
		xml_toc_Handler.endElement('book')
		xml_toc_Handler.endDocument()

		xml_search_Handler.endElement('book')
		xml_search_Handler.endDocument()

		if not os.path.isdir(bookName):
			os.mkdir(bookName)
		tocFile = open(bookName+"/help_toc.xml", "w")
		print >> tocFile, xml_toc_Output.getvalue()
		tocFile.close()
		searchFile = open(bookName+"/help_search_index.xml", "w")
		print >> searchFile, xml_search_Output.getvalue()
		searchFile.close()
		#todo
		#create a html for every method/property/class description
		for item in htmls:
			m = open(bookName+"/"+item["url"], "w")
			print >> m, HTML_TEMPLATE_HEAD % (item)
			print >> m, HTML_TEMPLATE_TABLE_START
			print >> m, HTML_TEMPLATE_NAV % (item)
			print >> m, HTML_TENPLATE_NAV_END
			print >> m, HTML_TEMPLATE_BODY % (item)
			print >> m, HTML_TEMPLATE_TABLE_END
			print >> m, HTML_TEMPLATE_NAV2 % (item)
			print >> m, HTML_TEMPLATE_FOOT

			m.close()
			

		
if __name__=='__main__':
	import sys, os

	bookName = "TestingClasses"
	theTestClass = {}
	theTestClass['class'] = {'name':"TestClass",
							'version':"1.0",
							'author':"Tanja Pislar",
							'description':"Class used for testing flashDocGenerator",
							'usage':"not to be used in the real world examples",
							'params':['param1 a string', 'param2 a second string']}
	theTestClass['methods'] =[{"name":'methodOne',
							   "description":'description is really basic for method on',
							   "params":['param1 a very basic param', 'param2 more basic params'],
								"returns":'an object of unknown origin',
								"throws":'unknown object exception',
								"usage":'TestClass.methodOne(param1, param2)'},
                              {"name":'methodTwo',
                                "description":'description is really basic for method two',
                                "params":['param1 a very basic param'],
                                "returns":'an object of unknown origin',
                                "throws":'unknown object exception',
                                "usage":'TestClass.methodTwo(param1)'}]
	theTestClass['properties'] = [{'name':'firstProp', 'description':'some description'},
									{'name':'secondProp', 'description':'someother description'}]
	testFlashDocGenerator = FLASHdocGenerator(theTestClass)
	testFlashDocGenerator.generateDoc(bookName)

