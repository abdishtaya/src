 $(document).ready(function() {
    $('#register-form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
           'username':{
                validators: {
                     stringLength: {
                        min: 4,
                    },
                    notEmpty: {
                        message: 'Please supply your last name'
                    }
                }
            },
			 type: {
                validators: {
                    notEmpty: {
                        message: 'Please select your type'
                    }
                }
            },
		   
                 'email': {
                validators: {
                    notEmpty: {
                        message: 'Please supply your email address'
                    },
                    emailAddress: {
                        message: 'Please supply a valid email address'
                    }
                }
            },
			 'password': {
                validators: {
                     stringLength: {
                        min: 8,
						max:25,
                    },

                    notEmpty: {
                        message: 'Please supply your password'
                    }
                }
            },
			   'confirm-password': {
				   
                validators: {
                  
                    notEmpty: {
                        message: 'Please supply your  repassword'
                    },
					  identical: {
                        field: 'password',
                        message: 'The password and its confirm are not the same'
                    }
					
                }
				
            },
          
           
            }
        })
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
                $('#').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('sendmessage'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});
