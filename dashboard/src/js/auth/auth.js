'use strict';

angular.module('auth', ['ngMaterial', 'ngMessages'])
  .config(function($mdThemingProvider) {
    $mdThemingProvider.definePalette('adomattic', {
      '0': '#ffffff',
      '50': '#fafafa',
      '100': '#f5f5f5',
      '200': '#eeeeee',
      '300': '#e0e0e0',
      '400': '#bdbdbd',
      '500': '#9e9e9e',
      '600': '#757575',
      '700': '#616161',
      '800': '#424242',
      '900': '#212121',
      '1000': '#000000',
      'A100': '#ffffff',
      'A200': '#eeeeee',
      'A400': '#bdbdbd',
      'A700': '#616161',
      'contrastDefaultColor': 'dark',
      'contrastLightColors': '600 700 800 900'
    });
    $mdThemingProvider.theme('default')
      .primaryPalette('adomattic', {
        'default': '200'
      });
  })
  .controller('AuthCtrl', function() {
  })
  .controller('FormCtrl', function() {
  });
