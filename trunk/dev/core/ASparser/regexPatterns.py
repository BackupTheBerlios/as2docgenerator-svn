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

killStars = re.compile(r'\*[ ]*')
killTabs = re.compile(r'(\r|\n|\t)')
classPat =  re.compile(r'/\*\*\s[\*| |\t]*(@class|@interface)(.+?)\*/', re.DOTALL)
classNamePat = re.compile('[@class|@interface](.+?)+')
authorPat = re.compile('@author(.+?)+')
usagePat = re.compile('@usage(.+?)[^@]+', re.DOTALL)
descriptionPat = re.compile(r'@description(.+?)[^@]+', re.DOTALL)
versionPat = re.compile('@version(.+?)+')
paramsPat = re.compile('@param[s]* (.+)+')
returnPat = re.compile('@return[s]*(.+?)[^@]+', re.DOTALL)
exceptionPat = re.compile('@throws(.+?)[^@]+', re.DOTALL)
propertyPat = re.compile('@property (.+)+')
methodsPat = re.compile(r'/\*\*\s[\*| |\t]*@method (.+?)\*/', re.DOTALL)
methodNamePat = re.compile('@method(.+?)+')
#seeLinkPat