#import time
<ul>
#for $id, $article in $articles.items():
  #* Parse date *#
  #set $date = $time.strftime("%A, %d %B %Y", $article.date)
  <li><b>$date</b>: $article.text ($article.author)</li>
#end for