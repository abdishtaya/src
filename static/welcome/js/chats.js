

function submitChat() {
	
     //  alert($("#texterea").html().trim().length );
	  // return ;
	if( form1.msg.value == '' 
	&& $("#texterea").html().trim().length=="0" 
	&& form1.fileupload.value=='') {
		alert("ALL FIELDS ARE MANDATORY!!!");
		return;
	}
	 var file = "";
	//alert(file.type);
	if(form1.fileupload.value!="")
	{
		file=document.getElementById('fileupload').files[0];
		//alert(file.type);
	
	if(file.size>4000000){
		alert("size of file grater than 4 M");
			form1.fileupload.value="";
	document.getElementById('namefile').innerHTML="  ";
	 document.getElementById('imagePreview').style.display='none';
		return;
	}
		
	if(file.type!='image/gif' && file.type!='image/jpeg' && file.type!='image/png' && file.type!='video/mp4' && file.type!='video/x-ms-wmv' && file.type!='video/x-msvideo' && file.type!='video/MP4'
		
	&& file.type!='application/x-zip-compressed'
	&& file.type!='audio/midi'
	&& file.type!='audio/mpeg'
	&& file.type!='audio/ogg'
	&& file.type!='audio/x-m4a'
	&& file.type!='audio/x-realaudio'
	)
	{
			alert("Sorry, only wmv, mp4 ,avi//zip // gif,jpg,png,jpeg//	mid midi kar,mp3,ogg,m4a,ra files are allowed.");
				form1.fileupload.value="";
	document.getElementById('namefile').innerHTML="  ";
	 document.getElementById('imagePreview').style.display='none';
		return;
	}
	}
	//var usersids =form1.usersid.value;
	//var msg =form1.msg.value;
	//alert(usersid);
	var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange = function() {
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
			
			document.getElementById('chatlogs').innerHTML = xmlhttp.responseText;
		}
	}
	
	//xmlhttp.open('GET','insert?usersid='+usersids+'&msg='+msg,true);
	//xmlhttp.send();
	$("#sendmessages").one('keydown',function(event){
	 if (event.keyCode == 13) {
		 content = document.getElementById("texterea").innerHTML;
	
     document.form1.msg.value += content;
		// alert('sdddd');
	  $.ajax({
            type: 'POST',
            url: 'insert',
			data: new FormData(this), 
contentType: false,      
cache: false,             
processData:false
        })
         .done(function(data){
		$("#chatlogs").append(data);
		$('#xx').scrollTop($('#xx')[0].scrollHeight);
		  $('#getusers').load('getusers');
           //  console.log(data);
         // alert(data);
        })
        .fail(function(data) {
         // console.log(data); 
		// alert("nooooo");
	   });}
	form1.msg.value="";
	form1.fileupload.value="";
	document.getElementById('namefile').innerHTML=" ";
	document.getElementById("texterea").innerHTML=" ";
    document.getElementById('imagePreview').style.display='none';
	// document.getElementById('imagePreview')="";
	//$('#chatlogs').load('logs?id='+usersids);
});
/////////////////////////////////////////////////////////////on click using button in form to send message
	
	$("#sendmessages").one('click',function(){
		 content = document.getElementById("texterea").innerHTML;
	
     document.form1.msg.value += content;
		// alert('sdddd');
	  $.ajax({
            type: 'POST',
            url: 'insert',
			data: new FormData(this), 
contentType: false,      
cache: false,             
processData:false
        })
         .done(function(data){
		$("#chatlogs").append(data);
		$('#xx').scrollTop($('#xx')[0].scrollHeight);
		  $('#getusers').load('getusers');
           //  console.log(data);
         // alert(data);
        })
        .fail(function(data) {
         // console.log(data); 
		// alert("nooooo");
	   });
	form1.msg.value="";
	form1.fileupload.value="";
	document.getElementById('namefile').innerHTML=" ";
	document.getElementById("texterea").innerHTML=" ";
    document.getElementById('imagePreview').style.display='none';
	// document.getElementById('imagePreview')="";
	//$('#chatlogs').load('logs?id='+usersids);
});
}

