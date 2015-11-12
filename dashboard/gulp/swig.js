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
    .pipe($.changed(paths.django.templates.root))
    .pipe($.swig({defaults: { cache: false }}))
    .pipe(gulp.dest(paths.django.templates.root));
});

gulp.task('partials', function() {
  return gulp.src([
      paths.html.root + '/partials/**/*.html',
      '!' + paths.html.root + '/**/__*.html',
    ])
    .pipe($.swig({defaults: { cache: false }}))
    .pipe($.minifyHtml())
    .pipe($.angularTemplatecache('template-cache.js', {
      module: 'adomattic.dashboard'
    }))
    .pipe($.debug({
      title: 'updating templating cache'
    }))
    .pipe(gulp.dest(paths.compile + '/source/js/dashboard/templates'));
});
