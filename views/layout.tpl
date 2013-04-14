<!DOCTYPE html>
<html>
  <head>
    <title>

      #if $pagetitle is not None
        $pagetitle by 
      #end if
      optiminimalist.com

    </title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="http://code.jquery.com/jquery.js"></script>
    <!-- Bootstrap -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <script src="/static/js/bootstrap.min.js"></script>
    <link href="/static/css/main.css" rel="stylesheet" media="screen">

  </head>
  <body>

    <div class="container">

        

        <header class="pageheader">

          <div class="pull-left">
            <a href="/">optiminimalist.com</a>
          </div>

          <div class="pull-right">
            <a href="http://www.optiminimalist.com">rss</a>
          </div>

      </header>


          $layout_yield

          

        
       

      <hr>

      <div class="footer">
        <p>&copy; 2013 optiminimalist.com</p>
      </div>

    </div> <!-- /container -->
  </body>
</html>



