# Jarman Liu
import requests
import re
from multiprocessing.dummy import Pool as ThreadPool


def htscraping(pid):
    headers = {'User-Agent': 'user_agent', }
    s = requests.Session()
    url = 'https://www.hottopic.com/product/' + str(pid) + '.html'
    r = s.get(url, headers=headers, allow_redirects=True)
    filter = re.findall(r"funko.*hot-topic-exclusive", str(r.url))
    filter1 = re.findall(r"street-date", str(r.url))
    if filter or filter1:
        print(r.url)
        file.write(r.url + "\n")


def blscraping(pid):
    headers = {'User-Agent': 'user_agent', }
    s = requests.Session()
    url = 'https://www.boxlunch.com/product/' + str(pid) + '.html'
    r = s.get(url, headers=headers, allow_redirects=True)
    filter = re.findall(r"funko.*boxlunch-exclusive", str(r.url))
    filter1 = re.findall(r"street-date", str(r.url))
    if filter or filter1:
        print(r.url)
        file.write(r.url + "\n")


print("Stores:")
print("1. Hot Topic")
print("2. Box Lunch")
choice = int(input("Which store would you like to scrape? "))
if choice == 1 or choice == 2:
    #pid = input(
    #    "What PID do you want to start with? (Best to start with 10000000) ")
    #ranges = input("What is the range of your desired PID scraping? ")
    #pid = int(pid)
    #ranges = int(ranges)
    pid = 11539160
    ranges = 1400000
    file = open("pids.txt", "w")
    a = []
    for i in range(ranges):
        a.append(pid)
        pid += 1
else:
    print("Invalid choice")

pool = ThreadPool(8)
if choice == 1:
    results = pool.map(htscraping, a)
    pool.close()
    pool.join()
    file.close()
elif choice == 2:
    results = pool.map(blscraping, a)
    pool.close()
    pool.join()
    file.close()
else:
    print("Please input a valid choice")
