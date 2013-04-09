#import time
#* Parse date *#
#set $date = $time.strftime("%B %Y", $article.date)
<article id="post_1">
            <header class="blog_header">
              <h2>$article.title</h2>
              <span class="date">$date</span>
            </header>

            $article.text
          </article>