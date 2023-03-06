import whois

# Set the sites to run the script
sites = ["facebook.com", "instagram.com", "spotify.com"]

# Get specific data from the whois lookup
companies = [whois.whois(s).org for s in sites]
creation_dates = [whois.whois(s).creation_date for s in sites]
expiration_date = [whois.whois(s).expiration_date for s in sites]
name_servers = [whois.whois(s).name_servers for s in sites]
address = [whois.whois(s).address for s in sites]
city = [whois.whois(s).city for s in sites]
state = [whois.whois(s).state for s in sites]
registrant_postal_code = [whois.whois(s).registrant_postal_code for s in sites]
country = [whois.whois(s).country for s in sites]
emails = [whois.whois(s).emails for s in sites]


# Output Area
print("Registered Domains: ", companies)
print()
print("Creation date: ", creation_dates)
print()
print("Expiration date: ", expiration_date)
print()
print("Address: ", address)
print()
print("City: ", city)
print()
print("State: ", state)
print()
print("Postal Code: ", registrant_postal_code)
print()
print("Country: ", country)
print()
print("Registered Emails: ", emails)