function start(){
$(document).ready(function(e){
	$.ajaxSetup({
		cache: false
	});
	 
	setInterval( function(){
		
		//$('#getss').load('logs');
         $.ajax({
            type: 'GET',
            url: 'logs'
           // data: $(this).serialize()
        })
		.done(function(data){
		$("#chatlogs").append(data);
		if(data){
			
			 $('#xx').scrollTop($('#xx')[0].scrollHeight);
		}
           //  console.log(data);
          // alert(data);
        });

		}, 2000 );
 
		
		});
}
 setTimeout(
    function() {
$('#getsmiles').load('getsmiles'); 
    }, 3000);

$(document).ready(function(e){
	$.ajaxSetup({
		cache: false
	});
	
	 $('#getusers').load('getusers'); 
});
$(document).ready(function(e){
	$.ajaxSetup({
		cache: false
	});
	
	setInterval( function(){ $('#getmessageusers').load('getmessageusers'); }, 4000 );
});
function chatu(name,id){
	// form1.usersid.value=id;
	//$("#chatlogs").append("loading chat....");
	 document.getElementById("chatlogs").innerHTML ="LOADING CHATLOG...";
	  document.getElementById("demos").innerHTML = name;
	   $.ajax({
            type: 'GET',
            url: 'sessionreceiver?id='+id
           // data: $(this).serialize()
        })
	 $('#chatlogs').load('logs');
		//$('#chatlogs').load('logs?id='+id);
       start();
	   $('#getusers').load('getusers'); 
	
	
	
}
function addsmile(smile){
	// var obj=document.getElementById('text');
 //obj.value+=" <img src='"+smile+"'> ";
	  $("#texterea").append("<img src='"+smile+"'/>");

//	$("#texterea").append(" "+smile+" ");
	//alert(smile);
	
}


function myFunction() {
	//addfile();
	document.getElementById('addfile').style.display='none';
	
    var x = document.getElementById('toglesmiles');
    if (x.style.display === 'none') {
        x.style.display = 'block';
		
	//	form1.fileupload.value="";
	document.getElementById('namefile').innerHTML="  ";
    document.getElementById('imagePreview').style.display='none';
    } else {
        x.style.display = 'none';
			
	 
    }
}
function addfile(){
	//myFunction();
	document.getElementById('toglesmiles').style.display='none';
	var x = document.getElementById('addfile');
    if (x.style.display === 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
		form1.fileupload.value="";
	document.getElementById('namefile').innerHTML="  ";
    document.getElementById('imagePreview').style.display='none';
    }
	
}
$(document).ready(function(e){

$('#fileupload').change(function(){	
	
			readImgUrlAndPreview(this);
	 var file = document.getElementById('fileupload').files[0];
	
	
document.getElementById('namefile').innerHTML="Item added :"+ file.name+" ";
     if(file.type!='image/gif' && file.type!='image/jpeg' && file.type!='image/png'){
		 document.getElementById('imagePreview').style.display='none';	
	 }else {
		 document.getElementById('imagePreview').style.display='block';
	 }
			function readImgUrlAndPreview(input){
				 if (input.files && input.files[0]) {
			            var reader = new FileReader();
						

			            reader.onload = function (e) {			            	
			                $('#imagePreview').attr('src', e.target.result);
							
							}
			          };
					  
			          reader.readAsDataURL(input.files[0]);
					 
			     }	
		});});
		
	 
		function search(){
		 
			var search=document.getElementById('searchfreind').value;
			 $.ajax({
            type: 'GET',
            url: 'searchfreind?search='+search
           // data: $(this).serialize()
        })
		.done(function(data){
		//$("#chatlogs").append(data);
		//$('#xx').scrollTop($('#xx')[0].scrollHeight);
		 document.getElementById('getusers').innerHTML=data;
		 document.getElementById('searchfreind').value="";
		  setTimeout(
    function() {
    $('#getusers').load('getusers'); 
    }, 15000);
           //  console.log(data);
         // alert(data);
        })
	// $('#chatlogs').load('logs');
			
		}
		//to focus on text area always
		function getfocus(){
			
			 focusint=setInterval(function(){  document.getElementById("texterea").focus(); }, 200);

		}
      function losefocus(){
		  clearInterval(focusint);
          document.getElementById("texterea").blur();
		  
	  }


	 

   



