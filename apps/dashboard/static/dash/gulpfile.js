'use strict';

var gulp = require('gulp');

gulp.paths = {
  src: 'src',
  dist: 'dist',
  compile: 'compile',
  e2e: 'e2e',
  django: {
    debug: '../../templates/debug',
    compile: '../../templates/compile',
    common:'../../templates',
    auth: '../../templates/registration'
  }
};

require('require-dir')('./gulp');

gulp.task('default', ['clean'], function () {
    gulp.start('serve');
});
