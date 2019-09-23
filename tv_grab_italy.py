#!/usr/bin/python
# coding=utf-8
# This file is part of TVHeadend Script Guida TV
#
# Copyright(c) 2017 Gitner S.M.
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

import subprocess
from optparse import OptionParser

parser = OptionParser(version="%prog 1.0b")
parser.add_option("-d","--description", action="store_true",dest="description",default=False, help="Prints the description of this script")
parser.add_option("-c","--capabilities", dest="capabilities", action="store_true" ,help="Not sure what this is - but saw it in tv_grab_file.", default=False)
(options, args) = parser.parse_args()

if options.description is False and options.capabilities is False:

  # Obtain xml file xml extracting xz archive by shell
  xmltv = subprocess.Popen("wget -qO- http://rytecepg.epgspot.com/epg_data/rytecIT_Basic.xz | xz -cd", stdout=subprocess.PIPE, shell=True)
  file_content = xmltv.stdout.read()

  # Print xml output
  print (file_content)
elif options.description is True:
    print ("TV Italy Basic Grab by URL")
elif options.capabilities is True:
    print ("baseline")
