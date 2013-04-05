#import time
#for $id, $article in $articles.items():
  #* Parse date *#
  #set $date = $time.strftime("%A, %d %B %Y", $article.date)
  <b>Date:</b> $date</br> 
  <h1>$article.title</h1> (by $article.author)
  <hr />
#end for