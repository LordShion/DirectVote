module.exports = {

    self: this,
    init: (function(){
            console.log('init messages handler');
            var self = this;

            self.system = function(message){
                console.log('system message called');
                console.log('passed message = ' + message);
                };

        })
    }