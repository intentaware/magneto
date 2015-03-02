'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

gulp.task('watch', ['inject'], function () {
  gulp.watch([
    paths.src + '/*.html',
    paths.src + '/assets/**/*.scss',
    paths.src + '/js/**/*.js',
    'bower.json'
  ], ['inject']);
});
