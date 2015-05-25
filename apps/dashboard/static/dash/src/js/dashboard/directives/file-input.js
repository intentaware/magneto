'use strict';

angular.module('adomattic.dashboard')
  .directive('inputFile', function() {
    return {
      restrict: 'E',
      require: '^ngModel'
    };
  });
