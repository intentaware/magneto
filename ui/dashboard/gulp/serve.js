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

gulp.task('serve', ['watch', 'copy'], function () {
  browserSyncInit([], [
    paths.django.assets.dashboard + '/**/*.css',
    paths.django.assets.dashboard + '/**/*.js',
    paths.django.templates.root + '/**/*.html'
    //paths.src + '/{app,components}/**/*.js',
    //paths.src + 'src/assets/images/**/*',
    //paths.compile + '/serve/*.html',
    //paths.compile + '/serve/{app,components}/**/*.html',
    //paths.src + '/{app,components}/**/*.html'
  ]);
});
