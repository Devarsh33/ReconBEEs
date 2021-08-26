import requests
import subprocess
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
from colors import *

if __name__ == '__main__':

    while True:
        searched_links = []
        broken_links = []


        def getLinksFromHTML(html):
            def getLink(el):
                return el["href"]

            return list(map(getLink, BeautifulSoup(html, features="html.parser").select("a[href]")))


        def find_broken_links(domainToSearch, URL, parentURL):
            if (not (URL in searched_links)) and (not URL.startswith("mailto:")) and (not ("javascript:" in URL)) and (
                    not URL.endswith(".png")) and (not URL.endswith(".jpg")) and (not URL.endswith(".jpeg")):
                try:
                    requestObj = requests.get(URL)
                    searched_links.append(URL)
                    if requestObj.status_code == 404:
                        broken_links.append("%sBROKEN: link %s" % (yellow, end) + URL + "%s from %s" % (yellow, end) + parentURL)
                        print(broken_links[-1])
                    else:
                        print("%sNOT BROKEN: link %s" % (red, end) + URL + "%s from %s" % (red, end) + parentURL)
                        if urlparse(URL).netloc == domainToSearch:
                            for link in getLinksFromHTML(requestObj.text):
                                find_broken_links(domainToSearch, urljoin(URL, link), URL)
                except Exception as e:
                    print("%s%s ERROR: %s" %(bad, red, end) + str(e))
                    searched_links.append(domainToSearch)

        print()
        fbl = input("%sEnter URL%s(%s Type with http:// or https:// %s)%s : %s" % (green, end, red, end, green, end))
        find_broken_links(urlparse(fbl).netloc, fbl, "")

        print("\n--- DONE! ---\n")
        print("The following links were broken:")

        for link in broken_links:
            print("\t" + link)

        print()
        again = input('''%sWould you like to another scan ? yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bees.py', shell=True)
            print(bh)
            break