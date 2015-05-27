'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

gulp.task('partials', function() {
  return gulp.src([
      paths.src + '/{app,components}/**/*.html',
      paths.compile + '/{app,components}/**/*.html'
    ])
    .pipe($.minifyHtml({
      empty: true,
      spare: true,
      quotes: true
    }))
    .pipe($.angularTemplatecache('templateCacheHtml.js', {
      module: 'dash'
    }))
    .pipe(gulp.dest(paths.compile + '/partials/'));
});

gulp.task('html:common', ['inject:common'], function() {
  var assets;
  var cssFilter = $.filter('**/*.css');

  gulp.src(paths.django.common + '/__base.html')
    .pipe($.debug())
    .pipe($.replace('{{ STATIC_URL }}dash/', ''))
    .pipe(assets = $.useref.assets({
      searchPath: ['.']
    }))
    .pipe($.rev())
    .pipe(cssFilter)
    .pipe($.csso())
    .pipe($.debug())
    .pipe(cssFilter.restore())
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe(gulp.dest('compile'));
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

  gulp.src(paths.django.debug + '/__base.html')
    .pipe($.debug())
    .pipe($.replace('{{ STATIC_URL }}dash/', ''))
    .pipe(assets = $.useref.assets({
     searchPath: ['.']
    }))
    .pipe($.debug())
    .pipe(jsFilter)
    .pipe($.ngAnnotate())
    .pipe($.uglify({preserveComments: $.uglifySaveLicense}))
    .pipe(jsFilter.restore())
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe(gulp.dest('compile/build'));
})

gulp.task('html', ['html:common', 'html:dashboard']);

// gulp.task('html', ['inject'], function () {
//   /*var partialsInjectFile = gulp.src(paths.compile + '/partials/templateCacheHtml.js', { read: false });
//   var partialsInjectOptions = {
//     starttag: '<!-- inject:partials -->',
//     ignorePath: paths.compile + '/partials',
//     addRootSlash: false
//   };
//   */

//   var htmlFilter = $.filter('*.html');
//   var jsFilter = $.filter('**/*.js');
//   var cssFilter = $.filter('**/*.css');
//   var assets;

//   return gulp.src(paths.django.common + '/__base.html')
//     //.pipe($.inject(partialsInjectFile, partialsInjectOptions))
//     .pipe(assets = $.useref.assets())
//     .pipe($.debug({title: 'inspect:'}))
//     .pipe($.rev())
//     .pipe(jsFilter)
//     .pipe($.ngAnnotate())
//     .pipe($.uglify({preserveComments: $.uglifySaveLicense}))
//     .pipe(jsFilter.restore())
//     .pipe(cssFilter)
//     .pipe($.csso())
//     .pipe(cssFilter.restore())
//     .pipe(assets.restore())
//     .pipe($.useref())
//     .pipe($.revReplace())
//     .pipe(htmlFilter)
//     .pipe($.minifyHtml({
//       empty: true,
//       spare: true,
//       quotes: true
//     }))
//     .pipe(htmlFilter.restore())
//     .pipe(gulp.dest(paths.django.dist + '/'))
//     .pipe($.size({ title: paths.dist + '/', showFiles: true }));
//   });

// gulp.task('images', function () {
//   return gulp.src(paths.src + '/assets/images/**/*')
//   .pipe(gulp.dest(paths.dist + '/assets/images/'));
// });

// gulp.task('fonts', function () {
//   return gulp.src($.mainBowerFiles())
//   .pipe($.filter('**/*.{eot,svg,ttf,woff}'))
//   .pipe($.flatten())
//   .pipe(gulp.dest(paths.dist + '/fonts/'));
// });

// gulp.task('misc', function () {
//   return gulp.src(paths.src + '/**/*.ico')
//   .pipe(gulp.dest(paths.dist + '/'));
// });

gulp.task('clean', function(done) {
  $.del([paths.dist + '/', paths.compile + '/'], done);
  $.del([paths.django.dist + '/'], {
    force: true
  });
});

gulp.task('build', ['html', 'images', 'fonts', 'misc']);
