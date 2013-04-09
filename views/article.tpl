#import time
#set $date = $time.strftime("%B %Y", $article.date)
<article id="post_1">
            <header class="blog_header">
              <h3>$article.title</h3>
              <span class="date">$date</span>
            </header>

            <section class="content">
                $article.text
            </section>

           <!--  <div id="disqus_thread"></div>
            <script type="text/javascript">
                /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
                var disqus_shortname = 'optiminimalist'; // required: replace example with your forum shortname

                /* * * DON'T EDIT BELOW THIS LINE * * */
                (function() {
                    var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                    dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
                    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
                })();
            </script>
            <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
            <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a> -->
    
          </article>

         <section id="article_nav">
         <div id="prev_article" class="pull-left">
          #if $prev_article is not None
             <a href="/$prev_article.id" >&larr; $prev_article.title</a>
          #end if
         </div>

          <div id="next_article" class="pull-right">
          #if $next_article is not None
             <a href="/$next_article.id" >$next_article.title &rarr;</a>
          #end if
          </div>
      </section>