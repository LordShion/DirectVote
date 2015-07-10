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
           
    
        $('.bt_login').on('click', function (event) {
            event.stopPropagation();
            
            self.login();
        });

            $('.bt_logout').on('click', function (event) {
                event.stopPropagation();
            
            self.logout();
        });
        
        $('a.ln').on('click',function(event) {
            event.stopPropagation();

            $('.nav li').removeClass("active");
            self.loadpage('#main_page', $(this).attr('data')).done(function(response){
                commons.collapsables();

            }).fail(function(error){
                console.log(error);
            });
            
            
        });
        
        $('.nav li').on('click',function(event) {
            
            $(this).addClass("active");
            
            
        });
        
        
        
        
        $('select[name=language]').on('change',function(event){
           console.log('language change detexted'); 
           $.ajaxSetup({beforeSend: function(xhr, settings){
            xhr.setRequestHeader('X-CSRFToken', $('input[name="csrfmiddlewaretoken"]').attr('value'));
        }});
           $.ajax({
			type: 'POST',
			url: '/i18n/setlang/',
			data: {language: $('select[name=language]').val()}
		}).done(function(response){


                    
                    $.when(self.loadpage('#login_header_space',"login"),
                        self.loadpage('#main_page',"page_start"),
                        self.loadpage('#navigation_page','navigation')).done(function(){
                            console.log('everything loaded');
                            self.jstart();
                        }).fail(function(){
                            console.log('error while loading');
                        });


                    
                    
          
          
                }).fail(function(error){
                    console.log('error changing language');
                });
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
                    /*console.log($.cookie('csrftoken'));
                    var csrftoken = $.cookie('csrftoken');
                    // set the token of the page with new token
                    $('input[name=csrfmiddlewaretoken]').val(csrftoken);*/
                    console.log(response);
                    console.log('login successfull');
                    console.log( $('#login_header_space') );


                    $.when(self.loadpage('#login_header_space',"login"),
                        self.loadpage('#main_page',"page_start"),
                        self.loadpage('#navigation_page','navigation')).done(function(){
                            console.log('everything loaded');
                            self.jstart();
                        }).fail(function(){
                            console.log('error while loading');
                        });
                    
          
          
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
                    //console.log($.cookie('csrftoken'));
                    //var csrftoken = $.cookie('csrftoken');
                    
                    
                    // set the token of the page with new token
                    //$('input[name=csrfmiddlewaretoken]').val(csrftoken);
          console.log(response);
          console.log('logout successfull');
          
          $.when(self.loadpage('#login_header_space',"login"),
            self.loadpage('#main_page',"page_start"),
            self.loadpage('#navigation_page','navigation')).done(function(){
                console.log('everything loaded');
                self.jstart();
            }).fail(function(){
                console.log('error while loading');
            });
          
         
                        
            


      }).fail(function(error){
          console.log(error);
          
      });
  
  };
  self.loadpage =  function(obj,name){
      var defer = $.Deferred();
      
      
      $(obj).load( "view/"+name, function( response, status, xhr ) {
                if ( status === "error" ) {
                  var msg = "Sorry but there was an error: " +name;
                  console.log( msg + xhr.status + " " + xhr.statusText );
                  defer.reject(response);
                }else{
                    
                    var msg = "page loaded: "+name;
                    console.log( msg + xhr.status + " " + xhr.statusText );
                    defer.resolve(response);
                    
                }
              });
      
     return defer.promise();; 
  };
        
})

};
    
  
    

/*
{
    
  
  
 };

*/
