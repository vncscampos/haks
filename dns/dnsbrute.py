import dns.resolver
import sys

try:
    url = sys.argv[1]
    name_file = sys.argv[2]
    wordlist = open(name_file, 'r').readlines()
except:
    print('Usage: python3 dnsbrute.py domain wordlist.txt')
    sys.exit()

resolver = dns.resolver.Resolver()

for subdomain in wordlist:
    try:
        target = "{}.{}".format(subdomain.rstrip('\n'), url)
        results = resolver.resolve(target, 'A')
        if(results):
            for res in results:
                print("subdomain: {} --> {}" .format(target, res))
    except Exception as err:
        pass
