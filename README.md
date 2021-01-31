# PyWaMG - WhatsApp Automator Bot
PyWaMG is a simple python library to automate sending messages and files on WhatsApp
##About Project
PyWaMG can be used to send documents, media or text messages through your personal WhatsApp number to groups and individual people, once or many times at defined intervals. You just have to login to WhatsApp web once on your personal computer, then you can upload the bot to remote servers so the messages keep getting sent without any user interaction.
## REQUIREMENTS:
[Python 3](https://www.python.org/downloads/)
## INSTALLATION:
```pip install PyWaMG```
## FUNCTIONS:
1. wa_login()
   ----------
    Use to login to Whatsapp Web
  
2. wa_close(isLogout=False)
   ------------------------
    Closes Whatsapp Web
    If parameter isLogout is set to True it logs out of Whatsapp Web

    isLogout : bool, optional
        Log out of Whatsapp Web (default is False)
      
3. send_txt(number,message,wait,times,appendMessageNumber = False,isInContacts = True,showLogs = True)
   ---------------------------------------------------------------------------------------------------
    Sends a text message to a WhatsApp number
    
    1. number : str
        - WhatsApp number where the message will be sent

    2. message : str
        - Message content that will be sent

    3. wait : int
        - Time in seconds to wait between sending messages

    4. times : int
        - Number of times to send the message

    5. appendMessageNumber : bool, optional
        - Add message count + 1 before message content (default is False)

    6. isInContacts : bool, optional
        - Set to false if sending message to a new number (default is True)

    7. showLogs : bool, optional
        - Show logs, ie record of messages sent (default is True)
