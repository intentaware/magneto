'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

var paths = gulp.paths;

gulp.task('watch', function() {
  gulp.watch([
      paths.src + '/**/*.scss'
    ], ['copy:css']);

  gulp.watch([
    paths.src + '/**/*.js',
    paths.src + '/**/partials/*.html'
    ], ['copy:js']);

  gulp.watch([
      paths.html.root + '/**/*.html',
      '!' + paths.html.root + '/**/__*.html',
      '!' + paths.html.root + '/partials/**/*.html'
    ], ['swig']);

  gulp.watch([
      paths.html.root + '/partials/**/*.html'
    ], ['copy:js']);
});
