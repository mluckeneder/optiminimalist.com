<style type="text/css">
  body {
    font-family: "Helvetica Neue";
    font-weight: 300;
  }
</style>

#import time
#for $id, $article in $articles.items():
  #* Parse date *#
  #set $date = $time.strftime("%A, %d %B %Y", $article.date)
  <b>Date:</b> $date</br> 

  #* Metadata *#
  #for key,value in $filter(lambda x: "text" not in x and "date" not in x, $article.items()):
    <b>$key:</b> $value</br> 
  #end for


  $article.text (by $article.author)
  <hr />
#end for