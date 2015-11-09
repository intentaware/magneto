'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')();

const pngquant = require('imagemin-pngquant');

var paths = gulp.paths;

gulp.task('images', function() {
  return gulp.src([
      paths.src + '/**/imgs/*'
    ])
    .pipe($.imagemin({
      progressive: true,
      svgoPlugins: [{
        removeViewBox: false
      }],
      use: [pngquant()]
    }))
    .pipe(gulp.dest(paths.django.assets.dashboard));
});
