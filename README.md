<h1>CSV-anomaly-detector </h1>
A tool to detect anomalies in CSV files (especially large files)

<h2> Description </h2>

This tool is handy if you are working with a large csv file wherein scanning each
line for anomalies is a daunting task. Even if the file is received from a reliable
source it is always safe to verify the veracity of the file before proceeding further.

Each column has a title, all of which will be mentioned in the very first line of any 
csv file which we shall refer as "HEADER" throughout this page.

The tool takes a header-wise scanning approach.After scanning each Header, the dominant
datatype is identified and any another datatype is assumed ("we are not concluding 
because the final decision rests with the user") to be defective. 

<h2> Command line execution </h2>

Let us assume that our .csv file is mock.csv & our source code is AnomalyDetector.py

To view the headers of the file:	

<code> python AnomalyDetector.py columns --filename=mock.csv </code>

We will be shown the following result:
['id', 'first_name', 'last_name', 'email', 'country', 'ip_address']
where each element of the above array is a header

To find out the anomalies in each header (say email):

<code> python AnomalyDetector.py executeColumns --filename=mock.csv --columns=email</code>

To find out anomalies in all headers (i.e the whole file) :

<code> python AnomalyDetector.py execute --filename=mock.csv </code>

The above command executes the scanning process across all columns in one-go.

Upon completion of the scanning process, you will see either of these two responses:
<li>This Column appears bug free.</li>
<li>PLEASE OPEN improperData.txt**</li>

To know the commands available:

<code> python AnomalyDetector.py --help </code>

Please "avoid" spacing in the following areas:
<li>--filename = mock.csv (will throw error)</li>
<li>--filename= mock.csv (will throw error)</li>
<li>--filename =mock.csv(will throw error)</li>
<li>--filename=mock.csv (will give result)</li>

The above set of rules also apply for --columns
All entries are case sensitive

** improperData.txt contains all errors. It will be created automatically when .py
file is executed.

<h5> Please ensure that the source file (AnomalyDetector.py) and the .csv file are in the 
same directory. </h5>

<h4> Note: </h4>

If you are using compound words (more than a word ex. first name), please make sure 
it is enclosed inside quotes.

<code>python AnomalyDetector.py executeColumns --filename=mock.csv --columns=first name</code>
(WON'T WORK)

<code>python AnomalyDetector.py executeColumns --filename=mock.csv --columns="first name"</code>
(WORKS LIKE A CHARM)
