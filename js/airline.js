$(document).ready(function(){
    $airlineNameMenu = $('#airlineNameMenu');
    $airlineName = $("#airlineName h2");
    $flights = $("#flights");
    $airNum = $("#airNum");
    $delAvg = $("#delAvg");
    $minAvg = $("#minAvg");
    $topPort = $("#topPort");
    $logo = $("#imageHolder img");

    function getUrlVars() {
        var vars = {};
        var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
            vars[key] = value;
        });
        return vars;
    };
    
    function getUrlParam(parameter, defaultvalue){
        var urlparameter = defaultvalue;
        if(window.location.href.indexOf(parameter) > -1){
            urlparameter = getUrlVars()[parameter];
            }
        return urlparameter;
    };
    
    
    var code = getUrlParam('code','Empty');
    var name = getUrlParam('name','Empty').replace(/%20/gi,' ');
    var flights = getUrlParam('flights','Empty');
    var airNum = getUrlParam('airNum','Empty');
    var delAvg = getUrlParam('delAvg','Empty');
    var minAvg = getUrlParam('minAvg','Empty');
    var topPort = getUrlParam('topPort','Empty');


    $airlineNameMenu.text(name);
    $airlineName.text(name);
    $flights.text(flights);
    $airNum.text(airNum);
    $delAvg.text(delAvg+"%");
    $minAvg.text(minAvg);
    $topPort.text(topPort);
    $logo.attr("src","logo/"+code+".png");



});

