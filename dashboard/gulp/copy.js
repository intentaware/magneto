'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')();

var paths = gulp.paths;

gulp.task('copy:css', ['inject:common'], function() {
  return gulp.src([
      paths.compile + '/**/*.css'
    ])
    .pipe(gulp.dest(paths.django.assets.dashboard));
});

gulp.task('copy:js', ['inject:dashboard'], function() {
  return gulp.src([
      paths.compile + '/**/*.js',
    ])
    .pipe($.changed(paths.django.assets.dashboard))
    .pipe($.debug({
      title: 'copying changed files'
    }))
    .pipe(gulp.dest(paths.django.assets.dashboard));
});

gulp.task('copy', ['copy:css', 'copy:js', 'inject:auth', 'swig', 'images']);
