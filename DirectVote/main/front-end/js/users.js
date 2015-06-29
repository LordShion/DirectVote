/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

module.exports = { 
    self: this,
    
    init:(function(){
    
    var self = this;
    
    self.jstart =  function(){
        console.log('restart js');
           
    
        $('#mn-fm-login input[type=submit]').on('click', function () {
            console.log(event);
            self.login();
        });

            $('.bt_logout').on('click', function () {
            console.log(event);
            self.logout();
        });

    },

           
  
  self.login =   function(){
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
                    console.log( $('#login_header_space') );


                    self.loadpage('#login_header_space',"view/login.html");
                    self.loadpage('#main_page',"view/page_start.html");
                    
          
          
                }).fail(function(error){
                    console.log('error submitting login');
                });
      
  };
  self.logout = function(){
  
        $.ajaxSetup({beforeSend: function(xhr, settings){
                  xhr.setRequestHeader('X-CSRFToken', $('input[name="csrfmiddlewaretoken"]').attr('value'));
              }});

        $.ajax({
			type: 'POST',
			url: '/logout',
			data: '',
			dataType:"json",
			contentType: "application/json; charset=utf-8"
		}).done(function(response){
          console.log(response);
          console.log('logout successfull');
          
          self.loadpage('#login_header_space',"view/login.html");
          self.loadpage('#main_page',"view/page_start.html");


      }).fail(function(error){
          console.log(error);
          
      });
  
  };
  self.loadpage =  function(obj,name){
      
      $(obj).load( name, function( response, status, xhr ) {
                if ( status === "error" ) {
                  var msg = "Sorry but there was an error: " +name;
                  console.log( msg + xhr.status + " " + xhr.statusText );
                }else{
                    
                    var msg = "page loaded: "+name;
                    console.log( msg + xhr.status + " " + xhr.statusText );
                    $(document).ready(function () {
                        self.jstart();
                    });
                }
              });
      
      
  };
        
})

};
    
  
    

/*
{
    
  
  
 };

*/
