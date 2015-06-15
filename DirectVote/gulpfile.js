/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


var gulp = require('gulp');   
    sass = require('gulp-ruby-sass') ;
    notify = require("gulp-notify") ;
    bower = require('gulp-bower');
    
    var config = {
     sassPath: './main/front-end/sass',
     bowerDir: './bower_components' 
};

gulp.task('bower', function() { 
    return bower()
         .pipe(gulp.dest(config.bowerDir)) ;
});

gulp.task('icons', function() { 
    return gulp.src(config.bowerDir + '/fontawesome/fonts/**.*') 
        .pipe(gulp.dest('./main/static/fonts')); 
});


/*gulp.task('css', function() {
    return sass(config.sassPath, { style: 'compressed' })
    .on("error", notify.onError(function (error) {
                 return "Error: " + error.message;
             }))
        .pipe(gulp.dest('./main/static/css'));
});*/


gulp.task('css', function() { 
    return gulp.src(config.sassPath + '/main.scss')
         .pipe(sass({
             style: 'compressed',
             loadPath: [
                 './main/front-end/sass',
                 config.bowerDir + '/bootstrap-sass-official/assets/stylesheets',
                 config.bowerDir + '/fontawesome/scss'
             ]
         }) 
            .on("error", notify.onError(function (error) {
                 return "Error: " + error.message;
             }))) 
         .pipe(gulp.dest('./main/static/css')); 
});

// Rerun the task when a file changes
 gulp.task('watch', function() {
     gulp.watch(config.sassPath + '/**/*.scss', ['css']); 
});

  gulp.task('default', ['bower', 'icons', 'css']);
  
  