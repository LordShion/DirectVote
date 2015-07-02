/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


var gulp = require('gulp'),   
    sass = require('gulp-ruby-sass') ,
    notify = require("gulp-notify") ,
    bower = require('gulp-bower'),
    sourcemaps = require('gulp-sourcemaps'),
    jshint     = require('gulp-jshint'),
    concat = require('gulp-concat'),
    gutil = require('gulp-util'),
    uglify = require('gulp-uglify'),
    
    webpack = require('gulp-webpack'),
    webpackConfig = require('./webpack.config.js');
    
    
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
        .pipe(gulp.dest('./main/static/main/fonts')); 
});

gulp.task('js', function (cb) {
  return gulp.src('')
  .pipe(webpack(webpackConfig))
  .pipe(gulp.dest('./main/static/main/js'));
});

//gulp.task('build-js', function() {
//  return gulp.src('./main/front-end/js/**/*.js')
//    .pipe(sourcemaps.init())
 //     .pipe(concat('bundle.js'))
//      //only uglify if gulp is ran with '--type production'
//////      .pipe(gutil.env.type === 'production' ? uglify() : gutil.noop()) 
 //   .pipe(sourcemaps.write())
 //   .pipe(gulp.dest('./main/static/main/js'));
//});


gulp.task('css', function() {
    return sass(
                 './main/front-end/sass',  {style: 'compressed' ,
             loadPath: [
                 './main/front-end/sass',
                 config.bowerDir + '/bootstrap-sass-official/assets/stylesheets',
                 config.bowerDir + '/fontawesome/scss',
             ]
         })
        .pipe(gulp.dest('./main/static/main/css'));
});


// Rerun the task when a file changes
 gulp.task('watch', function() {
     gulp.watch(config.sassPath + '/**/*.scss', ['css']); 
});

  gulp.task('default', ['bower', 'icons', 'css', 'js']);
  
  