If you are uncomfortable with git and familiar with pip install our pip package and starting 
playing right away.

On your terminal 

<code>sudo pip install CSV-anomaly-detector==1.2.7</code>

(Right now 1.2.7 is the stable version. When upgraded, changes will be reflected here).

Go to any directory that contains that has a .csv file (say sample.csv) 

To find the headers of the .csv file:

<code>AnamolyDetector columns --filename=sample.csv</code>

To find out the anamolies in each header (say email) :

<code>AnamolyDetector executeColumns --filename=sample.csv --columns=email</code>

To find out anomalies in all headers (i.e the whole file) :

<code>AnomalyDetector execute --filename=sample.csv</code>

Relative refernce to filenames will also work:

<code>AnomalyDetector execute --filename="./Verticals/sample.csv"</code>