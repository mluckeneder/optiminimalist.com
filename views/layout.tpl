<!DOCTYPE html>
<html>
  <head>
    <title>Bootstrap 101 Template</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="http://code.jquery.com/jquery.js"></script>
    <!-- Bootstrap -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <script src="/static/js/bootstrap.min.js"></script>
    <style type="text/css">
        body {
        padding-top: 50px;
        padding-bottom: 60px;
        font-weight: 300;
      }

      article > h2{
        /*margin-bottom: 20px;*/
      }

      p {
        line-height: 1.6em;
        font-size: 18px;
      }

      .blog_header {
        margin-bottom: 20px;
      }

      .blog_header > .date {
        color: #c7c2b8;
      }

      #about_me {
        margin-top:200px;
      }
      /* Custom container */
      .container {
        margin: 0 auto;
        max-width: 1000px;
      }
      .container > hr {
        margin: 60px 0;
      }

    
      article > header > h2:hover, article h3 a:hover {
        color: #DF7401;
        text-decoration: none;
      }

      .blog_header h3 a {
        color:#000;
      }

      .blog_header h3 {
        margin-bottom: 0px;
      }
    


    </style>
  </head>
  <body>

    <div class="container">

      <!-- Example row of columns -->
      <div class="row">
        
        <div class="span8">

          $layout_yield

          
        </div>

        
       
      </div>


      <hr>

      <div class="footer">
        <p>&copy; 2013 optiminimalist.com</p>
      </div>

    </div> <!-- /container -->

    <!-- <ul>
        #for $id, $article in $articles.items():
            <li><a href="/$id">$article.title</a></li>
        #end for
            <li><a href="/">All posts</a></li>
    </ul> -->
  </body>
</html>



