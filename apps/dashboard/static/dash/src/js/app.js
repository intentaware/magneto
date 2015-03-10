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
    partials: {
      routes: '/dashboard/partials/routes/',
      directives: '/dashboard/partials/directives/',
      dialogs: '/dashboard/partials/dialogs/'
    },
    apiBaseUrl: '/api/'
  })
  .config(function ($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('red')
      .accentPalette('orange');

  })
  .config(function ($routeProvider, urls) {
    $routeProvider.when('/', {
      templateUrl: urls.partials.routes + 'home.html',
      controller: 'HomeCtrl'
    })
      .when('/campaigns/', {
        templateUrl: urls.partials.routes + 'ads/list.html',
        controller: 'CampaignListCtrl'
      })
      .when('/campaigns/create/', {
        templateUrl: urls.partials.routes + 'ads/create.html'
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

