import os
import HTMLTestRunner
import platform
import codecs
import glob
from time import gmtime, strftime

def run(suite, filepath):
    filePath, fileExtension = os.path.splitext(filepath)
   # print filePath
   # print fileExtension
    filename = os.path.split(filePath)
   # print filename
    resultdir = os.path.join(filename[0], 'Results')
    suitename = os.path.split(filename[0])
    if not os.path.exists(resultdir):
        os.makedirs(resultdir)
    #print filename[1]
   # print resultfile
    os.chdir(resultdir)
    cnt=0
    for files in glob.glob("*.html"):
        if filename[1] in files:
            cnt = cnt+1
    if cnt != 0:
        ext = ("_%s.html" % cnt)
    else:
        ext = ".html"
    resultfile = os.path.join(resultdir, filename[1] + ext)
    print resultfile
    testcasename = filename[1]
    with open(resultfile, "wb") as f:
        HTMLTestRunner.HTMLTestRunner(
                    stream = f,
                    verbosity=2,
                    title='Test execution report',
                    description='Result of tests'
                    ).run(suite)
    f.close()
    write_index(resultfile, suitename[1], testcasename)
    os.chdir(filename[0])

def write_index(resultfile, suitename, testcasename):
    contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"> 
    <html>
    <head> 
    <meta content="text/html; charset=ISO-8859-1" 
    http-equiv="content-type"> 
    <title>Links to result files</title> 
    </head>
    <h2> Index to Result Files</h2>
    <p><br><b>      Test Suite:-&nbsp;&nbsp;&nbsp;%s</b></br>
    <br>Execution Summary:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s</br>
    Test case:-&nbsp;&nbsp;&nbsp;<a href='%s'>%s</a>
    </p>
    </html>
    '''
    contents1 = '''
    <p>Execution Summary:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s
    <br>Test case:-&nbsp;&nbsp;&nbsp;<a href='%s'>%s</a></br>
    </p>
    ''' 
    
    indexfilepath = os.path.split(resultfile)
    indexfilepath1 = os.path.join(indexfilepath[0], "index.html")
    htmlfile = indexfilepath[1].split('.') 
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
   # print indexfilepath1
    fh = None
    if os.path.exists(indexfilepath1):
        fh = codecs.open(indexfilepath1, "a+")
        fh.write(contents1 % (time, indexfilepath[1], testcasename))
    else:
        fh = codecs.open(indexfilepath1, "w+")
        fh.write(contents % (suitename, time, indexfilepath[1], testcasename))
    
                            


    