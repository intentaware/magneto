'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

var paths = gulp.paths;


gulp.task('ng', function() {
  return gulp.src([
      paths.src + '/js/**/*.js',
      //'!' + paths.src + '/js/**/auth/**/*.js',
      //'!' + paths.src + '/{app,components}/**/*.spec.js',
      //'!' + paths.src + '/{app,components}/**/*.mock.js'
    ])
    .pipe($.angularFilesort())
    .pipe($.ngAnnotate({
      single_quotes: true
    }))
    .pipe($.debug({
      title: 'angular source'
    }))
    .pipe($.jshint())
    .pipe($.jshint.reporter('jshint-stylish'))
    .pipe(gulp.dest(paths.compile + '/source/js'));
});
