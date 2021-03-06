# Import packages
from urllib.request import urlopen, Request

# Specify the url
#url = "http://www.datacamp.com/teach/documentation"
#url = 'http://docs.python.org/3/tutorial/index.html'
url = 'http://www.google.com'

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()
