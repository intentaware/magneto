'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

gulp.task('watch', ['copy'], function() {
  gulp.watch([
      paths.src + '/**/*.scss'
    ], ['copy:css']);

  gulp.watch([
    paths.src + '/**/*.js'
    ], ['copy:js']);
});
