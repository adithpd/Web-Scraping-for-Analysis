import wikipedia as wk

print(wk.search("Washington"))

print(wk.search("IIT Madras", results=2))

print(wk.summary("IIT Madras"))

print(wk.summary("IIT Madras", sentences=2))

full_page = wk.page("IIT Madras")

print(full_page.content)

print(full_page.url)

print(full_page.references)

print(full_page.title)

print(full_page.images)

print(full_page.images[0])

#extract html code of wikipedia page based on any search text
html = wk.page("IIT Madras").html().encode("UTF-8") 

import pandas as pd
df = pd.read_html(html)[6]  

df

