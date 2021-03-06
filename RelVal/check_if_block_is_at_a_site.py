#!/usr/bin/env python -u
import urllib2,urllib, httplib, sys, re, os
import json
import optparse
from xml.dom import minidom


parser = optparse.OptionParser()
parser.add_option('--site', dest='site')
parser.add_option('--block', dest='block')

(options,args) = parser.parse_args()

if options.site == None or options.block == None:
    print "Usage: python2.6 check_if_block_is_at_a_site.py --site SITENAME --block BLOCKNAME"
    sys.exit(0)


site=options.site
block = options.block


#block=["/DoubleMuParked/Run2012D-v1/RAW%23f469d5be-3a9e-11e2-8e2f-842b2b4671d8"

#os.popen("export PYTHON_PATH=/home/relval/WMCore/src/python/")

#os.environ['PYTHONPATH'] = '/home/relval/WMCore/src/python/'
#os.environ['PATH'] = '/home/relval/scripts:/usr/sue/bin:/usr/lib64/qt-3.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin'
#os.environ['LD_LIBRARY_PATH'] = ""
#os.putenv('LD_LIBRARY_PATH','')

#print "hi"

#if len(sys.argv) == 1:
#    os.system('python2.6 delete_this.py oo')

#print "hi2"


subscribed_to_disk=False

url=('https://cmsweb.cern.ch/phedex/datasvc/xml/prod/blockreplicasummary?block='+block).replace('#','%23')
urlinput = urllib.urlopen(url)
#print url
#print urlinput

xmldoc = minidom.parse(urlinput)

complete_at_site=False

for phedex in  xmldoc.childNodes:
    for block in phedex.childNodes:
        for subscription in block.childNodes:
            if subscription.attributes['node'].value == site:
                complete_at_site=True

if complete_at_site:
    sys.exit(1)
else:
    sys.exit(0)
