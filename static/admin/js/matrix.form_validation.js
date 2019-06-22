
$(document).ready(function(){
	
	$('input[type=checkbox],input[type=radio],input[type=file]').uniform();
	
	$('select').select2();
	
	// Form Validation
    $("#addServices").validate({
		rules:{

			nameofservice:{
				required:true,
				minlength:8,
				maxlength:40

			},
			emailcustomer:{
				required:true,
				email: true
			}

		},
		errorClass: "help-inline",
		errorElement: "span",
		highlight:function(element, errorClass, validClass) {
			$(element).parents('.control-group').addClass('error');
		},
		unhighlight: function(element, errorClass, validClass) {
			$(element).parents('.control-group').removeClass('error');
			$(element).parents('.control-group').addClass('success');
		}
	});
	

		// Form Validation
    $("#addservice2").validate({
		rules:{
			nameofservice1:{
				required:true
			},
			emailcustomer1:{
				required:true,
				email: true
			}

		},
		errorClass: "help-inline",
		errorElement: "span",
		highlight:function(element, errorClass, validClass) {
			$(element).parents('.control-group').addClass('error');
		},
		unhighlight: function(element, errorClass, validClass) {
			$(element).parents('.control-group').removeClass('error');
			$(element).parents('.control-group').addClass('success');
		}
	});
	$("#addcusto").validate({
		rules:{
		required:{
				required:true,
				minlength:8,
				maxlength:40
			},
			email:{
				required:true,
				email: true,
				minlength:8,
				maxlength:50

			},
			pwd:{
				required: true,
				minlength:8,
				maxlength:40
			},
			pwd2:{
				required:true,
				minlength:8,
				maxlength:40,
				equalTo:"#pwd"
			}
		},
		errorClass: "help-inline",
		errorElement: "span",
		highlight:function(element, errorClass, validClass) {
			$(element).parents('.control-group').addClass('error');
		},
		unhighlight: function(element, errorClass, validClass) {
			$(element).parents('.control-group').removeClass('error');
			$(element).parents('.control-group').addClass('success');
		}
	});


		$("#addcusto2").validate({
		rules:{
		required1:{
				required:true,
				minlength:8,
				maxlength:40
			},
			email1:{
				required:true,
				email: true,
				minlength:8,
				maxlength:50

			},
			pwd1:{
				required: true,
				minlength:8,
				maxlength:40
			},
			pwd21:{
				required:true,
				minlength:8,
				maxlength:40,
				equalTo:"#pwd1"
			}
		},
		errorClass: "help-inline",
		errorElement: "span",
		highlight:function(element, errorClass, validClass) {
			$(element).parents('.control-group').addClass('error');
		},
		unhighlight: function(element, errorClass, validClass) {
			$(element).parents('.control-group').removeClass('error');
			$(element).parents('.control-group').addClass('success');
		}
	});
});
