/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

module.exports = {
        collapsables: function (){

                $('.clickcollapse').on('click',function(event){
                    console.log('collapsing/expanding');

                                if ($(this).next('.mycollapse').height()>0) {
                                    $(this).next('.mycollapse').height(0);
                                    $(this).children('.glyphicon').removeClass('glyphicon-chevron-down');
                                    $(this).children('.glyphicon').addClass('glyphicon-chevron-right');
                                } else {
                                    $(this).next('.mycollapse').height($(this).next('.mycollapse').children('.expandsize').height());
                                    $(this).children('.glyphicon').removeClass('glyphicon-chevron-right');
                                    $(this).children('.glyphicon').addClass('glyphicon-chevron-down');
                                };


                            });




    }
};
