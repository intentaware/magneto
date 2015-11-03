'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')();

var wiredep = require('wiredep');

var injectOptions = {
  //ignorePath: [paths.src, paths.compile + '/serve'],
  addRootSlash: false,
  addPrefix: '{{ STATIC_URL }}dashboard'
    //relative: true
};

gulp.task('install:css', function() {
  return gulp.src(wiredep().css)
    .pipe(gulp.dest(paths.compile + '/serve/vendor/css'));
});

gulp.task('install:js', function() {
  return gulp.src(wiredep().js)
    .pipe(gulp.dest(paths.compile + '/serve/vendor/js'));
});

// injectionstyles common base
gulp.task('inject:common', ['styles', 'install:css'], function() {
  // style injection stream setup
  var injectStyles = gulp.src([
    paths.compile + '/serve/**/*.css',
    '!' + paths.compile + '/serve/vendor/**/*.css'
  ], {
    read: false
  });


  // i don't know why this works but this works !!
  // the funny thing, it automatically injects the files in the write places
  var vendorStyles = gulp.src([
    paths.compile + '/serve/vendor/**/*.css',
    //'!' + paths.compile + '/serve/**/*.css',
  ], {
    read: false
  }).pipe($.debug());

  var vendorOptions = {
    //ignorePath: [paths.src, paths.compile + '/serve'],
    name: 'bower',
    addRootSlash: false,
    addPrefix: '{{ STATIC_URL }}dashboard'
      //relative: true
  };

  return gulp.src(paths.html.root + '/__base.html')
    .pipe($.inject(vendorStyles, vendorOptions))
    .pipe($.inject(injectStyles, injectOptions))
    .pipe(gulp.dest(paths.django.templates.root));
});


// injecting into dashboard
gulp.task('inject:dashboard', ['styles'], function() {

  var injectScripts = gulp.src([
      paths.src + '/js/**/*.js',
      '!' + paths.src + '/js/auth/**/*.js'
      //'!' + paths.src + '/{app,components}/**/*.spec.js',
      //'!' + paths.src + '/{app,components}/**/*.mock.js'
    ])
    .pipe($.angularFilesort())
    .pipe($.jshint())
    .pipe($.jshint.reporter('jshint-stylish'));

  return gulp.src(paths.django.debug + '/__base.html')
    .pipe($.inject(injectScripts, injectOptions))
    .pipe(gulp.dest(paths.django.debug));

});

// injecting into auth
gulp.task('inject:auth', ['styles'], function() {

  var injectScripts = gulp.src([
    paths.src + '/js/auth/**/*.js'
    //'!' + paths.src + '/auth/**/*.spec.js',
    //'!' + paths.src + '/auth/**/*.mock.js'
  ]).pipe($.angularFilesort());

  return gulp.src(paths.django.auth + '/__base.html')
    .pipe($.inject(injectScripts, injectOptions))
    .pipe(gulp.dest(paths.django.auth));

});


gulp.task('inject', ['inject:common', 'inject:dashboard', 'inject:auth']);
