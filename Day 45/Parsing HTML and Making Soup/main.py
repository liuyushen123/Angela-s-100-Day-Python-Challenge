from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser") # This line will compelete our parsing
# Now soup is a object that allows us to tap into various parts of the website
# Using python code


# For Exampless
print(soup.title) # This will print out the title tag
print(soup.title.string) # Gives the string which is contain inside the title tag

print(soup.prettify()) 

print(soup.a)
