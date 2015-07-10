/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
require("expose?$!jquery");
require("expose?commons!./commonBindings.js");
require('jquery-cookie');


// uncomment or comment this this for  console logging;
console.log = function(){    return; };


var users = require('./users.js');


 
    users.init();
    $(document).ready(function () {
        users.jstart();
        $(document).on('load',function(){
            console.log('document changed');
            commons.collapsables();
        });
        
        
    });
    
