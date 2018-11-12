import requests
import re
from multiprocessing.dummy import Pool as ThreadPool

pid = input("What PID do you want to start with? (Best to start with 10000000) ")
ranges = input("What is the range of your desired PID scraping? ")
pid = int(pid)
ranges = int(ranges)
file = open("pids.txt", "w")


def scraping(pid):
    headers = {'User-Agent': 'user_agent', }
    s = requests.Session()
    url = 'https://www.hottopic.com/product/' + str(pid) + '.html'
    r = s.get(url, headers=headers, allow_redirects=True)
    filter = re.findall('figure-hot-topic-exclusive', str(r.url))
    if filter:
        # print(r.url)
        file.write(r.url + "\n")
    #pid += 1
    return (pid)


a = []
for i in range(ranges):
    a.append(pid)
    pid += 1
# print(a)

pool = ThreadPool(25)
results = pool.map(scraping, a)
pool.close()
pool.join()
file.close()
