# Top 1000 IMDB Movies

## Instructions
To make sure you have the required packages, install the packages in `requirements.txt`.

To run the IMDB search, run `python3 imdb.py`. To choose a query, change the argument inside the file.

To scrape the data for the Top 1000 IMDB movies by rating, run `python3 data_prep.py`.  

## Assumptions
- While crawling the IMDB website, I assume the website has a fixed structure. This assumption is made because all the 
HTML encountered has this format.   
- I assume the text for the movie title, and directors and actors/actresses are of a fixed format. I make this 
assumption because all the text for the movies happened to occur in the same format. 

## Improvements 
- Error handling: There is currently no error handling. This is dangerous for multiple reasons. One, if there is 
connectivity issues during the web requests, this can lead to a crash and loss of work. Two, because the scraping 
implementation is not flexible to any HTML, if IMDB changes the format of their frontend app, this will lead to errors 
when scraping. 
- Testing: There is room for more robust testing, such as developing unit tests. Only spot checks have been performed 
so far.  
- Design Patterns: Currently, there seem to be some implementations that reflect poor design. For example, when the 
directors and actors/actresses are being parsed from a string, each part is being done individually in a hard-coded 
manner. There may be a way to do this more elegantly in case where there are more fields to parse from the string.   