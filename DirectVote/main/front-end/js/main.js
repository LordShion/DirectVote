/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var users = require('./users.js');
    users.init();
    $(document).ready(function () {
        users.jstart();
    });