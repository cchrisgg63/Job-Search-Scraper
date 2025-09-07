from bs4 import BeautifulSoup

with open('/Users/admin/reactapp/ECGTech/Webscraper/home.html', 'r') as html_file:
    content = html_file.read()

    
    #BeautifulSoup parses HTML or XML so python can easily extract data from it. 'lxml' is the parser BeautifulSoup will use to read the HTML
    #Parsers are the engine that understand HTML structure
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card' )
    for item in course_cards:
        item_name = item.h5.text
        item_price = item.a.text.split()[-1]


        print(f'{item_name} costs {item_price}')

#When inspecting the website. I looked at the pricing, then saw that the a tag had the pricing. So I'm using above to scrape the pricing of the html.
#This is what I saw: <a href="#" class="btn btn-primary">Start for 20$</a>
#all the div has a class of 'card'
#class_ is the language to pull from a html attributes
#class is python

#output was 
#Python for beginners
#Start for 20$
#Python Web Development
#Start for 50$
#Python Machine 

#I'm going to clean it up by adding .split()[-1] since it's the last text value in the a tag.

#output is 
#Python for beginners
#20$
#Python Web Development
#50$
#Python Machine Learning
#100$

#to further clean it and print as only one sentence instead of those choppy lines.
#  I went FROM print(item_name) print(item_price)
# TO  print(f'{item_name} costs {item_price}')
# f imbeds multiple variables into a string.
