import requests #nemshy l safha l feha les donnees(Yallakora page :matchCenter)
from bs4 import BeautifulSoup #parsing lel html code ykhalini nkharej les donnees
import csv 
from itertools import  zip_longest

result= requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
src= result.content
soup= BeautifulSoup(src, "lxml")

job_title=[]
company_name=[]
location_name=[]
job_skill=[]
Links=[]

#find the elements containing info:
#job titles, job skills, company names , location names
job_titles= soup.find_all("h2",{"class":"css-m604qf"})
company_names= soup.find_all("a", {"class":"css-17s97q8"})
location_names= soup.find_all("span", {"class":"css-5wys0k"})
job_skills= soup.find_all("div", {"class":"css-y4udm8"})




#returned lists to extract needed info into other lists
for i in range (len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    job_skill.append(job_skills[i].text)
    Links.append(job_titles[i].find("a").attrs['href'])

for link in Links:
    if link.startswith('/'):
        link = 'https://wuzzuf.net' + link
    result= requests.get(link)
    src= result.content
    soup= BeautifulSoup(src,"lxml")



#create csv file and fill it with values
file_list= [job_title,company_name,location_name,job_skill,Links]
exported= zip_longest(*file_list)
with open('C:\\Users\\marie\\Desktop\\Projects\\wuzzuf(jobs)\\jobs.csv', 'w') as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["job title","company name", "location","skills","Links"])
    wr.writerows(exported)




