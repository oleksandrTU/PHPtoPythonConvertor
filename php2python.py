
tabul = 0

def onceReplace(lineNumber,oldPhrase,newPhrase):
    console.write("onceReplace is called" + " \n")
    s = editor.getLine(lineNumber)

    if (oldPhrase in s): 
        j_end = editor.getLineEndPosition(lineNumber)
        j_beg = j_end - len(editor.getLine(lineNumber)) + 2
        fbeg = s.index(oldPhrase)
        editor.deleteRange(j_beg + fbeg, len(oldPhrase))
        editor.insertText(j_beg + fbeg, newPhrase)   
    	s = editor.getLine(lineNumber)        
    else:    
        return 1  
            

def forReplace(lineNumber,oldPhrase,newPhrase):
    s = editor.getLine(lineNumber)
    for nn in range (1,8):
        if (oldPhrase in s): 
            j_end = editor.getLineEndPosition(lineNumber)
            j_beg = j_end - len(editor.getLine(lineNumber)) + 2
            fbeg = s.index(oldPhrase)
            editor.deleteRange(j_beg + fbeg, len(oldPhrase))
            editor.insertText(j_beg + fbeg, newPhrase)   
    	    s = editor.getLine(lineNumber)        
        else:    
            return 1  

def lonlyIf(lineNumber):

    s = editor.getLine(lineNumber) 
    console.write("lif is called" + s + " \n")
    j_end = editor.getLineEndPosition(lineNumber)
    j_beg = j_end - len(editor.getLine(lineNumber)) + 2      
    if ("if(" in s):
        in_if = s.index("if(") + 1
        ii = s.index("(",in_if) + 1
        brekats = 1
        break_cond = 1
        #console.write("lif is called" + str(ii) + " \n")
        while (break_cond):
            c = "%c" % editor.getCharAt(j_beg + ii)
            #console.write("c = " + c + " \n")
            if (c == "("):
                brekats = brekats + 1;
            elif (c == ")"):
                brekats = brekats - 1;
            else:
                pass
            if (brekats == 0):
                break_cond = 0
                brek_pos_bg = j_beg  + ii+1
            ii = ii + 1
        end_cond = 1
        while (end_cond):
            c = "%c" % editor.getCharAt(j_beg + ii)
            if (c == ";"):
                end_cond = 0
                brek_pos_end = j_beg  + ii + 2     
            elif (c == "{"):
                return 1             
            else: 
                pass
            ii = ii + 1 
        editor.insertText(brek_pos_bg,"{")
        editor.insertText(brek_pos_end,"}")
        
def lonlyElse(lineNumber):
    
    s = editor.getLine(lineNumber) 
    console.write("lel is called" + s + " \n")	
    j_end = editor.getLineEndPosition(lineNumber)
    j_beg = j_end - len(editor.getLine(lineNumber)) + 2      
    if ("else" in s):
        ii = s.index("else") + 4
        brek_pos_bg = ii+j_beg
        #console.write("lel is called" + str(ii) + " \n")
        end_cond = 1
        while (end_cond):
            c = "%c" % editor.getCharAt(j_beg + ii)
            #console.write("else " + c + " \n")
            if (c == ";"):
                end_cond = 0
                brek_pos_end = j_beg  + ii + 2     
            elif (c == "{"):
                return 1             
            else: 
                pass
            ii = ii + 1 
        editor.insertText(brek_pos_bg,"{")
        editor.insertText(brek_pos_end,"}")        
    
def longComments(contents, lineNumber, totalLines):
    s = editor.getLine(lineNumber)    
    if ("/*" in contents):
    	if ("*/" in contents):
            fbeg = s.index("*/") + 2
            if (fbeg == len(s)):
                forReplace(lineNumber,"/*","#")
                return 1
            else:
                j_end = editor.getLineEndPosition(lineNumber)
                j_beg = j_end - len(editor.getLine(lineNumber)) + 2
                #forReplace(lineNumber,"/*","#")
                editor.insertText(j_beg + fbeg,"\r\n")  
                forReplace(lineNumber,"/*","#")
                return 1
        else:
            forReplace(lineNumber,"/*","#")
        ii = 1
        s = editor.getLine(lineNumber + ii)    
        while ("*/" not in s):
            j_end = editor.getLineEndPosition(lineNumber+ii)
            j_beg = j_end - len(editor.getLine(lineNumber+ii)) + 2
            editor.insertText(j_beg,"# tp1")
            ii = ii + 1
            s = editor.getLine(lineNumber + ii)    
        j_end = editor.getLineEndPosition(lineNumber+ii)
        j_beg = j_end - len(editor.getLine(lineNumber+ii)) + 2
        editor.insertText(j_beg,"# tp1")
        return ii
        
