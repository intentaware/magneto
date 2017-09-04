'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

gulp.task('lint', function () {
  return gulp.src([
    paths.src + '/js/**/*.js'
    // '!' + paths.src + '/js/**/auth/**/*.js',
    // '!' + paths.src + '/{app,components}/**/*.spec.js',
    // '!' + paths.src + '/{app,components}/**/*.mock.js'
  ])
  .pipe($.debug())
  .pipe($.eslint({
    fix: true
  }))
  .pipe($.eslint.format())
  .pipe(gulp.dest(paths.src + '/js/'));
});
