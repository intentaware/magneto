'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del']
});


gulp.task('minify:common', ['inject:common'], function() {
  var assets,
    cssFilter = $.filter('**/*.css');

  return gulp.src(paths.django.templates.root + '/__base.html')
    //.pipe($.debug())
    .pipe($.replace('{{ STATIC_URL }}dashboard', 'compile'))
    .pipe(assets = $.useref.assets({
      searchPath: ['.']
    }))
    .pipe($.rev())
    .pipe(cssFilter)
    .pipe($.csso())
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
    .pipe($.replace('{{ STATIC_URL }}dashboard', 'compile'))
    //.pipe($.debug())
    .pipe(assets = $.useref.assets({
      searchPath: ['.']
    }))
    .pipe($.rev())
    .pipe(jsFilter)
    //.pipe($.ngAnnotate())
    .pipe($.uglify({
      preserveComments: $.uglifySaveLicense
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
    .pipe($.replace('{{ STATIC_URL }}dashboard', 'compile'))
    //.pipe($.debug())
    .pipe(assets = $.useref.assets({
      searchPath: ['.']
    }))
    .pipe($.rev())
    .pipe(jsFilter)
    //.pipe($.ngAnnotate())
    .pipe($.uglify({
      preserveComments: $.uglifySaveLicense
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
  return  gulp.src('compile/builds/*.html')
    .pipe(gulp.dest(paths.django.templates.root));
});

gulp.task('build', ['restore:html', 'swig', 'images']);
