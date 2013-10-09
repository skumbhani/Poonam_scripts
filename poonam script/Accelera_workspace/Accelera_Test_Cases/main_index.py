import os
import properties
import codecs

def write_main_index(resultlocation):
    contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"> 
    <html>
    <head> 
    <meta content="text/html; charset=ISO-8859-1" 
    http-equiv="content-type"> 
    <title>Main Index File</title> 
    </head>
    <h2> Main Index</h2>
    <p><b> Test Suite: %s </b>
    <br>Result Index File: <a href='%s'>Index</a><br>
    Coverage Index File: <a href='%s'>Index</a>
    </p>
    </html>
    '''
    contents1 ='''
    <p><b> Test Suite: %s </b>
    <br>Result Index File: <a href='%s'>Index</a></br>
    Coverage Index File: <a href='%s'>Index</a>
    </p>
    '''
    os.chdir(resultlocation)
    mainindexfilepath = os.path.join(resultlocation, 'Main_Index.html')  
    suitename = None
    suitename1 = None
    fh = None
    for dirn,dir,files in os.walk(resultlocation):
        for file in files:
            if 'index.html' in file:
                if 'htmlcov' in dirn or 'Coverage'in dirn:
                    dir1 = os.path.split(os.path.dirname(dirn))
                    suitename = dir1[1]
                    htmlindexfile = os.path.join(dirn,file)
                    htmlindexfile1 = os.path.relpath(htmlindexfile, resultlocation)
                elif 'Results' in dirn:
                    dir2 = os.path.split(os.path.dirname(dirn))
                    suitename1 = dir2[1]
                    resultindexfile = os.path.join(dirn,file)
                    resultindexfile1 = os.path.relpath(resultindexfile, resultlocation)
                if suitename != None and suitename1 != None:
                    if suitename ==  suitename1:
                        if os.path.exists(mainindexfilepath):
                            fh = codecs.open(mainindexfilepath, "a+")
                            fh.write(contents1 % (suitename, resultindexfile1, htmlindexfile1))
                        else:
                            fh = codecs.open(mainindexfilepath, "w+")
                            fh.write(contents % (suitename, resultindexfile1, htmlindexfile1))
        
        
