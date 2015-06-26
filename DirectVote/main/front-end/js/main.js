/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var users = require('./users.js');

$(document).ready(function () {
    
    $('#mn-fm-login input[type=submit]').on('click', function () {
        //console.log(event);
        users.login();
    });



});





