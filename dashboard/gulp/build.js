'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});

var uglifyCompressOptions = {
  sequences: true, // join consecutive statemets with the “comma operator”
  properties: true, // optimize property access: a["foo"] → a.foo
  dead_code: true, // discard unreachable code
  drop_debugger: true, // discard “debugger” statements
  conditionals: true, // optimize if-s and conditional expressions
  comparisons: true, // optimize comparisons
  evaluate: true, // evaluate constant expressions
  booleans: true, // optimize boolean expressions
  loops: true, // optimize loops
  unused: true, // drop unused variables/functions
  hoist_funs: true, // hoist function declarations
  hoist_vars: false, // hoist variable declarations
  if_return: true, // optimize if-s followed by return/continue
  join_vars: true, // join var declarations
  cascade: true, // try to cascade `right` into `left` in sequences
  side_effects: true, // drop side-effect-free statements
  warnings: false, // warn about potentially dangerous optimizations/code
  drop_console: true // drops console.log statements
};


gulp.task('minify:common', ['inject:common'], function() {
  var assets,
    cssFilter = $.filter('**/*.css');

  return gulp.src(paths.django.templates.root + '/__base.html')
    //.pipe($.debug())
    .pipe($.replace('href="{{ STATIC_URL }}dashboard', 'href="compile'))
    .pipe(assets = $.useref.assets({
      searchPath: ['.']
    }))
    .pipe($.rev())
    .pipe(cssFilter)
    //.pipe($.csso())
    .pipe($.size())
    .pipe(gulp.dest(paths.django.assets.dashboard + '/builds'))
    .pipe(cssFilter.restore())
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe($.revReplace())
    .pipe($.replace('href="styles', 'href="{{ STATIC_URL }}dashboard/builds/styles'))
    .pipe(gulp.dest('compile/builds'));
});

gulp.task('minify:dashboard', ['inject:dashboard'], function() {
  var assets,
    jsFilter = $.filter('**/*.js');

  return gulp.src(paths.django.templates.root + '/__dashboard.html')
    .pipe($.replace('script src="{{ STATIC_URL }}dashboard', 'script src="compile'))
    //.pipe($.debug())
    .pipe(assets = $.useref.assets({
      searchPath: ['.']
    }))
    .pipe($.rev())
    .pipe(jsFilter)
    //.pipe($.ngAnnotate())
    .pipe($.uglify({
      preserveComments: $.uglifySaveLicense,
      compress: uglifyCompressOptions
    }))
    .pipe($.size())
    .pipe(gulp.dest(paths.django.assets.dashboard + '/builds'))
    .pipe(jsFilter.restore())
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe($.revReplace())
    .pipe($.replace('src="scripts', 'src="{{ STATIC_URL }}dashboard/builds/scripts'))
    .pipe(gulp.dest('compile/builds'));
});

gulp.task('minify:auth', ['inject:auth'], function() {
  var assets,
    jsFilter = $.filter('**/*.js');

  return gulp.src(paths.django.templates.root + '/__auth.html')
    .pipe($.replace('script src="{{ STATIC_URL }}dashboard', 'script src="compile'))
    //.pipe($.debug())
    .pipe(assets = $.useref.assets({
      searchPath: ['.']
    }))
    .pipe($.rev())
    .pipe(jsFilter)
    //.pipe($.ngAnnotate())
    .pipe($.uglify({
      preserveComments: $.uglifySaveLicense,
      compress: uglifyCompressOptions
    }))
    .pipe($.size())
    .pipe(gulp.dest(paths.django.assets.dashboard + '/builds'))
    .pipe(jsFilter.restore())
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe($.revReplace())
    .pipe($.replace('src="scripts', 'src="{{ STATIC_URL }}dashboard/builds/scripts'))
    .pipe(gulp.dest('compile/builds'));
});

gulp.task('restore:html', ['minify:common', 'minify:dashboard', 'minify:auth'], function() {
  return gulp.src('compile/builds/*.html')
    .pipe(gulp.dest(paths.django.templates.root));
});

gulp.task('build', ['restore:html', 'swig', 'images']);
