$(document).ready(function(){
    var $listItems = $("#airlines");
    var xmlhttp = new XMLHttpRequest();
    var myArr = "";

    $('#airlinesList').on('click', 'a', function( e ){
      var $self = $(this);
      var href = $self.attr('href');
      var i = $self.attr('value');
      e.preventDefault();
      
      href += "?code="+myArr[i].code+"&name="+myArr[i].name+"&flights="+myArr[i].flights;
      href += "&airNum="+myArr[i].airNum+"&delAvg="+myArr[i].delAvg+"&minAvg="+myArr[i].minAvg;
      href += "&topPort="+myArr[i].topPort;
      console.log(href);

      window.location = href;
  });

    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        myArr = JSON.parse(this.responseText);
        listDatas = "";
        for( var i = 0; i < myArr.length; i++ ){
            listDatas += "<a value=\""+i+"\" href=\"airline.html\"><li>" + myArr[i].name + "</li></a>";
        };
        $listItems.html(listDatas);
      }
    };

    xmlhttp.open("GET", "https://api.jsonbin.io/b/5ec7d44718c8475bf16e4782", true);
    xmlhttp.send();
});
