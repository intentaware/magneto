'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')();

gulp.task('styles', function () {

  var sassOptions = {
    style: 'expanded'
  };

  var injectFiles = gulp.src([
    paths.src + '/assets/styles/**/*.scss'
  ], { read: false });

  var injectOptions = {
    transform: function(filePath) {
      filePath = filePath.replace(paths.src + '/app/', '');
      filePath = filePath.replace(paths.src + '/components/', '../components/');
      return '@import \'' + filePath + '\';';
    },
    starttag: '// injector',
    endtag: '// endinjector',
    addRootSlash: false
  };

  var indexFilter = $.filter('main.scss');

  return gulp.src([
    paths.src + '/scss/main.scss'
  ])
    //.pipe(indexFilter)
    //.pipe($.inject(injectFiles, injectOptions))
    //.pipe(indexFilter.restore())
    .pipe($.sourcemaps.init())
    .pipe($.sass(sassOptions))
    .pipe($.sourcemaps.write())
    .pipe($.autoprefixer())
    .pipe($.size())
    .on('error', function handleError(err) {
      console.error(err.toString());
      this.emit('end');
    })
    .pipe(gulp.dest(paths.compile + '/serve/styles'));
});
