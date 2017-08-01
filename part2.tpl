<!doctype html>
<head>
    <meta charset="utf-8" />
    <title>WebSocket Connection Testing</title>

    <style>
        li { list-style: none; }
    </style>

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>
    <script>
   setInterval(function myFunction() {
    document.getElementById("getData").click();
   var x=document.getElementById("getData");
   x.style.display='none';
},1);



   $(document).ready(function() {
            $("#getData").click();
            if (!window.WebSocket) {
                if (window.MozWebSocket) {
                    window.WebSocket = window.MozWebSocket;
                } else {
                    $('#messages').append("<li>Your browser doesn't support WebSockets.</li>");
                }
            }
            ws = new WebSocket('ws://192.168.0.11:8080/ws_welcome');
            ws.onopen = function(evt) {
                $('#messages').append('<li>Connected to server</li>');
            }
            ws.onmessage = function(evt) {
                console.log(str(evt.data))
            }
  
            $('#getData').click(function(){
                console.log('clicked');
                ws.send(window.location.pathname);
            });
            
        });
    </script>
</head>
<body>
    <h2>Hello world- Login!</h2>
   <button id="getData" onpageshow="myFunction()">Get Data</button>
</body>
</html>
