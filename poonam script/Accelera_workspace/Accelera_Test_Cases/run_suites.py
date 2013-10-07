import unittest
import sys
import os
import properties
import shutil
import main_index

def run_suite():
    curdir = os.getcwd()
    suitefile = os.path.join(curdir, 'suite.conf')
    suites = []
    if os.path.exists(suitefile):
        #print 'yes'
        fh = open(suitefile, 'r')
        for line in fh:
            if 'suite_' in line:
                line = line.replace("\n", "")
                line = line.replace("\t", "")
                line = line.replace("\r", "")
                line = line.lower()
                suites.append(line)
    #print suites
    configfiles = [0]*len(suites)
    #print configfiles
    #print len(configfiles)
    for dirname,dir,files in os.walk(curdir):
        for file in files:
            if 'config' in file:
                 #print dirname
                 suitepath = os.path.split(dirname)
                 suitename = suitepath[1]   
                 suitename = suitename.lower()
                 if suitename in suites:
                     index = suites.index(suitename)
                     #print index
                     configpath = os.path.join(dirname,file)
                     #print configpath
                     configfiles.pop(index)
                     configfiles.insert(index, configpath)
                     #print configfiles
    parentdir = os.path.split(os.getcwd())
    if os.path.exists(os.path.join(properties.Results, parentdir[1])):
        shutil.rmtree(os.path.join(properties.Results, parentdir[1]))
    else:
        os.mkdir(os.path.join(properties.Results, parentdir[1]))
    for each in configfiles:
        sourcedir = os.path.dirname(each)
        os.chdir(sourcedir)
        command = ("nosetests -c %s" % each)
        os.system(command)
        #print each
        suitename = os.path.split(sourcedir)
        destidir = os.path.join(properties.Results, parentdir[1], suitename[1])
        #print sourcedir
        #print destidir
        shutil.copytree(sourcedir, destidir, symlinks=False, ignore=shutil.ignore_patterns('*.py', '*.ini', '*.pyc', '*.coverage'))
    os.chdir(curdir)
        #print suitename
   # main_index.write_main_index()
   # print configfiles,len(configfiles)
             
run_suite()
main_index.write_main_index()

    
