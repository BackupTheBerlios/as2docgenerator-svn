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

import time

today = time.strftime("%c")

defCss = """
		<STYLE><!--
		HR.small{height:1px; width:100%; background:#E7BFA3; border: 0px;}
		HR.big{height:4px; width:100%; background:#E7BFA3; border: 0px;}
		A:hover{text-decoration: underline}
		A{text-decoration: none; color: #993333}
		code{font-family:monospace; font-size: 12px; color: #666666;}
		.methodAttributesTitle{font-size: 12px; font-weight: bold; color: #7B779C}
		.ToC{font-size: 12px; font-weight: bold; color: #993333}
		.methodTitle{font-size: 14px; font-weight: bold; color: #993333}
		.groupTitle{font-size: 18px; font-weight: bold; color: #993333}
		.sectionTitle{font-size: 22px; font-weight: bold; color: #993333}
		.majorTitle{font-size: 32px; font-weight: bold; color: #993333; padding-bottom:100px;}
		.methodsDiv{margin-left:40px;}
		.footer{font-size: 11px; color: #666666;}
		body{font-family: arial,sans-serif; font-size: 12px;}
		//--></STYLE>
		"""

class HTMLdocGenerator:
	def __init__ (self, theDocumentation, defcss=defCss):
		self.css = defcss
		self.documentation = theDocumentation

	def generateDoc (self,theGenVersion,theFile):
		self.out = open(theFile, "w")

		#header
		print >> self.out,  """
		<HTML>
		<HEAD>
		<TITLE>%s  Documentation</TITLE>
		%s
		</HEAD>
		<BODY bgColor='white'>
		<P class='majorTitle'>%s Documentation</P>
		""" % (self.documentation["class"]['name'],self.css,self.documentation["class"]['name'])

		#author, time
		print >> self.out,  """
		<P><B>Author:</B> %(author)s<BR>
		<B>Last Modified:</B> """ % (self.documentation["class"]) + today + """<HR class='big'>"""

		#table of contents
		print >> self.out,  """
		<P class='sectionTitle'>Summary</P>
		<P class='ToC'>%(name)s %(type)s:</P>
		<div class='methodsDiv'><a href='#classinfo'>- description</a></div>""" % self.documentation["class"]
		if self.documentation['properties']:
			print >> self.out, "<P class='ToC'>%(name)s Properties:</P><div class='methodsDiv'>" % self.documentation["class"]
			for prop in self.documentation['properties']:
				print >> self.out, "<a href='#%(name)s'>- %(name)s</a><br>" % prop
			print >> self.out, "</div><br>"
		if self.documentation["methods"]:
			print >> self.out,  "<P class='ToC'>%(name)s Methods:</P><div class='methodsDiv'>" % self.documentation["class"]
			for meth in self.documentation["methods"]:
				print >> self.out, "<a href='#%(name)s'>- %(name)s</a><br>" %  meth
			print >> self.out, "</div><br>"

		#class description
		print >> self.out, """
		<HR class='big'>
		<P class='sectionTitle'><A name='classinfo'></A>%(name)s <I>%(type)s</I></P>
		<P> <span class='methodTitle'>version:</span> %(version)s</P>
		<P class="methodTitle">description:</P>
		<P>%(description)s</P>
		<P class="methodTitle">usage:</P> %(usage)s""" %  (self.documentation["class"])
		if self.documentation["class"]["params"]:
			print >> self.out,  '''<P> <span class='methodTitle'>parameters:</span>
				<ul> '''
			for p in self.documentation["class"]["params"]:
				print >> self.out,  '<li>%s</li>' % p
			print >> self.out, "</ul>"
		print >> self.out, "<p><a href='#'>back to top</a></p>"

		# class properties
		if self.documentation['properties']:
			print >> self.out,  """
			<HR class='small'>
			<P class='groupTitle'><A name='properties'></A>%(name)s Properties:</P>
			<div class='methodsDiv' >
			""" %  (self.documentation["class"])
			for prop in self.documentation['properties']:
				print >> self.out,  """
				<P class='methodTitle'><A name='%(name)s'></A><u> %(name)s</u></P>
				<P> %(description)s</P>""" % prop
			print >> self.out, "<p><a href='#'>back to top</a></p>"
			print >> self.out,  "</div>"

		# class methods
		if self.documentation["methods"]:
			print >> self.out,  """
			<HR class='small'>
			<P class='groupTitle'><A name='methods'></A>%(name)s Methods:</P>
			<div class='methodsDiv' >
			""" %  (self.documentation["class"])
			for meth in self.documentation["methods"]:
				if not meth["params"]: del meth["params"]
				if meth["throws"] == "Documentation not provided.": del meth["throws"]
				if meth["returns"] == "Documentation not provided.": meth["returns"] ="Void."
				print >> self.out,  """
				<P class='methodTitle'><A name='%(name)s'></A><u> %(name)s</u></P>
				<P><span class='methodAttributesTitle'>description: </span>
				%(description)s</P>
				<P><span class='methodAttributesTitle'>usage:</span> %(usage)s</P>""" % meth
				if meth.has_key("params"):
					print >> self.out,  "<P> <span class='methodAttributesTitle'>parameters:</span><ul>"
					for p in meth["params"]:
						print >> self.out, "<li>%s</li>" % p
					print >> self.out, "</ul></P>"
				if meth.has_key("throws"):
					print >> self.out, "<P> <span class='methodAttributesTitle'>throws:</span> %(throws)s</P>" % meth
				print >> self.out, "<P><span class='methodAttributesTitle'>returns:</span> %(returns)s</P>" % meth
				print >> self.out, "<p><a href='#'>back to top</a></p>"
			print >> self.out, "</div>"

		#footer
		print >> self.out, """
			<BR>
			<BR>
			<HR class='big'>
			<span class="footer">generated with <A href='http://blog.klaustrofobik.org/' target='_blank'>%s</A></span>
			</BODY>
			</HTML>
			""" % (theGenVersion)
		self.out.close()
		print "documentation generated successfully."
		print "files generated: " + theFile