def forfinReplace(contents, lineNumber, totalLines):
    forReplace(lineNumber,"//","#") 
    if (commentsLine(lineNumber)):
        return 1
    forReplace(lineNumber,"printf","#commented printf")
    forReplace(lineNumber,"print_r","#commented printr") 

def countOpenings(contents):
    console.write("countOpenings " + contents)	
    count = 0
    for i in range(0,len(contents)):
        if contents[i] == "\"":
            count = count + 1

    if count % 2 == 0:
        return True
    else:
        return False
           

        
def fortextReplace(contents, lineNumber, totalLines):
    console.write("fortextReplace " + editor.getLine(lineNumber)  + " \n")	

    if ("\"" in contents):
        s = editor.getLine(lineNumber) 
        oddOpening = countOpenings(s);
        if not oddOpening:
            ii = 1
            j_end = editor.getLineEndPosition(lineNumber)
            editor.insertText(j_end,"\\")
            s = editor.getLine(lineNumber + ii)
    	    while (countOpenings(s)):
                console.write("lel is called" + str(ii) + s + " \n")
                j_end = editor.getLineEndPosition(lineNumber+ii)
                editor.insertText(j_end," \\")
                ii = ii + 1
                s = editor.getLine(lineNumber + ii)    
    	    return ii+1            
        return 1
        fbeg = s.index("\"") + 1
        #console.write("lel is called" + str(ii) + " \n")
        end_cond = 1
        ii = 1
        while (end_cond):
            c = "%c" % editor.getCharAt(fbeg + ii)
            #console.write("else " + c + " \n")
            if (c == ";"):
                end_cond = 0
                brek_pos_end = j_beg  + ii + 2     
            elif (c == "{"):
                return 1             
            else: 
                pass
            ii = ii + 1 
    	ii = 1
    	s = editor.getLine(lineNumber + ii)    

    return 1

    
def forPrepReplace(contents, lineNumber, totalLines):
    forReplace(lineNumber,"//","#") 
    if (commentsLine(lineNumber)):
        return 1

    forReplace(lineNumber,"function","def")     
    forReplace(lineNumber,"+=1","++") 
    forReplace(lineNumber,"if (","if(") 
    forReplace(lineNumber,"if  (","if(") 
    forReplace(lineNumber,"$","")
    forReplace(lineNumber,"->",".")     
    forReplace(lineNumber,"->",".")     
    forReplace(lineNumber,"true","True") 
    forReplace(lineNumber,"FALSE","False") 
    forReplace(lineNumber,"false","False") 
    forReplace(lineNumber,"echo","print")   
   
    forReplace(lineNumber,"sizeof","len")
    forReplace(lineNumber,"array ()","[]")
    forReplace(lineNumber,"array()","[]")
    forReplace(lineNumber,"private $","self.")
    forReplace(lineNumber,"this.","self.")
    forReplace(lineNumber,"=\"","= \"")
    
    forReplace(lineNumber,"=\""," = \"")
    forReplace(lineNumber,"public def ","def ")
    
    
    lonlyIf(lineNumber)
    lonlyElse(lineNumber)
    
