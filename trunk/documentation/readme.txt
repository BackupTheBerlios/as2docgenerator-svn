**********************************************

	AS2docGenerator beta-0.5		     

**********************************************

Author: Tanja Pislar <klaut@klaustrofobik.org>
Last Modified: 	19.june 2004

-----------------------------------------------
history:
-----------------------------------------------
	19.jun 2004 - added support for the @interface tag
				- added support for the recursive walk through directories of .as files
				
	30.nov 2003 - if the @class tag is missing, AS2doGenerator now prints an error:
					"### ERROR: @class tag is required"
				- corrected a bug that prevented from correctly saving files with relative paths.
	
	22.nov 2003 - added @usage tag for methods
				- added "description" html heading for methods

------------------------------------------------
Usage:
------------------------------------------------
from commandPrompt:
1) single.as file
	C:\> [path to]AS2docGenerator.exe [path to]AS2class.as
this generates a AS2class_doc.html file in the same directory AS2class.as is in.

2) supplying a directory containing .as files (or more diretcories with .as files)
		C:\> [path to]AS2docGenerator.exe [path to]AS2classDirectory
this generates a _docs directory in the same directory where the AS2classDirectory was called from. All the asClass_doc.html files are in the _docs directory.
	

It can be also used from EditPlus or SciteFlash or other text editors that support "user tools" configuration.

A sample of a commented dummy .as class file: SampleClass.as
Generated documentation: SampleClass_doc.html


-----------------------------------------------------
Tags supported in the .as file:
-----------------------------------------------------
	@class (required)
	@interface (required)
	@author
	@version 
	@description
	@usage
	@param

	@property

	@method
	@description
	@usage
	@param
	@return
	@throws



----------------------------------------------------------
some of the HTML tags that can be used in the .as file:
----------------------------------------------------------
	<P>
	<code>
	<pre>
	<blockquote>
	<b>
	<a>
	<tt>

