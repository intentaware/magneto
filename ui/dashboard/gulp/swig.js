'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

var paths = gulp.paths;


gulp.task('swig', function() {
  return gulp.src([
      paths.html.root + '/**/*.html',
      '!' + paths.html.root + '/**/__*.html',
      '!' + paths.html.root + '/partials/**/*.html'
    ])
    .pipe($.swig())
    .pipe(gulp.dest(paths.compile + '/html'));
});

gulp.task('partials', function() {
  return gulp.src([
      paths.html.root + '/partials/**/*.html',
      '!' + paths.html.root + '/**/__*.html',
    ])
  .pipe($.swig())
  .pipe($.minifyHtml())
  .pipe($.angularTemplatecache('template-cache.js', {
    module: 'adomattic.dashboard'
  }))
  .pipe(gulp.dest(paths.compile + '/source/js/dashboard/templates'));
});
