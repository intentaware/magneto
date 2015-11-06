'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

gulp.task('copy:css', function() {
  return gulp.src([
      paths.compile + '/**/*.css'
    ])
  .pipe(gulp.dest(paths.django.assets.dashboard));
});
