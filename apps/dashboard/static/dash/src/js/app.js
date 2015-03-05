'use strict';

angular.module('adomattic', [
  'ngAnimate',
  'ngCookies',
  'ngTouch',
  'ngSanitize',
  'ngResource',
  'ngRoute',
  'ngMaterial',
  'adomattic.dashboard'
])
  .constant('urls', {
    templateBaseUrl: '/partials/dashboard/',
    apiBaseUrl: '/api/'
  })
  .config(function ($mdThemingProvider) {
    $mdThemingProvider.theme('dark')
      .primaryPalette('red')
      .accentPalette('orange');

  })
  .config(function ($routeProvider, urls) {
    $routeProvider.when('/', {
      templateUrl: urls + 'home.js',
      controller: 'DashboardHome'
    });
  })
  .config(function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
  })
  .config(function ($httpProvider) {
    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  });

