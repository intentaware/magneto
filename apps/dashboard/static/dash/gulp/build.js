'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});


// gulp.task('partials', function() {
//   return gulp.src([
//       paths.src + '/{app,components}/**/*.html',
//       paths.compile + '/{app,components}/**/*.html'
//     ])
//     .pipe($.minifyHtml({
//       empty: true,
//       spare: true,
//       quotes: true
//     }))
//     .pipe($.angularTemplatecache('templateCacheHtml.js', {
//       module: 'dash'
//     }))
//     .pipe(gulp.dest(paths.compile + '/partials/'));
// });

gulp.task('html:common', ['inject:common'], function() {
  var assets;
  var cssFilter = $.filter('**/*.css');

  return gulp.src(paths.django.common + '/__base.html')
    ////.pipe($.debug())
    .pipe($.replace('{{ STATIC_URL }}dash/', ''))
    .pipe(assets = $.useref.assets({
      searchPath: ['.']
    }))
    .pipe($.rev())
    .pipe(cssFilter)
    .pipe($.csso())
    //.pipe($.debug())
    .pipe(cssFilter.restore())
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe($.revReplace())
    .pipe($.replace('href="styles/', 'href="{{ STATIC_URL }}dash/compile/common/styles/'))
    .pipe(gulp.dest('compile/common'));
});

gulp.task('html:dashboard', ['styles', 'inject:dashboard'], function() {
  var assets;
  var jsFilter = $.filter('**/*.js');

  var uglifyOptions = {
    mangle: {
      toplevel: true,
    },
    compress: {
      sequences: true,
      dead_code: true,
      conditionals: true,
      booleans: true,
      unused: true,
      if_return: true,
      join_vars: true,
      //drop_console: true
    },
    outSourceMap: false
  };

  return gulp.src(paths.django.debug + '/__base.html')
    //.pipe($.debug())
    .pipe($.replace('{{ STATIC_URL }}dash/', ''))
    .pipe(assets = $.useref.assets({
     searchPath: ['.']
    }))
    .pipe($.rev())
    //.pipe($.debug())
    .pipe(jsFilter)
    .pipe($.ngAnnotate())
    .pipe($.uglify({preserveComments: $.uglifySaveLicense}))
    .pipe(jsFilter.restore())
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe($.revReplace())
    .pipe($.replace('src="scripts/', 'src="{{ STATIC_URL }}dash/compile/dashboard/scripts/'))
    .pipe(gulp.dest('compile/dashboard'));
})

gulp.task('html:copy', ['html:dashboard', 'html:common'], function() {
  return gulp.src(paths.compile + '/dashboard/__base.html')
    //.pipe($.debug())
    .pipe($.minifyHtml({
      empty: true,
      spare: true,
      quotes: true
    }))
    .pipe(gulp.dest(paths.django.compile));
})

gulp.task('html', ['html:copy']);

gulp.task('clean', function(done) {
  $.del([paths.dist + '/', paths.compile + '/'], done);
  $.del([paths.django.dist + '/'], {
    force: true
  });
});

gulp.task('build', ['html', 'images', 'fonts', 'misc']);
