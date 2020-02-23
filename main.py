import requests
from bs4 import BeautifulSoup

URL = 'https://portal.nsts.ca/Cancellations.aspx'
page = requests.get(URL)

delay_soup = BeautifulSoup(page.content, 'html.parser')
div_notice = delay_soup.find(id='ctl00_CPHPageBody_Panel_GeneralNotice')

job_elems = div_notice.find_all('span', class_='Normal')
general_notice_elem = delay_soup.find(id='ctl00_CPHPageBody_GeneralNoticesMsg')

str_gen_note = general_notice_elem.text.strip()

if(str_gen_note == "There are no general notices at this time"):
    print("You have to go to damn school.")
else:
    print("You don't have to go to damn school.")