<h1>Web Scraping Homework - Mission to Mars</h1>
<h3>Gary Jeter</h3>
</br>
<h3> Step 1: Scraping</h3>
<ul>Jupyter Notebook: mission_to_mars.ipynb is Python code that scraps 4 webpages for the following info</ul>
    <li>NASA Mars News</li>
    <li>JPL Mars Images</li>
    <li>Mars Facts</li>
    <li>Mars Hemispheres - Names & Image URLs</li>

<h3> Step 2: Display data scraped</h3>
<ul>Step A: scrape_mars.py:  created functions using Jupyter Notebook Pythong code.  Functions are: </ul>
    <li>scrape_news()</li>
    <li>scrape_space_image()</li>
    <li>scrape_fact_table()</li>
    <li>scrape_mars_hemi()</li>
    <li>master_scrape():  This pulled the top four into one master dictionary</li>

<p></p>
<p>Step B: app.py:  calls functions and writes data to the MongoDB database (mars_db) and provides data to index.html.  Used the master_scrape() function</p>
<p> Andrew Perez and Michael Badinger helped me with the syntax to make app.py work
<p></p>
<p>Step C: index.html:  diplays the Mars data and images and has a button to execute the scrape.  Was unable to format or get the hemisphere images to appear.  I think I did not scrape the full image url which caused the problem.  </p>
<p></p>
<p>I ran out of time to complete the full assignment.</p>
    

