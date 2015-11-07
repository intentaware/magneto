'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync');

var paths = gulp.paths;

function browserSyncInit(baseDir, files, browser) {
  browser = browser === undefined ? 'default' : browser;

  browserSync.instance = browserSync.init(files, {
    startPath: '/',
    /*)
    server: {
      baseDir: baseDir,
      middleware: middleware
      //routes: routes
    },
    */
    browser: browser,
    host:'0.0.0.0',
    port: '9050',
    proxy: 'http://localhost:8000/'
  });
}

// task to serve development with live refresh
gulp.task('serve', ['watch', 'copy'], function () {
  browserSyncInit([], [
    paths.django.assets.dashboard + '/**/*.css',
    paths.django.assets.dashboard + '/**/*.js',
    '!' + paths.django.assets.dashboard + '/**/vendor.js',
    paths.django.templates.root + '/**/*.html'
    //paths.src + '/{app,components}/**/*.js',
    //paths.src + 'src/assets/images/**/*',
    //paths.compile + '/serve/*.html',
    //paths.compile + '/serve/{app,components}/**/*.html',
    //paths.src + '/{app,components}/**/*.html'
  ]);
});

// task to quick preview the build files
gulp.task('preview', ['build'], function () {
  browserSyncInit([], [
    paths.django.assets.dashboard + '/**/*.css',
    paths.django.assets.dashboard + '/**/*.js',
    '!' + paths.django.assets.dashboard + '/**/vendor.js',
    paths.django.templates.root + '/**/*.html'
    //paths.src + '/{app,components}/**/*.js',
    //paths.src + 'src/assets/images/**/*',
    //paths.compile + '/serve/*.html',
    //paths.compile + '/serve/{app,components}/**/*.html',
    //paths.src + '/{app,components}/**/*.html'
  ]);
});
