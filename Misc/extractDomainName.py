## https://www.codewars.com/kata/514a024011ea4fb54200004b/solutions/python

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
#
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"
import re

def domain_name(url):
    if url.startswith('http'):
        r = re.compile('(?<=://)(.*?)(?=/|$)')
    else:
        r = re.compile('^(.*?)(?=/|$)')

    search = re.search(r, url)
    domain_list = search.group(0).split('.')

    return domain_list[0] if len(domain_list) == 2 else domain_list[1]


## Alt solution
def domain_name(url):
    return url.split("//")[-1].split('www.')[-1].split(".")[0]

### TESTING
#res = domain_name("http://github.com/carbonfive/raygun") == "github"
#res = domain_name("http://www.zombie-bites.com") == "zombie-bites"
#res = domain_name("https://www.cnet.com") == "cnet"
#res = domain_name("www.xakep.ru")

print(res)