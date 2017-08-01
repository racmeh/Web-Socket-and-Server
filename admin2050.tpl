<!doctype html>
<head>
    <meta charset="utf-8" />
    <title>WebSocket Connection Admin</title>

    <style>
        li { list-style: none; }
    </style>

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>
    <script>
    
       setInterval(function myFunction() {
    document.getElementById("getCount").click();
   var x=document.getElementById("getCount");
   x.style.display='none';
},1);

setInterval(function myFunction1() {
    document.getElementById("getIp").click();
   var y=document.getElementById("getIp");
   y.style.display='none';
},1);

        $(document).ready(function() {
            $("#getCount").click();
            $("#getIp").click();
            
            if (!window.WebSocket) {
                if (window.MozWebSocket) {
                    window.WebSocket = window.MozWebSocket;
                } else {
                    $('#messages').append("<li>Your browser doesn't support WebSockets.</li>");
                }
            }
            ws = new WebSocket('ws://192.168.0.11:8080/ws_admin');
            ws.onopen = function(evt) {
                $('#messages').append('<li>Connected to server</li>');
                
                
            }
           ws.onmessage = function(evt) {
                

                var abc=evt.data;
                var res = abc.substring(10,11);
                var num=abc.lastIndexOf("}");
                var res1 = abc.substring(23,num-1);
                console.log('Count : ' + res);
                $('#count').text(res);
                console.log('IP : ' + res1);
                $('#ip').text(res1);
                }

            $('#getCount').click(function(){
                console.log('click');
                ws.send('Hello');
            });

$('#getIp').click(function(){
                console.log('click1');
                ws.send('Hello1');
            });
            
        });
    </script>
</head>
<body>
    <h2>WebSocket Connection Admin</h2>
       <br>
    <h3>Online Devices : <span id="count"></span></h3>
<button id="getCount" onpageshow="myFunction()">Get Count</button>
<br><br><br>
<h3>User IP : <span id="ip"></span></h3>
<button id="getIp" onpageshow="myFunction1()">Get IP</button>
</body>
</html>
