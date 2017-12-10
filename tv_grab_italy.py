#!/usr/bin/python
# coding=utf-8
# This file is part of TVHeadend Script Guida TV
#
# Copyright(c) 2017 Stefano Mastrodomenico
#
# This script takes over a part of the code 
# written by Mathias F. Svendsen - okey.dk
# and Andrea Draghetti - andreadraghetti.it
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 3 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import io
import os
import gzip
import StringIO
from urllib2 import urlopen
from optparse import OptionParser

parser = OptionParser(version="%prog 1.0b")
parser.add_option("-d","--description", action="store_true",dest="description",default=False, help="Prints the description of this script")
parser.add_option("-c","--capabilities", dest="capabilities", action="store_true" ,help="Not sure what this is - but saw it in tv_grab_file.", default=False)
(options, args) = parser.parse_args()

if options.description is False and options.capabilities is False:
  url = "http://rytecepg.ipservers.eu/epg_data/rytecIT_Basic.gz"
    
  # Scarico il file GZ
  gzFile = urlopen(url)
  compressedFile = StringIO.StringIO()
  compressedFile.write(gzFile.read())
  
  # Imposto la posizione corrente del file
  # all'inizio in modo che gzip.GzipFile possa
  # leggere il contenuto dal principio
  compressedFile.seek(0)

  # Decomprimo il file GZ    
  decompressedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
  file_content = decompressedFile.read()

  print (file_content)
elif options.description is True:
    print ("TV Italy Basic Grab by URL")
elif options.capabilities is True:
    print ("baseline")