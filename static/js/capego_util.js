//common
var constants = {
    "Solve video": 1,
    "Visit video": 2,
    "Share video": 3,
    "Visit the site": 4,
    "Send correction": 5,
    "Contribute video": 6,
    "Sign up": 7,
    'event_key': 'event_key'
};

function getToday(){
    var currentdate = new Date();
    var today = currentdate.getDate() + "/"
        + (currentdate.getMonth()+1)  + "/"
        + currentdate.getFullYear();
    return today;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

//play specific
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

function correct_data(e, span_ctrl, input_ctrl, span_correct_ctrl, id, btn_suggest){
    if (typeof e == 'undefined' && window.event)
    { e = window.event; }
    if (e.keyCode != 13)
        return;
    send_correction(getXmlHttp(), span_ctrl, input_ctrl, span_correct_ctrl, false, id, btn_suggest);
}

function send_correction(xmlhttp, span_ctrl, input_ctrl, span_correct_ctrl, is_correct_next_word, id, btn_suggest)
{
    //alert(xmlhttp, span_ctrl, input_ctrl, span_correct_ctrl, is_correct_next_word, id, btn_suggest)
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
    input_ctrl_id = input_ctrl.id;
	loadXMLDoc(
			xmlhttp,
			url_check + input_ctrl.id + "/" 
			+ input_text + "/",
			function() {
				if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
					span_ctrl.innerHTML = xmlhttp.responseText;
					if (span_ctrl.innerHTML.indexOf('<div class="status-correct">') !== -1){
						btn_suggest.style.display = 'none';
					}
                    var input = document.getElementById(input_ctrl_id);
                    if (input){
                        var txt = input.value;
                        input.focus();
                        input.value = txt;
                    }
                    else{
                        for (var i=0;i<10;i++){
                            e = document.getElementById("line_id".concat(i));
                            if (e!=null){
                                var txt = e.value;
                                e.focus();
                                e.value = txt;
                                break;
                            }
                        }
                    }
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
				id,
				document.getElementById("btn_suggest" + i));
	}		
}

// newsletter specific
$(document).ready(function() {
    $('#subscribe-form').submit(function() {
        $(this).ajaxSubmit({success: showResponse});  //newsletter specific
        // always return false to prevent standard browser submit and page navigation
        return false;
    });
});

function showResponse(responseText, statusText, xhr, $form){
    $('#newsletter_msg').html(responseText);
    document.getElementById('email').value="";
}

//common
function doSomethingAfterSomeSeconds(seconds, f){
    var ms = seconds * 1000;
    setTimeout(f, ms);
}

function sendActivity(activity_code, desc){
    $.ajax({
        type: "POST",
        url: "/user/register_activity/",
        beforeSend: function(xhr) {
            return doINeedToSend(desc);
        },
        data: { activity_code: activity_code, description: desc, csrfmiddlewaretoken: csrftoken }
    }).done(function(msg) {
            analyseResponseActivityMessage(msg, desc);
        });
}

function analyseResponseActivityMessage(msg, desc){
    if (msg.length < 1)
        return;
    obj = JSON && JSON.parse(msg) || $.parseJSON(msg);
    if (obj != null) obj = obj[0];
    //this is to avoid sending the same events
    if (obj.status){
        localStorage.setItem(desc, "true");
    }
}

//play specific
function focusOnInput()
{
    document.getElementById("line_id1").focus();
}

function initPlay(video_id){
    focusOnInput();
    sendUserActivities(video_id);
}

function getElementByXPath(path) {
  result = document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
  return result.singleNodeValue;
}


function setElementIdByXpath(xpath, id_name){
    if (document.getElementById(id_name) == null){
        e = getElementByXPath(xpath);
        if (e != null){
            e.id = id_name;
        }
    }
}

function remove(id)
{
    return (elem=document.getElementById(id)).parentNode.removeChild(elem);
}

function removeIfFunctionDoesNotExist(f, id_name){
    if (eval("typeof " + f) == "undefined") {
        remove(id_name)
    }
}
