import dns.resolver

# url = input('Digite o domínio: ')

resolver = dns.resolver.Resolver()

try:
    results = resolver.resolve('bancocn.com', 'A')
    for res in results:
        print(res)
    
except Exception as err:
    print('Error:', err)
