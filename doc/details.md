# Details on finding new endpoints

Details of the Web Control source code are given below and illustrated for the power ON/OFF example.

## Marantz Web control
If you go to the AVR web control landing page you `/index.html` you can select main zone and zone 2.
If you click on main zone, you are redirected to /MainZone/index.html.
Here, skeleton HTML is loaded first...

```html
			<div id="powerBtn">
				<div class="RParamL">
					POWER
				</div>
				<div class="RParamRBtn1">
				</div>
				<div class="RParamRBtn2">
				</div>
				<div class="clear">
				</div>
			</div>
```

Then, at the end of the skeleton HTML, the JavaScript is loaded. 
```html
</body>
<script type="text/javascript">
	function loadLib(lib){
		var s = document.createElement("script");
		s.src = lib;
		s.charset = "UTF-8";
		document.body.appendChild(s);
	}
	
	setTimeout(function(){
		loadLib('/lib/jquery/jquery.pack.js?201104070000');
		var id = setInterval(function(){
			if (window["jQuery"]) {
				clearInterval(id);
				loadLib('./index.js?201104070000');
			}
		}, 100);
	}, 500);
</script>
</html>
```
You can see that the JavaScript is loaded from `./index.js?201104070000`.

## Javascript
The javascript creates clickable buttons depending on the state of the AVR. 

```javascript
// Power
if (data.getValue("Power") == "ON") {
    $("div#powerBtn div.RParamRBtn1").empty().append(acreateButtonSelect(90, "ON"));
    $("div#powerBtn div.RParamRBtn2").empty().append(createButton(90, "#", "STANDBY").attr("title", "POWER > STANDBY").click(function() {
        putRequest({
            cmd0: "PutSystem_OnStandby/STANDBY",
            cmd1: "aspMainZone_WebUpdateStatus/"
        }, true, true);
        return false;
    }));

} else {
    $("div#powerBtn div.RParamRBtn1").empty().append(createButton(90, "#", "ON").attr("title", "POWER > ON").click(function() {
        putRequest({
            cmd0: "PutSystem_OnStandby/ON",
            cmd1: "aspMainZone_WebUpdateStatus/"
        }, true, true);
        return false;
    }));
    $("div#powerBtn div.RParamRBtn2").empty().append(acreateButtonSelect(90, "STANDBY"));
}
```

The buttons create `putRequest` calls. That method reveals the API endpoint is at `MainZone/index.put.asp` and the message payload is simple JSON.

```javascript
/**
 * ./index.put.asp ã«dataã‚’é€ä¿¡ã™ã‚‹ã€‚
 *
 * @since	2009/01/09
 * @param {Object} data
 * @param {Object} bReload
 * @param {Object} bFill
 */
function putRequest(data, bReload, bFill) {
	var url = "";
	if (_bDebug) {
		url = "/proxy.php?url=" + encodeURI("MainZone/index.put.asp");
		//url = "/postVar.php";
	} else {
		url = "./index.put.asp";
	}
	$.post(url, data, function(data) {
		if (_bDebug) {
			//alert(data);
		}
		if (bReload) {
			loadMainXml(bFill);
			setTimeout( function() {
				loadMainXml( false );
			}, 2000 );
		}
	});
}
```



