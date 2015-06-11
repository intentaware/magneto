'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync');
var reload = browserSync.reload;

var paths = gulp.paths;

gulp.task('watch', ['inject'], function () {
  gulp.watch([
    //paths.src + '/js/**/*.js',
    paths.compile + '/**/*.css',
  ])
  //.on('change', reload);

  gulp.watch([
    paths.src + '/*.html',
    paths.src + '/assets/**/*.scss',
    //paths.src + '/js/**/*.js',
    'bower.json'
  ], ['inject']);
});
