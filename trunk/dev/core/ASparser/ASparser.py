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

import re
from regexPatterns import *

class ASparser:
	def __init__ (self, filename):
		fp = open(filename)
		self.content = fp.read()
		fp.close()

		self.datatype = None

		try:
			self.classStuff = classPat.search(self.content)
			self.datatype = self.classStuff.group(1)[1:]
			self.classStuff = self.cleanStars(self.classStuff.group(1,2))

		except AttributeError, e:
			self.classStuff = "none"
			msg="### ERROR in file %s: @class or @interface tag is required. " % (filename)
			raise Exception(msg)
			#print msg

		self.methods = methodsPat.findall(self.content)

		self.documentation = {}

	def cleanStars (self, output):
		newOutput = []
		for line in output:
			line.rstrip()
			newOutput.append(re.sub(killStars, '', line))
		return "".join(newOutput)

	def findParams (self, text):
		m = paramsPat.findall(text)
		if m:
			return m

	def findProperties (self, text):
		m = propertyPat.findall(text)
		all = []
		for prop in m:
			p = re.split('[ ]+',prop, maxsplit=1)
			try:
				desc = p[1]
			except:
				desc = "No description provided."
			temp = {'name':p[0], 'description':desc}
			all.append(temp)
		return all

	def findParts (self, pattern, theString):
		returnStr = "Documentation not provided."
		try:
			temp = pattern.search(theString)
			templist = re.split('[ ]+',temp.group(0), maxsplit=1)
			return templist[1]
		except:
			return returnStr

	def findMethods(self, methods):
		allMeths=[]
		for meth in methods:
			metha = re.sub(killStars, '', meth)
			name = metha[:metha.index("\n")].rstrip()
			description = self.findParts(descriptionPat, metha)
			params = self.findParams(metha)
			returns = self.findParts(returnPat, metha)
			throws = self.findParts(exceptionPat, metha)
			usage = self.findParts(usagePat, metha)
			aMeth = {"name":name,
					"description":description,
					"params":params,
					"returns":returns,
					"throws":throws,
					"usage":usage}
			allMeths.append(aMeth)
		return allMeths

	def parse (self):
		self.documentation['class'] = {'name':self.findParts(classNamePat, self.classStuff ),
									'version':self.findParts(versionPat, self.classStuff ),
									'author':self.findParts(authorPat, self.classStuff ),
									'description':self.findParts(descriptionPat, self.classStuff),
									'usage':self.findParts(usagePat, self.classStuff),
									'params':self.findParams(self.classStuff),
									'type':self.datatype}
		self.documentation['methods'] = self.findMethods(self.methods)
		self.documentation['properties'] = self.findProperties(self.content)

		return self.documentation