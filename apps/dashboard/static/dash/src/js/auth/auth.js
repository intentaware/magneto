'use strict';

angular.module('auth', ['ngMaterial', 'ngMessages'])
  .config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('blue')
      .accentPalette('orange');
  })
  .controller('AuthCtrl', function() {
  });

