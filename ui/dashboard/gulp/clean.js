'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

var paths = gulp.paths;

gulp.task('clean', function(done) {
  // deleting temporary files before copying them to django static
  $.del([paths.dist + '/', paths.compile + '/'], done);
  // deleting django files
  $.del([
    paths.django.assets.dashboard + '/',
    paths.django.templates.root + '/'
  ], {
    force: true
  });
});
