#import time
#set $date = $time.strftime("%d %B %Y", $article.date)
<article class="blogpost ">
            <header class="blog_header">
              <h1 class="list-title">$article.title</h1>
              <span class="date">$date</span>
              <!-- <span class="tags">
                [
                #for $t in $article.tags
                  <a href="/tags/$t">\#$t</a>
                #end for
                ]
              </span> -->
            </header>


            <div class="tldr">
              <span class="header">
                TL;DR
              </span>
                $article.tldr
            </div>




            <!-- <br clear="all"/> -->

            <section class="content ">
                $article.content
            </section>

            <section class="social text-center">
            <a href="https://twitter.com/share" class="twitter-share-button">Tweet</a>
            <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>

            <!-- Place this tag where you want the +1 button to render. -->
            <div class="g-plusone" data-size="medium"></div>

            <!-- Place this tag after the last +1 button tag. -->
            <script type="text/javascript">
              (function() {
                var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
                po.src = 'https://apis.google.com/js/plusone.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
              })();
            </script>
          </section>


           <section class="article_nav">
         <div id="prev_article" class="pull-left">
          #if $prev_article is not None
             <a href="/$prev_article.id" rel="prev-article">&larr; $prev_article.article.title</a>
          #end if
         </div>

          <div id="next_article" class="pull-right">
          #if $next_article is not None
             <a href="/$next_article.id" rel="next-article">$next_article.article.title &rarr;</a>
          #end if
          </div>
      </section>
      <br/>
            <hr/>
            <div id="disqus_thread"></div>
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
            <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
    
          </article>

          

        