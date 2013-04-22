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
    <link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400' rel='stylesheet' type='text/css'>
    <script src="http://code.jquery.com/jquery.js"></script>
    <!-- Bootstrap -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <script src="/static/js/bootstrap.min.js"></script>
    <script src="/static/js/application.js"></script>
    <link href="/atom.xml" type="application/atom+xml" rel="alternate" title="ATOM feed">
    <link href="/static/css/main.css" rel="stylesheet" media="screen">

  </head>
  <body>

    <div class="container">

        

        <header class="pageheader">

          <div class="pull-left">
            <a href="/"><i class="icon-home icon-black"></i> optiminimalist.com</a> 
            
          </div>

<!--           <div class="pull-right">
            <a href="http://www.optiminimalist.com">rss</a>
          </div>
 -->
      </header>


          $layout_yield

          

        
       

      <hr>

      <div class="footer">
        <p>&copy; 2013 <a href="mailto:optiminimalist(at)gmail(dot)com">optiminimalist</a></p>
      </div>

    </div> <!-- /container -->

    <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-40155093-1', 'optiminimalist.com');
  ga('send', 'pageview');

</script>
  </body>
</html>



