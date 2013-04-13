#import time

<section id="articlelist">
    #for $id, $article in $articles.items():
        #* Parse date *#
        #set $date = $time.strftime("%B %Y", $article.date)
        <article id="post_1">
                    <header class="blog_header">
                      <h3><a href="/$id">$article.title</a></h3>
                      <span class="date">$date</span>
                    </header>
        </article>
    #end for
</section>