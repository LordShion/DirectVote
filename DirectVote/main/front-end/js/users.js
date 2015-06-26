/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

module.exports = {
  login :   function(){
      data = {  
                user    :   $('#mn-in-login-user').val(),
                pass    :   btoa($('#mn-in-login-pass').val())
            };
            
            console.log(data);
      $.ajaxSetup({beforeSend: function(xhr, settings){
            xhr.setRequestHeader('X-CSRFToken', $('input[name="csrfmiddlewaretoken"]').attr('value'));
        }});
                
      $.ajax({
			type: 'POST',
			url: '/login/submit',
			data: JSON.stringify(data),
			dataType:"json",
			contentType: "application/json; charset=utf-8"
		}).done(function(response){
          console.log(response);
          console.log('login successfull');
          window.location = '/';
      }).fail(function(error){
          console.log(error);
          
      });
      
  }
};
