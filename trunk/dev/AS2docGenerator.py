#######################################################################
#AS2docGenerator - documentation generator for actionscript2 classes
#Copyright (C) Tanja Pislar contact: klaut@klaustrofobik.org
#
#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
######################################################################

import sys
import os
import stat
import string
import getopt
from optparse import OptionParser

import core.ASparser.ASparser as ASparser
import core.DocOutput.htmlDocOutput as htmlDocOutput
import core.DocOutput.FlashDocOutput as FlashDocOutput

#this function found on http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/161542
def walktree (top, depthfirst = True):

    names = os.listdir(top)
    if not depthfirst:
        yield top, names
    for name in names:
        try:
            st = os.lstat(os.path.join(top, name))
        except os.error:
            continue
        if stat.S_ISDIR(st.st_mode):
            for (newtop, children) in walktree (os.path.join(top, name), depthfirst):
                yield newtop, children
    if depthfirst:
        yield top, names

class AS2docGenerator:
	def __init__ (self, filename, newFile):
		self.version = "AS2docGenerator beta 0.5.4"
		self.newFilename = newFile
		self.ASparser = ASparser.ASparser(filename)
		self.documentation = self.ASparser.parse()

	def writeDoc (self, theType = "html", bookName="flashdocs"):
		if theType=="html":
			theGenerator =htmlDocOutput.HTMLdocGenerator(self.documentation)
			theGenerator.generateDoc(self.version, self.newFilename)
		elif theType=="flashdoc":
			theGenerator =  FlashDocOutput.FLASHdocGenerator(self.documentation)
			theGenerator.generateDoc(bookName)




if __name__=='__main__':

	# parsing option arguments
	usage = """usage: %prog [options] arg1 [arg2,..]
	type %prog -h for help"""

	version ="%prog beta-0.5.4"
	parser = OptionParser(usage=usage, version=version)
	parser.add_option("-o", "--out", dest="output", default="html",
                  help="""the output format of the documentation 
						options: html|flashdoc""")

	(options, args) = parser.parse_args()

	if len(args) == 0:
		print parser.error("incorrect number of arguments")

	else:
		
		if options.output == "html":
			#print args
			print "generating html documentation..."
			################################################
			end = ".html"
			o = args[0]
			if os.path.isdir(o):
				d = os.getcwd()
				ndir = os.path.join(d, '_docs')
				if not os.path.exists(ndir):
					os.makedirs(ndir)

				for (basepath, children) in walktree(o):
					for child in children:
						print os.path.join(basepath, child)
						f = os.path.join(basepath, child)

						if os.path.isfile(f):
							newname = os.path.basename(f)
							ext = string.lower((os.path.splitext(f))[1])[1:]
							if ext=="as":
								try:
									newname = newname[:newname.index(".")] + "_doc" + end
									newFile = os.path.join(ndir, newname)
									theDoc = AS2docGenerator(f, newFile)
									theDoc.writeDoc()
								except Exception, e:
									print e
									continue
						
			else:
				fname = o
				newname = os.path.basename(fname)
				theDir = os.path.dirname(fname)
				try:
					if "." not in newname:
						raise Exception("### ERROR: the filename provided does not seem to be a correct file name or directory.\nPlease, check the filename and try again [hint: classfile.as]")

					newname = newname[:newname.index(".")] + "_doc" + end
					newFile = os.path.join(theDir, newname)

					theDoc = AS2docGenerator(fname, newFile)
					theDoc.writeDoc()
				except Exception, e:
					print e
			################################################
		elif options.output == "flashdoc":
		# FINISH IT -- right now it does not work
			print "generating flashdoc documentation... in the next revision."
			#f = args[0]
			#if os.path.isfile(f):
				#newname = os.path.basename(f)
				#ext = string.lower((os.path.splitext(f))[1])[1:]
				#if ext=="as":
					#try:
						#newname = newname[:newname.index(".")]


	# ideas for the next revision:
	# -d(dir) dirName -o(output) outputFormat(html|flashdoc|xml) -b(book name for flashdoc) bookName -i(input) .as files or directory of .as files
	# example 1:
	# AS2docGenerator.exe -d myDir -o flashdoc -b myClasses class1.as class2.as class3.as
	# example 2:
	# AS2docGenerator.exe -d myDir -o html -i classesDir