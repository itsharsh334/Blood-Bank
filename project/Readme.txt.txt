DBS_PR_01 Blood Bank Management System
- In this project, we have made a Blood Bank Management System
  where we match people wishing to give blood (donors) and people
  needing the blood (receivers) using their blood types and location.

Contributors:
1) Harsh Priyadarshi - 2020A7PS0110P
2) Shashank Shreedhar Bhatt - 2020A7PS0078P

Requirements to run the program:
- MySQL (preferably version 8.0.28) and Python3 have been used.
- The program requires that the 2 “.ico” images and the “.jpg” image labelled ‘bb.jpg’, ‘bb.ico’ and ‘images.ico’ be
  placed in the same folder as the python file named ‘hello.py’.

Things to do before running the program:
- The user must run the .sql file to initialise the database. The .sql file will make the tables and populate them too.
- The user must enter their MySQL account password in the required places (indicated clearly by a comment) so that the
  software will be able to connect to the database.
  		For reference, the lines where these changes are to be made are: 68, 91, 150, 211, 237, 348, 452, 467,
										 523, 545, 569, 594, 676, 764 (14 hits)
		For ease of operation, you can search "localhost" in the python file and fill in the password at each hit.

Required Python3 Libraries (installation of these libraries and packages will require 'pip'):
- mysql.connector (>_ pip install mysql.connector)  ## to install the package ##
- tkinter 	  (>_ pip install tk)      ## to install the library ##
- PIL 		  (>_ pip install Pillow)  ## to install the library ##
- email.mime 	  (>_ pip install email)   ## to install the library ##
- turtle 	  (>_ pip install turtle)  ## to install the library ##