def forFORreplace(contents, lineNumber, totalLines):
    if (commentsLine(lineNumber)):
        return 1
    #forReplace(lineNumber,"true","True")

    forReplace(lineNumber,"\".","\"+")
    forReplace(lineNumber,"\" .","\"+")
    forReplace(lineNumber,".\"","+\"")
    forReplace(lineNumber,". \"","+\"")
    forReplace(lineNumber,"self ","self.")
    forReplace(lineNumber,"for (","for(")
    forReplace(lineNumber,"+=1","++")
    forReplace(lineNumber,"++ )","++)")


    if ("for(" in contents):
        j_end = editor.getLineEndPosition(lineNumber)
        j_beg = j_end - len(editor.getLine(lineNumber)) + 2
        console.write("str " + contents ) 
        s = editor.getLine(lineNumber)    
        fbeg = s.index("for(") + 4
        fend = 0
        if ("++)" in s): 
            fend = s.index("++)") + 3
        if ("--)" in s):
            fend = s.index("--)") + 3        
        if (fend < 3):
            return 1
        if (">=" in s):    
            return 1      
        elif ("=>" in s):
            return 1     
        elif ("<=" in s):
            return 1  
        elif ("=<" in s):
            return 1      
        else:
            pass
        cond = s[fbeg:fend].split(';')
        precond = cond[0].split("=")
        #precond2 = cond[0].split("=")
        if ("<" in cond[1]):
        	precond2 = cond[1].split("<")[1]
        elif (">" in cond[1]):
        	precond2 = cond[1].split(">")[1]
            
        if ("++" in cond[2]):
            insert_txt = "for " + precond[0].strip() + " in range ("+ (precond[1]).strip() + ", " + precond2.strip()+"-1): #was "
            console.write("insert " + str(j_beg + fbeg) + " "  + insert_txt + " \n")
            fbeg = fbeg - 4
            editor.insertText(j_beg + fbeg,insert_txt)  
        elif ("--" in cond[2]):
            insert_txt = "for " + precond[0].strip() + " in range ("+ precond2.strip() + ", " + precond[1].strip()+"+1): #was "
            console.write("insert " + str(j_beg + fbeg) + " "  + insert_txt + " \n")
            fbeg = fbeg - 4
            editor.insertText(j_beg + fbeg,insert_txt)  
        else:
            pass     

    forReplace(lineNumber,"++","+=1")    
    return 1
            
def insertabul(j_beg, ii_c):
    global tabul
    console.write("insertab is called" + str(ii_c) + " \n")
    for ii in range(j_beg+ii_c, j_beg+tabul*4):
        editor.insertText(ii," ")    
       
def maketabul(lineNumber1, tabN):
    console.write("maketab is called\n")
    j_end = editor.getLineEndPosition(lineNumber1)
    j_beg = j_end - len(editor.getLine(lineNumber1)) + 2
    for ii in range(0, tabN):
        c = "%c" % editor.getCharAt(j_beg + ii)
        if (c != " "):
            insertabul(j_beg, ii)
            return 1
            
        
def devideLine(lineNumber1, strRepl):
    #console.write("devideline is called\n")
    j_end = editor.getLineEndPosition(lineNumber1)
    # j_beg = editor.getLineEndPosition(lineNumber1)
    j_beg = j_end - len(editor.getLine(lineNumber1)) + 2
    #console.write("beg"+str(j_beg)+"\n")  
    #console.write("end"+str(j_end)+"\n")
    c = "%c" % editor.getCharAt(j_beg)
    #console.write("  c="+c)
    if (c == strRepl):
        #console.write("get jh \n")
        editor.insertText(j_beg+1,"\r\n")
        return 1
    for ii in range(j_beg, j_end):
        c = "%c" % editor.getCharAt(ii)
        #console.write(" get=" + c)
        if (c == "#"):
            return 1
        if (c == strRepl):
            #console.write("c now = " + str(ii) + " "+ c  +"\n")
            editor.insertText(ii,"\r\n")
            return 1
            
def commentsLine(lineNumber1):  
    #j_end = editor.getLineEndPosition(lineNumber1)
    s = editor.getLine(lineNumber1).strip() 
    if (len(s)>1):
        c = s[0]
    else:
        return 0
    if (c == '#' ):
        return 1
    else:
        return 0
        
def cleanLine(lineNumber1):  
    #console.write("cleanLine is called\n")
    j_end = editor.getLineEndPosition(lineNumber1)
    j_beg = j_end - len(editor.getLine(lineNumber1))+2         
    #console.write("beg"+str(j_beg)+"\n")  
    #console.write("end"+str(j_end)+"\n")
    #for ii in range(j_beg, j_end):  
    #    c = "%c" % editor.getCharAt(ii)
        #console.write("c =" + str(ord(c)) + "\n")
    for ii in range(j_beg, j_end):      
        c = "%c" % editor.getCharAt(ii)
        #c = editor.getCharAt(ii)
        #console.write("c =" + str(ord(c)) + "\n")
        if (c == ' ' ) or (c == '\t'):
            console.write("=")
            pass
        else:
            #if (c == '#' ):
            #    return 1
            editor.deleteRange(j_beg, ii - j_beg)
            #console.write("c = " + c +"\n")
            return 1
            

