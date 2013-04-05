#import time
#* Parse date *#
#set $date = $time.strftime("%A, %d %B %Y", $article.date)
<b>Date:</b> $date</br> 
<h1>$article.title</h1>
$article.text (by $article.author)