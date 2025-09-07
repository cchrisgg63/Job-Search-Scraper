#GOAL is to pull all the jobs that posted Yesterday and Today and output them in a neat manner with the Job Listing # and name.
#BeautifulSoup is a tool helps read HTML and allows it to be printed
from bs4 import BeautifulSoup

#Selenium is a tool that pulls the dynamic live website data and parses it into HTML.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://salesforce.wd12.myworkdayjobs.com/en-US/External_Career_Site?locations=1038e944b1101012453fb2ac8e470000&locations=1038e944b1101012453f7a44a4600000&locations=1038e944b1101012453a519010ae0000')

# Loads up the website for 10 seconds to find at least one job to appear to let the script run
#EC, By, and CLASS_NAME are Seleniums tools that help the website load before closing. VSCode script is too fast and will close the website before it reads anything.
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "css-1q2dra3"))
)


html_text = driver.page_source 

soup = BeautifulSoup(html_text, 'lxml')
#Salesforce has the HTML Element as 
# li class="css-1q2dra3"
jobs = soup.find_all('li',class_="css-1q2dra3")

#url variable is needed to allow redirect from VSCode to the webbrowser URL
base_url = 'https://salesforce.wd12.myworkdayjobs.com'

print("Jobs Posted Recently in Chicago are:")
print()

for job in jobs:


    job_name = job.a.text


    job_url = base_url+job.a['href']


    job_number_li = job.find('li', class_='css-h2nt8k')
    if job_number_li:
        job_number = job_number_li.text
    else:
        continue


 # The dd_elements makes it easier for the find to search through the dd text. If removed, there's too much text and it doesn't return anything.
    dd_elements = job.find_all('dd')
    if not dd_elements:
        continue


    job_date = dd_elements[-1].text
    if job_date in ["Posted Yesterday", "Posted Today"]:
        print("Job:", job_name)
        print("Listing Code:", job_number)

        choice = input('Do you want the job URL? (Yes or No): ')
        if choice == 'Yes':
            print()
            print("Job URL:", job_url)
        print()

driver.quit()


git remote add origin https://github.com/cchrisgg63/Job-Search-Scraper.git
git branch -M main
git push -u origin main
