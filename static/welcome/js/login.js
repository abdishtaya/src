 $(document).ready(function() {
    $('#login-form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
           
                 'email_usename': {
                validators: {
                    notEmpty: {
                        message: 'Please supply your username or email address'
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
