function getXmlHttp(){
	var httpRequest;
    if (window.XMLHttpRequest) { // Mozilla, Safari, ...
        httpRequest = new XMLHttpRequest();
      } else if (window.ActiveXObject) { // IE
        try {
          httpRequest = new ActiveXObject("Msxml2.XMLHTTP");
        } 
        catch (e) {
          try {
            httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
          } 
          catch (e) {}
        }
      }
    return httpRequest;
}

function loadXMLDoc(xmlhttp, url, cfunc) {	
	xmlhttp.onreadystatechange = cfunc;
	url = encodeURIComponent(url) + new Date().getTime() + "/";
	xmlhttp.open("GET", url, true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send();
}

function correct_data(e, span_ctrl, input_ctrl, span_correct_ctrl, id){
    // look for window.event in case event isn't passed in
    if (typeof e == 'undefined' && window.event)
    { e = window.event; }
    if (e.keyCode == 13)
    {
    	send_correction(getXmlHttp(), span_ctrl, input_ctrl, span_correct_ctrl, false, id);
    }		
}

function send_correction(xmlhttp, span_ctrl, input_ctrl, span_correct_ctrl, is_correct_next_word, id)
{
	if (typeof input_ctrl=='undefined' || input_ctrl==null){
		   return;
	}
	input_text = span_correct_ctrl.innerHTML + input_ctrl.value.replace("?","");
	if (is_correct_next_word && input_text.length < 1)
		input_text = "*****";
	if (input_text.length < 1)
		return;
	var url_check = (is_correct_next_word? "../get_next_word/":
											"../check/");
	url_check += id + "/";
	loadXMLDoc(
			xmlhttp,
			url_check + input_ctrl.id + "/" 
			+ input_text + "/",
			function() {
				if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
					span_ctrl.innerHTML = xmlhttp.responseText;
				}
			}); 
}
	
function correct_everything(num_dialogs, id)
{
	for (var i=1; i<num_dialogs+1;i++)
	{
		send_correction(
				getXmlHttp(),
				document.getElementById("span_id" + i), 
				document.getElementById("line_id" + i),
				document.getElementById("span_correct_id" + i),
				false,
				id);
		
	}		
}

function FocusOnInput()
{
     document.getElementById("line_id1").focus();
}
