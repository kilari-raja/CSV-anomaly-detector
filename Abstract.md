<h1>Brief Workflow </h1>
<b> Data Acceptor : </b>
	The tool scans the given csv file. First step of check is to look for improper commas. Any issues with commas and the tool ceases there. If perfectly comma seperated, the scanning continues.<br>
<b> DataType Classifier : </b>
	Once the scanning is complete, each entry in each line is segregated into different datatypes depending on the given entry.<br>
<b> Data Calculator </b>
	Once the classification is over, each column has a dominant datatype and few minority datatypes (Assuming our csv file has few defects). Now the minority datatypes are concluded to be defective.
<b> Improper Data Displayer </b>
	Once the defective entries are known, they are printed back for the sake of users.

<h1> Detailed Workflow</h1>
<ul>
<li>The file which is used directly from the command line is starter.py</li>
<li>This file contains various @app.command</li>
<li>Each @app.command is a seperate functionality provided in the tool.</li>
<li>Of all these, two are considered quintessential. (execute and executeColumns)</li>
<li>Both these commands are linked to a common function called startTool, which can be found in trigger.py</li>
<li>This function is the key to whole tool. The steps explained in the brief workflow (see above) can be seen in the said function "startTool"</li>
</ul>

<h3>Data Acceptor:</h3>
As soon as the file is received, the function commaChecker (in <b>starter.py</b>) splits each row at commas and looks for rows with improper commas. If any such row is found, the tool stops execution. The improper row is documented in a seperate file (improperData.txt)
<h3>DataType Classifier :</h3>
Once the comma check is over, each element in each row is now taken and analyzed (using regex) and given a datatype (in <b>Classifier.py</b>)
Datatypes cover not just string, integer. The tool dives a bit deeper and subclassifies string further into string with spaces,string with integers, string with integer and spaces and so on.
To get an idea of the different types of datatypes that are handled, please use <b>ToolTestCases.py</b>
<h3>Data Calculator :</h3>
We take a column wise approach throughout the tool. Once each element in each row is assigned a datatype, we scan the whole column to see which datatype is dominating (<b>Calculator.py</b>). Whichever elements form the minority datatype can be assumed (with some confidence) to be defective.
The same goes for one column after the other (if you choose "execute" in the command line).
If you choose "executeColumns" in the command line, then the process ceases at the end of the mentioned column.
<h3>Improper Data Displayer </h3>
Once the defective rows are known, they are documented in a seperate file (improperData.txt) which can be later used by user.

<h4>Extra Details</h4>
<p>
The file <b>commonFunc.py</b> is used to reuse a set of lines while printing defective entries.
This file is assisted by a dict defined in <b>config.py</b>
All global variables are declared in <b>reader.py</b>
</p>

<b> The tool only detects the defects. It doesn't automatically replace the wrong with the right. (Evolution takes time) </b>