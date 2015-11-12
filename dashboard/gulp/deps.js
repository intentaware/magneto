'use strict';

var gulp = require('gulp');
var wiredep = require('wiredep');
var mbf = require('main-bower-files');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

gulp.task('deps:css', function() {
  return gulp.src(wiredep().css)
    .pipe(gulp.dest(paths.compile + '/vendor/css'));
});

gulp.task('deps:js', function() {
  return gulp.src(wiredep().js)
    .pipe($.sourcemaps.init())
    .pipe($.concat('vendor.js'))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest(paths.compile + '/vendor/js'));
});

gulp.task('deps:swf', function() {
  return gulp.src(mbf())
    .pipe($.filter(['*.swf']))
    .pipe(gulp.dest(paths.django.assets.dashboard + '/swf'));
});
