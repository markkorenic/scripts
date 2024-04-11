import dns.resolver as dns

def check_host_by_name(domain):
    """
    Checks if domain can be looked up and display its host.
    Similar no nslookup
    """

    domain = "m.um.eu"
    # Fancy exception handling
    try:
        result = dns.resolve(domain, 'CNAME')

        # return domain and its target host with cnval.target
        for cnval in result:
            print(f"The domain {domain} is hosted on" , cnval.target)

    # if CNAME cannot be found
    except dns.NoAnswer:
        print('No record found for {domain}')
        pass
    #If domain is not found, print exception, or else this will error out.
    except dns.NXDOMAIN:
        print(f'{domain} does not exist or cannot resolve.')
        quit()

check_host_by_name('m.um.eu')
