$(document).ready(function(){
  var myArr = "";
  var xmlhttp = new XMLHttpRequest();

  var $name1st = $("#name1st");
  var $minAvg1st = $("#minAvg1st");

  var $name2nd = $("#name2nd");
  var $minAvg2nd = $("#minAvg2nd");

  var $name3rd = $("#name3rd");
  var $minAvg3rd = $("#minAvg3rd");


  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        myArr = JSON.parse(this.responseText);
        $name1st.text(myArr[0].name);
        $minAvg1st.text(myArr[0].minutesAvg);

        $name2nd.text(myArr[1].name);
        $minAvg2nd.text(myArr[1].minutesAvg);
      
        $name3rd.text(myArr[2].name);
        $minAvg3rd.text(myArr[2].minutesAvg);
    }
  };

  xmlhttp.open("GET", "https://api.jsonbin.io/b/5ec8ee2fe91d1e45d10fc9bc/1", true);
  xmlhttp.send();
});