'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

gulp.task('copy:css', ['inject:common'], function() {
  return gulp.src([
      paths.compile + '/**/*.css'
    ])
  .pipe(gulp.dest(paths.django.assets.dashboard));
});

gulp.task('copy:js', ['inject:dashboard'], function() {
  return gulp.src([
      paths.compile + '/**/*.js'
    ])
  .pipe(gulp.dest(paths.django.assets.dashboard));
});
