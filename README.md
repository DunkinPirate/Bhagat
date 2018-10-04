# Bhagat

Bhagat is a work-in-progress RAT (remote administration tool) written in Python. The framework for the code allows for new commands and modules to be easily added. Bhagat uses standard TCP socket connections included with the default Python libraries and can run in the background silently once converted to .exe. 

Current Commands:

'help' - Displays text, ensuring that the connection is stable.

'ss' - Takes a screenshot of the client's screen, saves it as a .PNG image, and sends it to the server.

'listdir' - Provides the server with a list of items in the client's target directory. 

'delete' - Allows the server to delete a target file on the client's system. 

This project is for educational use only. Please do not use Bhagat for nefarious, malicious, or illegal purposes. 
