/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

//var jquery = require('jquery');
//var $ = jquery.jQuery;

$(document).ready(function(){
  console.log('ready');  
    
    $(document).mouseover(function(){
        $('body').attr('style','background-color:black');
    });
    $(document).mouseleave(function(){
        $('body').attr('style','background-color:none');
    });
    
    
});



