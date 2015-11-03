'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

var paths = gulp.paths;

gulp.task('clean', function(done) {
  $.del([paths.dist + '/', paths.compile + '/'], done);
  $.del([paths.django.dist + '/'], {
    force: true
  });
});
