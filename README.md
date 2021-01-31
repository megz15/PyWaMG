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
        
4. send_txt_to_group(group_id,message,wait,times,appendMessageNumber=False,showLogs=True)
   --------------------------------------------------------------------------------------
   Sends a text message to a WhatsApp group

    1. group_id : str
        - WhatsApp Group ID (as seen in Group Invite Link)

    2. message : str
        - Message content that will be sent

    3. wait : int
        - Time in seconds to wait between sending messages

    4. times : int
        - Number of times to send the message

    5. appendMessageNumber : bool, optional
        - Add message count + 1 before message content (default is False)

    6. showLogs : bool, optional
        - Show logs, ie record of messages sent (default is True)

5. send_file(number,fpath,isInContacts=True,showLogs=True)
   -------------------------------------------------------
   Sends a file/document to a WhatsApp number

    1. number : str
        - WhatsApp number where the file will be sent

    2. fpath : str
        - Absolute path to the file being sent

    3. isInContacts : bool, optional
        - Set to false if sending message to a new number (default is True)

    4. showLogs : bool, optional
        - Show logs, ie record of messages sent (default is True)
        
6. send_file_to_group(group_id,fpath,showLogs=True)
   ------------------------------------------------
   Sends a file/document to a WhatsApp number

    1. group_id : str
        - WhatsApp Group ID (as seen in Group Invite Link)

    2. fpath : str
        - Absolute path to the file being sent

    3. showLogs : bool, optional
        - Show logs, ie record of messages sent (default is True)

7. send_media_file(number,fpath,caption,isInContacts=True,showLogs=True)
   ---------------------------------------------------------------------
   Sends a visual media file (image/video) with an optional caption message to a WhatsApp number

    1. number : str
        - WhatsApp number where the file will be sent

    2. fpath : str
        - Absolute path to the file being sent

    3. caption : str
        - Message content that will be sent with the media file

    4. isInContacts : bool, optional
        - Set to false if sending message to a new number (default is True)

    5. showLogs : bool, optional
        - Show logs, ie record of messages sent (default is True)
      
8. send_media_file_to_group(group_id,fpath,caption,showLogs=True)
   --------------------------------------------------------------
   Sends a file/document to a WhatsApp number

    1. group_id : str
        - WhatsApp Group ID (as seen in Group Invite Link)

    2. fpath : str
        - Absolute path to the file being sent

    3. caption : str
        - Message content that will be sent with the media file
    
    4. showLogs : bool, optional
        - Show logs, ie record of messages sent (default is True)
        
## NOTE:
Phone number has to be in the format 'Country code'+'phone number', eg for country code +91 and mobile number 9876543210, the number parameter should be '919876543210'
Group ID can be found out from the group invite link. For that:
1. Open the Group chat in WhatsApp
2. Click on the Group name at the top
3. Click on 'Invite to group via link' (Ask your group admin to send the invite link if you can't see it)
4. Get the Group ID (https://chat.whatsapp.com/this_is_the_group_id)

\
\
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)<br>
Made with :heart: by Meghraj Goswami<br>
For Terms of Service visit https://bit.ly/3aeIVfl
