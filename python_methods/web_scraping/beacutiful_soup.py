Web scraping:
  If HTML is file more complex but want to find any element easily we can use BeautifulSoup.
  
  Ex:
    from bs4 import BeautifulSoup
#import lxml : another of files like html, xml ..

with open("website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title)
Result(Rs):
  <title>Angela's Personal Site</title>
  -----------
print(soup.title.name)
Rs:
  title
  ----------
  
  print(soup.title.string)
  Rs:
    
Angela's Personal Site
----------------
  
print(soup)

Rs:
  <!DOCTYPE html>

<html>
<head>
<meta charset="utf-8"/>
<title>Angela's Personal Site</title>
</head>
<body>
<h1 id="name">Angela Yu</h1>
<p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
<p>I am an iOS and Web Developer. I ❤️ coffee and motorcycles.</p>
<hr/>
<h3 class="heading">Books and Teaching</h3>
<ul>
<li>The Complete iOS App Development Bootcamp</li>
<li>The Complete Web Development Bootcamp</li>
<li>100 Days of Code - The Complete Python Bootcamp</li>
</ul>
<hr/>
<h3 class="heading">Other Pages</h3>
<a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>
<a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>
</body>
</html>
---------------

print(soup.prettify()) #with indentaion

Rs:
<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8"/>
  <title>
   Angela's Personal Site
  </title>
 </head>
 <body>
  <h1 id="name">
   Angela Yu
  </h1>
  <p>
   <em>
    Founder of
    <strong>
     <a href="https://www.appbrewery.co/">
      The App Brewery
     </a>
    </strong>
    .
   </em>
  </p>
  <p>
   I am an iOS and Web Developer. I ❤️ coffee and motorcycles.
  </p>
  <hr/>
  <h3 class="heading">
   Books and Teaching
  </h3>
  <ul>
   <li>
    The Complete iOS App Development Bootcamp
   </li>
   <li>
    The Complete Web Development Bootcamp
   </li>
   <li>
    100 Days of Code - The Complete Python Bootcamp
   </li>
  </ul>
  <hr/>
  <h3 class="heading">
   Other Pages
  </h3>
  <a href="https://angelabauer.github.io/cv/hobbies.html">
   My Hobbies
  </a>
  <a href="https://angelabauer.github.io/cv/contact-me.html">
   Contact Me
  </a>
 </body>
</html>

============================
if want to hold all the elements
===========================

###Helps to print all defined elements:
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

#####Print all the anchor text
# for tag in all_anchor_tags:
#     # print(tag.getText)

    #####Prints only anchor links
    # print(tag.get("href"))


#####prints only the required element by using id/class
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)

#######If want get from nested tags/elements
# company_url = soup.select_one(selector="p a")
# print(company_url)

#####id######
# name = soup.select_one(selector="#name")
# print(name)

heading = soup.select(".heading")
print(heading)
