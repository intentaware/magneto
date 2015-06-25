'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')();

var wiredep = require('wiredep').stream;

// default file, generated by yeoman
// kept, for future reference


// gulp.task('inject', ['styles'], function () {

//   var injectStyles = gulp.src([
//     paths.compile + '/serve/{app,components}/**/*.css',
//     '!' + paths.compile + '/serve/app/vendor.css'
//   ], { read: false });

//   var injectScripts = gulp.src([
//     paths.src + '/{app,components}/**/*.js',
//     '!' + paths.src + '/{app,components}/**/*.spec.js',
//     '!' + paths.src + '/{app,components}/**/*.mock.js'
//   ]).pipe($.angularFilesort());

//   var injectOptions = {
//     ignorePath: [paths.src, paths.compile + '/serve'],
//     addRootSlash: false
//   };

//   var wiredepOptions = {
//     directory: 'bower_components',
//     exclude: [/bootstrap\.css/, /foundation\.css/]
//   };

//   return gulp.src(paths.src + '/*.html')
//     .pipe($.inject(injectStyles, injectOptions))
//     .pipe($.inject(injectScripts, injectOptions))
//     .pipe(wiredep(wiredepOptions))
//     .pipe(gulp.dest(paths.compile + '/serve'));

// });

var injectOptions = {
  //ignorePath: [paths.src, paths.compile + '/serve'],
  addRootSlash: false,
  addPrefix: '{{ STATIC_URL }}dash'
    //relative: true
};

var wiredepScripts = {
  directory: 'bower_components',
  ignorePath: '../../static/',
  exclude: ['.css'],
  fileTypes: {
    html: {
      replace: {
        js: '<script src="{{ STATIC_URL }}{{filePath}}"></script>'
          //css: '<link rel="stylesheet" href="{{ STATIC_URL }}{{filePath}}" />'
      }
    }
  }
};

var wiredepStyles = {
  directory: 'bower_components',
  ignorePath: '../static/',
  exclude: ['.js', 'materialdesignicons.css'],
  fileTypes: {
    html: {
      replace: {
        //js: '<script src="{{ STATIC_URL }}{{filePath}}"></script>'
        css: '<link rel="stylesheet" href="{{ STATIC_URL }}{{filePath}}" />'
      }
    }
  }
};

// injection into common base
gulp.task('inject:common', ['styles'], function() {
  var injectStyles = gulp.src([
    paths.compile + '/serve/**/*.css',
    //'!' + paths.compile + '/serve/app/vendor.css'
  ], {
    read: false
  }).pipe($.print());

  return gulp.src(paths.django.common + '/__base.html')
    .pipe($.inject(injectStyles, injectOptions))
    .pipe(wiredep(wiredepStyles))
    .pipe(gulp.dest(paths.django.common));
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
    .pipe(wiredep(wiredepScripts))
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
    .pipe(wiredep(wiredepScripts))
    .pipe(gulp.dest(paths.django.auth));

});


gulp.task('inject', ['inject:common', 'inject:dashboard', 'inject:auth']);
