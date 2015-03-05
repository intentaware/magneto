'use strict';

angular.module('auth', ['ngMaterial', 'ngMessages'])
  .config(function($mdThemingProvider) {
    $mdThemingProvider.theme('dark')
      .primaryPalette('red')
      .accentPalette('orange');
  })
  .controller('AuthCtrl', function() {
  })
  .controller('FormCtrl', function() {
  });

