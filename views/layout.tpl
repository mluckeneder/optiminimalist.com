<style type="text/css">
  body {
    font-family: "Helvetica Neue";
    font-weight: 300;
    width:80%;
    margin:0 auto;
    text-align: justify;
  }
</style>
<ul>
    #for $id, $article in $articles.items():
        <li><a href="/$id">$article.title</a></li>
    #end for
        <li><a href="/">All posts</a></li>
</ul>
$layout_yield

