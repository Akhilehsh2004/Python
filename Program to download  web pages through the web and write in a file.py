import requests

url = 'https://github.com/'

# Make the request
r = requests.get(url, allow_redirects=True)

# Specify the filename
filename = "content.txt"

# Write content to the file
with open(filename, 'wb') as file:
    file.write(r.content)

print(f"Content saved to {filename}")
