# EL2020

### tempWeb Branch

This is the branch of this repository that has the code that you will need for the mid-term.  It's pretty simple.  My sqlite database is in the log/ folder.  In the python/ folder you will find two scripts: flaskServer.py and tempReader.py and a folder: templates/

The folder contains the index.html for the Google chart of our temperature data.  The tempReader.py reads the temperature and humidity and logs them to a database along with the time that the reading was taken.  The flaskServer.py uses the Flask framework to establish a web server, serve the index.html, and establish an 'sqlData' app route to be called by the javascript in index.html to read the data from the database.
