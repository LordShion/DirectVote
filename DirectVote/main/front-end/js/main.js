/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
require("expose?$!jquery");
require("expose?commons!./commonBindings.js");
require('../../../bower_components/jquery-cookie/jquery.cookie');
require('../../../bower_components/bootstrap');


// uncomment or comment this this for  console logging;
// console.log = function(){    return; };

      var messages_handler = require('./messages_handler.js');

var users = require('./users.js');


    messages_handler.init();
    users.init();


    $(document).ready(function () {
        users.jstart();
        commons.links('#startpage');
        $(document).on('load',function(){
            console.log('document changed');
            commons.collapsables();

        });


    });

