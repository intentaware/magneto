'use strict';

var gulp = require('gulp');
var wiredep = require('wiredep');
/* jshint ignore:start */
var _ = require('lodash');
/* jshint ignore:end */


var $ = require('gulp-load-plugins')();

var paths = gulp.paths;

// common inject options
var injectOptions = {
  ignorePath: [paths.src, paths.compile],
  addRootSlash: false,
  addPrefix: '{{ STATIC_URL }}dashboard'
    //relative: true
};

var vendorOptions = _.merge({
  name: 'bower'
}, injectOptions);

gulp.task('install:css', function() {
  return gulp.src(wiredep().css)
    .pipe(gulp.dest(paths.compile + '/vendor/css'));
});

gulp.task('install:js', function() {
  return gulp.src(wiredep().js)
    .pipe($.sourcemaps.init())
      .pipe($.concat('vendor.js'))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest(paths.compile + '/vendor/js'));
});

// injectionstyles common base
gulp.task('inject:common', ['styles', 'install:css'], function() {
  // style injection for application styles
  var injectStyles = gulp.src([
    paths.compile + '/source/**/*.css',
    //'!' + paths.compile + '/vendor/**/*.css'
  ], {
    read: false
  }).pipe($.debug({
    title: 'dashboard styles'
  }));

  // style setup for vendor styles
  var vendorStyles = gulp.src([
    paths.compile + '/vendor/**/*.css',
    //'!' + paths.compile + '/serve/**/*.css',
  ], {
    read: false
  }).pipe($.debug({
    title: 'vendor styles'
  }));

  // the actual task
  return gulp.src(paths.html.root + '/__base.html')
    .pipe($.inject(vendorStyles, vendorOptions))
    .pipe($.inject(injectStyles, injectOptions))
    .pipe(gulp.dest(paths.django.templates.root));
});


// injecting scripts into dashboard
gulp.task('inject:dashboard', ['ng', 'install:js', 'partials'], function() {

  var injectScripts = gulp.src([
      paths.compile + '/source/**/*.js',
      '!' + paths.compile + '/source/**/auth/**/*.js',
      '!' + paths.compile + '/source/**/templates/*.js'
    ])
    .pipe($.angularFilesort())
    .pipe($.debug({
      title: 'dashboard scripts'
    }));

  // style setup for vendor styles
  var vendorScripts = gulp.src([
    paths.compile + '/vendor/**/*.js',
    //'!' + paths.compile + '/serve/**/*.css',
  ], {
    read: false
  }).pipe($.debug({
    title: 'vendor scripts'
  }));

  var templateCache = gulp.src([
      paths.compile + '/source/**/templates/**/*.js'
    ]).pipe($.debug({
      title: 'dashboard partials'
    }));

  var cacheOptions = _.merge({
    name: 'partials'
  }, injectOptions);

  return gulp.src(paths.html.root + '/__dashboard.html')
    .pipe($.inject(injectScripts, injectOptions))
    .pipe($.inject(vendorScripts, vendorOptions))
    .pipe($.inject(templateCache, cacheOptions))
    .pipe(gulp.dest(paths.django.templates.root));
});

// injecting into auth
gulp.task('inject:auth', ['styles'], function() {

  var injectScripts = gulp.src([
    paths.src + '/js/auth/**/*.js'
    //'!' + paths.src + '/auth/**/*.spec.js',
    //'!' + paths.src + '/auth/**/*.mock.js'
  ]).pipe($.angularFilesort());

  return gulp.src(paths.html.root + '/__dashboard.html')
    .pipe($.inject(injectScripts, injectOptions))
    .pipe(gulp.dest(paths.django.auth));

});


gulp.task('inject', ['inject:common', 'inject:dashboard']);
