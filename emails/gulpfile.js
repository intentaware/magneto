'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

gulp.task('emails', function() {
    gulp.src('./src/*.html')
      .pipe($.inlineCss({}))
      .pipe(gulp.dest('../../apps/dashboard/templates/emails'));
  });

gulp.task('default', ['emails'], function() {

  });