def findCurl(contents, lineNumber, totalLines):
    #console.write(contents)
    if (commentsLine(lineNumber)):
        return 1
    if ("{" in contents): 
        if contents.strip() == "{": 
            return 1#j+1;
        else:
            devideLine(lineNumber,"{")
            return 1
    if ("}" in contents): 
        if contents.strip() == "}":            
            return 1#j+1;
        else:
            devideLine(lineNumber,"}")
            return 1       
    else:
	    return 1    
        
def findCurlForComments(contents, lineNumber, totalLines):
    #console.write(contents)
    console.write("line = "+contents + "\n")
    if (commentsLine(lineNumber)):
        return 1
    if ("{" in contents): 
        if contents.strip() == "{": 
            onceReplace(lineNumber,"{","#{");
            return 1
    if ("}" in contents): 
        if contents.strip() == "}":    
            onceReplace(lineNumber,"}","#}");        
            return 1     
    else:
	    return 1            

def formatTab(contents, lineNumber, totalLines):
    global tabul

    console.write("line = "+contents + "\n")
    cleanLine(lineNumber);
    #if (commentsLine(lineNumber)):
    #    return 1
    if tabul > 0:
        if contents.strip() == "}": 
            tabul = tabul - 1
            maketabul(lineNumber,tabul*4)
            tabul = tabul + 1
        else:
            maketabul(lineNumber,tabul*4)	

    if ("{" in contents): 
        if contents.strip() == "{": 
            tabul = tabul + 1
            console.write("tabul ="+str(tabul) + "\n")
            return 1#j+1;
    if ("}" in contents): 
        if contents.strip() == "}":    
            tabul = tabul - 1 
            console.write("tabul = "+str(tabul) + "\n" )          
            return 1#j+1;

    # elif ("if (" in contents):
        # putDots(lineNumber)	
        # return 1
    # elif ("for(" in contents):
        # putDots(lineNumber)	
        # return 1
    # elif ("for (" in contents):
        # putDots(lineNumber)	
        # return 1
    # elif ("def " in contents):
        # putDots(lineNumber)	
        # return        

	return 1   

        
def putDots(lineNumber1):
	j = editor.getLineEndPosition(lineNumber1)
	editor.insertText(j,":")
    
def testCont(contents, lineNumber, totalLines):
    if ("if(" in contents): 
        putDots(lineNumber)	
        return 1#j+1;
    elif ("if (" in contents):
        putDots(lineNumber)	
        return 1
    elif ("for(" in contents):
        putDots(lineNumber)	
        return 1
    elif ("for (" in contents):
        putDots(lineNumber)	
        return 1
    elif ("def " in contents):
        putDots(lineNumber)	
        return   
    elif ("else " in contents):
        putDots(lineNumber)	
        return     
    elif ("else" in contents):
        putDots(lineNumber)	
        return         
    else:
	    return 1    
    #    if contents.strip() == "rubbish":
       #         editor.deleteLine(lineNumber)
                # As we've deleted the line, the "next" line to process
                # is actually the current line, so we return 0 to advance zero lines
                # and hence stay on the same line
     #           return 0

    #    elif contents.strip() == "something old":
    #            editor.replaceLine(lineNumber, "something new")

    #    elif contents.strip() == "little something":
    #            editor.replaceLine(lineNumber, "BIG\nSOMETHING")
                # Here we return 2, as we've inserted a newline,
                # and we don't want to test the "SOMETHING" line again
   #             return 2

        # if you wanted, you could optionally return 1 here, to move the next line
        # but that's the default, so you don't need to bother.


editor.beginUndoAction() 
editor.forEachLine(longComments)
editor.forEachLine(forPrepReplace)
editor.forEachLine(findCurl)
editor.forEachLine(formatTab)
editor.forEachLine(forFORreplace)
editor.forEachLine(testCont)
editor.forEachLine(forfinReplace)

editor.forEachLine(findCurlForComments)

editor.forEachLine(fortextReplace)
console.write("finished" ) 
editor.endUndoAction()