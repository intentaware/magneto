'use strict';

angular.module('adomattic', [
    // angular core
    'ngAnimate',
    'ngCookies',
    'ngTouch',
    'ngSanitize',
    'ngResource',
    'ngRoute',
    'ngMessages',
    'ngMaterial',
    // 3rd party
    'ngMask',
    'nvd3',
    // adomattic
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
  .config(function($routeProvider, urls) {
    $routeProvider
      .when('/', {
        templateUrl: urls.partials.routes + 'landing/__base.html',
      })
      // campaigns
      .when('/campaigns/', {
        templateUrl: urls.partials.routes + 'campaigns/list.html',
        controller: 'CampaignListCtrl',
        controllerAs: 'campaignsList'
      })
      .when('/campaigns/create/', {
        templateUrl: urls.partials.routes + 'campaigns/create.html',
        controller: 'CampaignCreateCtrl',
        controllerAs: 'baseCampaignFormCtrl'
      })
      .when('/campaigns/:campaignID/edit/', {
        templateUrl: urls.partials.routes + 'campaigns/edit.html',
        controller: 'CampaignEditCtrl',
        controllerAs: 'baseCampaignFormCtrl'
      })
      // settings
      .when('/settings/', {
        templateUrl: urls.partials.routes + 'settings/__base.html',
      })
      // invoices
      .when('/invoices/', {
        templateUrl: urls.partials.routes + 'invoices/list.html',
        controller: 'InvoiceListCtrl',
        controllerAs: 'invoiceList'
      })
      .otherwise('/');
  })
  .config(function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
  })
  .config(function($httpProvider) {
    //$httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  });

// pace.js options
