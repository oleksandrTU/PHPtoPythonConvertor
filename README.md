# PHPtoPythonConvertor<br>
PHP to Python convertor tool.<br>
This was a side project for TU Ilmenau, Integrated Communication Systems Group. <br>
https://www.tu-ilmenau.de/en/integrated-communication-systems-group/<br>

This is script for Notepad++ with plugin Python Script (http://npppythonscript.sourceforge.net/).<br><br>
It will convert PHP code to Python code. It will not convert 100%, but it will do 80% of job. For file with 2000 lines you need around 3 hours for full conversion. <br>
<br>
How to use:<br>
1. Install Notepad++ and plugin Python Script (http://npppythonscript.sourceforge.net/)<br>
2. Create new file in Notepad++, copy code from php2python.py to this new file. Select menu Plugins->Python Script->New Script and save it with some name (let's say php2python). You will use this name to run a script. <br>
3. Open your PHP code in Notepad++. Save it with some name. Select Plugins->Python Script->Show Console, then select Plugins->Python Script->Scripts->php2python. Conversion started immidiatly. It will take around 2-3 minutes on i5 computer to finish 2000 lines.<br>
4. If you like to expand script or change it. Press <b>Ctrl</b> and then select Plugins->Python Script->Scripts->php2python. Script will be opened for editing in new window. It is python code, so you can use all Python power for text processing.<br>
5. For SQL querries you can use file <b>db_class.py</b>. In PHP file you need an adaptor like below. So SQL part of code will be the same as before.<br><b>
def mysql_query (self, querry):<br>
 &nbsp;&nbsp;&nbsp;&nbsp;    res = self.db.LoadData(querry);<br>
 &nbsp;&nbsp;&nbsp;&nbsp;    return res<br></b>
6. For saving data to file, if you are doing it like this:<br>
<b>fwrite (fopen("output.txt","a"),"\nError: Cannot find data for the node 18.  All RSSI are zero!\n\n");</b><br>
you need 2 function from file <b>log_file_write.py</b><br>


