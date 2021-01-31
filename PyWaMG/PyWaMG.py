from msedge.selenium_tools import Edge,EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
import base64,os
from time import sleep,ctime
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def wait_for_load(term):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,term)))

options = EdgeOptions()
options.use_chromium = True      #Uses chromium-based edgium, remove to use legacy edge
options.add_argument("user-data-dir="+os.getcwd()+"\\Cache")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.49")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
options.headless = True          #Headless mode
driver = Edge(EdgeChromiumDriverManager().install(),options=options)

def wa_login():
    '''
    Use to login to Whatsapp Web
    
    Can omit usage if already logged in once by scanning QR

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    try:
        driver.get('https://web.whatsapp.com/')
        if os.path.isfile('./Cache/wa.exists'):
            return
        else:
            pass
        wait_for_load('_1PTz1')
        driver.execute_script("""
        var element1 = document.querySelector("._3DgtU");
        var element2 = document.querySelector("._1iKcN");
        if (element1)
            element1.parentNode.removeChild(element1);
        if (element2)
            element2.parentNode.removeChild(element2);
        """)
        Image.open(BytesIO(driver.find_element_by_class_name('landing-main').screenshot_as_png)).show()
        with open('Cache/wa.exists','w') as file:
            pass
    except:
        print('Error in PyWaMG')
        driver.quit()

def wa_close(isLogout=False):
    '''
    Closes Whatsapp Web

    If parameter isLogout is set to True it logs out of Whatsapp Web

    Parameters
    ----------
    isLogout : bool, optional
        Log out of Whatsapp Web (default is False)

    Returns
    -------
    None
    '''
    try:
        if isLogout:
            driver.find_element_by_css_selector("span[data-icon='menu']").click()
            driver.find_element_by_css_selector("span[title='Log out']").click()
            os.remove('Cache/wa.exists')
        driver.quit()
    except:
        print('Error in PyWaMG')
        driver.quit()

def send_txt(number,message,wait,times,appendMessageNumber = False,isInContacts = True,showLogs = True):
    '''
    Sends a text message to a WhatsApp number

    Arguments
    ---------
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

    Returns
    -------
    None
    '''
    try:
        if driver.current_url != 'https://web.whatsapp.com/' or not isInContacts:
            driver.get('https://web.whatsapp.com/send/?phone='+number)
            wait_for_load('_1awRl')
        else:
            wait_for_load('_1awRl')
            driver.find_element_by_class_name('_1awRl').send_keys(number,Keys.RETURN)
        if times == 1: wait = 0
        for i in range(times):
            driver.find_elements_by_class_name('_1awRl')[1].send_keys(((str(i+1)+': ') if appendMessageNumber else '')+message,Keys.RETURN)
            if showLogs: print('\033[1;32mSent message to '+number+' at '+ctime()+'!\033[0m')
            sleep(wait)
        WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"span[aria-label=' Pending ']")))
    except:
        print('Error in PyWaMG')
        driver.quit()

def send_txt_to_group(group_id,message,wait,times,appendMessageNumber=False,showLogs=True):
    '''
    Sends a text message to a WhatsApp group

    Arguments
    ---------
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

    Returns
    -------
    None
    '''
    try:
        driver.get('https://web.whatsapp.com/accept?code='+group_id)
        wait_for_load('_1awRl')
        if times == 1: wait = 0
        for i in range(times):
            sleep(1)
            driver.find_elements_by_class_name('_1awRl')[1].send_keys(((str(i+1)+': ') if appendMessageNumber else '')+message,Keys.RETURN)
            if showLogs: print('\033[1;32mSent message to Group'+group_id+' at '+ctime()+'!\033[0m')
            sleep(wait)
        WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"span[aria-label=' Pending ']")))
    except:
        print('Error in PyWaMG')
        driver.quit()

def send_file(number,fpath,isInContacts=True,showLogs=True):
    '''
    Sends a file/document to a WhatsApp number

    Arguments
    ---------
    1. number : str
        - WhatsApp number where the file will be sent

    2. fpath : str
        - Absolute path to the file being sent

    3. isInContacts : bool, optional
        - Set to false if sending message to a new number (default is True)

    4. showLogs : bool, optional
        - Show logs, ie record of messages sent (default is True)

    Returns
    -------
    None
    '''
    try:
        if driver.current_url != 'https://web.whatsapp.com/' or not isInContacts:
            driver.get('https://web.whatsapp.com/send/?phone='+number)
            wait_for_load('_1awRl')
        else:
            wait_for_load('_1awRl')
            driver.find_element_by_class_name('_1awRl').send_keys(number,Keys.RETURN)
        driver.find_element_by_css_selector("span[data-icon='clip']").click()
        driver.find_element_by_css_selector("input[type='file']").send_keys(fpath)
        wait_for_load('_3Git-')
        driver.find_element_by_css_selector("span[data-icon='send']").click()
        wait_for_load('aLK5N')
        WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"span[aria-label=' Pending ']")))
        if showLogs: print('\033[1;32mSent file to '+number+' at '+ctime()+'!\033[0m')
    except:
        print('Error in PyWaMG')
        driver.quit()

def send_media_file(number,fpath,caption,isInContacts=True,showLogs=True):
    '''
    Sends a visual media file (image/video) with an optional caption message to a WhatsApp number

    Arguments
    ---------
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

    Returns
    -------
    None
    '''
    try:
        if driver.current_url != 'https://web.whatsapp.com/' or not isInContacts:
            driver.get('https://web.whatsapp.com/send/?phone='+number)
            wait_for_load('_1awRl')
        else:
            wait_for_load('_1awRl')
            driver.find_element_by_class_name('_1awRl').send_keys(number,Keys.RETURN)
        driver.find_element_by_css_selector("span[data-icon='clip']").click()
        driver.find_element_by_css_selector("input[type='file']").send_keys(fpath)
        wait_for_load('_3Git-')
        driver.find_element_by_class_name('_1awRl').send_keys(caption,Keys.RETURN)
        wait_for_load('aLK5N')
        WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"span[aria-label=' Pending ']")))
        if showLogs: print('\033[1;32mSent media file to '+number+' at '+ctime()+'!\033[0m')
    except:
        print('Error in PyWaMG')
        driver.quit()

def send_file_to_group(group_id,fpath,showLogs=True):
    '''
    Sends a file/document to a WhatsApp number

    Arguments
    ---------
    1. group_id : str
        - WhatsApp Group ID (as seen in Group Invite Link)

    2. fpath : str
        - Absolute path to the file being sent

    3. showLogs : bool, optional
        - Show logs, ie record of messages sent (default is True)

    Returns
    -------
    None
    '''
    try:
        driver.get('https://web.whatsapp.com/accept?code='+group_id)
        wait_for_load('_1awRl')
        driver.find_element_by_css_selector("span[data-icon='clip']").click()
        driver.find_element_by_css_selector("input[type='file']").send_keys(fpath)
        wait_for_load('_3Git-')
        driver.find_element_by_css_selector("span[data-icon='send']").click()
        wait_for_load('aLK5N')
        WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"span[aria-label=' Pending ']")))
        if showLogs: print('\033[1;32mSent file to Group'+group_id+' at '+ctime()+'!\033[0m')
    except:
        print('Error in PyWaMG')
        driver.quit()

def send_media_file_to_group(group_id,fpath,caption,showLogs=True):
    '''
    Sends a file/document to a WhatsApp number

    Arguments
    ---------
    1. group_id : str
        - WhatsApp Group ID (as seen in Group Invite Link)

    2. fpath : str
        - Absolute path to the file being sent

    3. caption : str
        - Message content that will be sent with the media file
    
    4. showLogs : bool, optional
        - Show logs, ie record of messages sent (default is True)

    Returns
    -------
    None
    '''
    try:
        driver.get('https://web.whatsapp.com/accept?code='+group_id)
        wait_for_load('_1awRl')
        driver.find_element_by_css_selector("span[data-icon='clip']").click()
        driver.find_element_by_css_selector("input[type='file']").send_keys(fpath)
        wait_for_load('_3Git-')
        driver.find_element_by_class_name('_1awRl').send_keys(caption,Keys.RETURN)
        wait_for_load('aLK5N')
        WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"span[aria-label=' Pending ']")))
        if showLogs: print('\033[1;32mSent media file to Group'+group_id+' at '+ctime()+'!\033[0m')
    except:
        print('Error in PyWaMG')
        driver.quit()

# except Exception as e:
#     print('PyWaMg error:',e)
#     os.remove('Cache/wa.exists')
#     driver.quit()