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

