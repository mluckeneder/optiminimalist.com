$(function(){
    $(document).keydown(function(e){
        var sel = $("a[rel=prev-article]");
        if (e.keyCode == 37 && sel.length !== 0) { 

            prevlink = sel.attr("href");
            location.href = prevlink;
            return false;        
        }

        sel = $("a[rel=next-article]");
         if (e.keyCode == 39 && sel.length !== 0) { 

            nextlink = $("a[rel=next-article]").attr("href");
            location.href = nextlink;
            return false;
        }
    });
});