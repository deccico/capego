var constants = {
    "Solve video": 1,
    "Visit video": 2,
    "Share video": 3,
    "Visit the site": 4,
    "Send correction": 5,
    "Contribute video": 6,
    "Sign up": 7
};

var csrftoken = $.cookie('csrftoken');

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
    // look for window.event in case event isn't passed in
    if (typeof e == 'undefined' && window.event)
    { e = window.event; }
    if (e.keyCode == 13)
    {
    	send_correction(getXmlHttp(), span_ctrl, input_ctrl, span_correct_ctrl, false, id, btn_suggest);
    }		
}

function send_correction(xmlhttp, span_ctrl, input_ctrl, span_correct_ctrl, is_correct_next_word, id, btn_suggest)
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
					//todo next line is also coupled with Formatter class..
					if (span_ctrl.innerHTML.indexOf('<div class="status-correct">') !== -1){
						btn_suggest.style.display = 'none';
					}
				}
			}); 
}
	
//todo: move this class to the formatter class? since it has information about the control names..
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

function focusOnInput()
{
     document.getElementById("line_id1").focus();
}

$(function () {
    $('.disconnect form a').on('click', function (e) {
        e.preventDefault();
        $(this).parent('form').submit();
    });
});

$(document).ready(function() {
    $('#subscribe-form').submit(function() {
        $(this).ajaxSubmit({success: showResponse});
        // always return false to prevent standard browser submit and page navigation
        return false;
    });
});

// post-submit callback
function showResponse(responseText, statusText, xhr, $form){
    $('#newsletter_msg').html(responseText);
}

function doSomethingAfterSomeSeconds(seconds, f){
    var ms = seconds * 1000;
    setTimeout(f, ms);
}

String.prototype.hashCode = function(){
    var hash = 0, i, char;
    if (this.length == 0) return hash;
    for (i = 0; i < this.length; i++) {
        char = this.charCodeAt(i);
        hash = ((hash<<5)-hash)+char;
        hash = hash & hash; // Convert to 32bit integer
    }
    return hash;
};

function getActivityKey(activity_code, description){
    user
}

function sendActivity(activity_code, description){
    $.ajax({
        type: "POST",
        url: "/user/register_activity",
        beforeSend: function(xhr) {
            xhr.overrideMimeType("text/plain; charset=x-user-defined");
        },
        data: { activity_code: activity_code }
    }).done(function(msg) {
            if (msg.substring(0,2)=="OK"){
                localStorage.setItem('favoriteflavor','vanilla');
            }

        });
}

function initPlay(){
    focusOnInput();
    doSomethingAfterSomeSeconds(5, function(){sendActivity(constants["Visit video"])});
}
