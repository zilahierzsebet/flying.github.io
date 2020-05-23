$(document).ready(function(){
    var myArr = "";
    var xmlhttp = new XMLHttpRequest();

    var $name1st = $("#name1st");
    var $flights1st = $("#flights1st");
    var $code1st = $("#code1st");
    var $coor1st = $("#coor1st");

    var $name2nd = $("#name2nd");
    var $flights2nd = $("#flights2nd");
    var $code2nd = $("#code2nd");
    var $coor2nd = $("#coor2nd");

    var $name3rd = $("#name3rd");
    var $flights3rd = $("#flights3rd");
    var $code3rd = $("#code3rd");
    var $coor3rd = $("#coor3rd");

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myArr = JSON.parse(this.responseText);
            $name1st.text(myArr[0].name);
            $flights1st.text(myArr[0].flights);
            $code1st.text(myArr[0].code);
            $coor1st.text(myArr[0].lat+" "+myArr[0].long);
            
            $name2nd.text(myArr[1].name);
            $flights2nd.text(myArr[1].flights);
            $code2nd.text(myArr[1].code);
            $coor2nd.text(myArr[1].lat+" "+myArr[1].long);

            $name3rd.text(myArr[2].name);
            $flights3rd.text(myArr[2].flights);
            $code3rd.text(myArr[2].code);
            $coor3rd.text(myArr[2].lat+" "+myArr[2].long);
        }
    };

    xmlhttp.open("GET", "https://api.jsonbin.io/b/5ec8323ebbaf1f2589452835/1", true);
    xmlhttp.send();
});