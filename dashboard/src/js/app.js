'use strict';

angular.module('adomattic', [
    // angular core
    'ngAnimate',
    'ngCookies',
    'ngSanitize',
    'ngResource',
    'ngRoute',
    'ngMessages',
    'ngMaterial',
    // 3rd party
    'ngMask',
    'nvd3',
    'zeroclipboard',
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
    // $mdThemingProvider.definePalette('adomattic', {
    //   '0': '#ffffff',
    //   '50': '#fafafa',
    //   '100': '#f5f5f5',
    //   '200': '#eeeeee',
    //   '300': '#e0e0e0',
    //   '400': '#bdbdbd',
    //   '500': '#9e9e9e',
    //   '600': '#757575',
    //   '700': '#616161',
    //   '800': '#424242',
    //   '900': '#212121',
    //   '1000': '#000000',
    //   'A100': '#ffffff',
    //   'A200': '#eeeeee',
    //   'A400': '#bdbdbd',
    //   'A700': '#616161',
    //   'contrastDefaultColor': 'dark',
    //   'contrastLightColors': '600 700 800 900'
    // });
    // $mdThemingProvider.theme('default')
    //   .primaryPalette('adomattic', {
    //     'default': '200'
    //   });
    var customPrimary = {
      '50': '#ffffff',
      '100': '#fefefe',
      '200': '#fdfdfd',
      '300': '#fcfcfc',
      '400': '#fbfbfb',
      '500': '#eeeeee',
      '600': '#e1e1e1',
      '700': '#d4d4d4',
      '800': '#c8c8c8',
      '900': '#bbbbbb',
      'A100': '#fefefe',
      'A200': '#fdfdfd',
      'A400': '#fcfcfc',
      'A700': '#aeaeae'
    };

    $mdThemingProvider
      .definePalette('customPrimary',
        customPrimary);

    var customAccent = {
      '50': '#e7a2a0',
      '100': '#e28d8c',
      '200': '#dd7977',
      '300': '#d86563',
      '400': '#d3514e',
      '500': '#CE3D3A',
      '600': '#bf3230',
      '700': '#ab2d2a',
      '800': '#962825',
      '900': '#822220',
      'A100': '#ecb6b5',
      'A200': '#f2cac9',
      'A400': '#f7dedd',
      'A700': '#6d1d1b'
    };
    $mdThemingProvider
      .definePalette('customAccent',
        customAccent);

    var customWarn = {
      '50': '#ffd280',
      '100': '#ffc966',
      '200': '#ffc04d',
      '300': '#ffb733',
      '400': '#ffae1a',
      '500': '#ffa500',
      '600': '#e69500',
      '700': '#cc8400',
      '800': '#b37300',
      '900': '#996300',
      'A100': '#ffdb99',
      'A200': '#ffe4b3',
      'A400': '#ffedcc',
      'A700': '#805300'
    };
    $mdThemingProvider
      .definePalette('customWarn',
        customWarn);

    var customBackground = {
      '50': '#ffffff',
      '100': '#ffffff',
      '200': '#ffffff',
      '300': '#ffffff',
      '400': '#fdfdfd',
      '500': '#f0f0f0',
      '600': '#e3e3e3',
      '700': '#d6d6d6',
      '800': '#cacaca',
      '900': '#bdbdbd',
      'A100': '#ffffff',
      'A200': '#ffffff',
      'A400': '#ffffff',
      'A700': '#b0b0b0'
    };
    $mdThemingProvider
      .definePalette('customBackground',
        customBackground);

    $mdThemingProvider.theme('default')
      .primaryPalette('customPrimary')
      .accentPalette('customAccent')
      .warnPalette('customWarn')
      .backgroundPalette('customBackground');
  })
  .config(function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'routes/landing/main.html'
      })
      // campaigns
      .when('/campaigns/', {
        templateUrl: 'routes/campaigns/list.html',
        controller: 'CampaignListCtrl',
        controllerAs: 'campaignsList'
      })
      .when('/campaigns/past/', {
        templateUrl: 'routes/campaigns/list.html',
        controller: 'CampaignListCtrl',
        controllerAs: 'campaignsList'
      })
      .when('/campaigns/create/', {
        templateUrl: 'routes/campaigns/create.html',
        controller: 'CampaignCreateCtrl',
        controllerAs: 'baseCampaignFormCtrl'
      })
      .when('/campaigns/:campaignID/edit/', {
        templateUrl: 'routes/campaigns/edit.html',
        controller: 'CampaignEditCtrl',
        controllerAs: 'baseCampaignFormCtrl'
      })
      // assets
      .when('/assets/', {
        templateUrl: 'routes/assets/list.html',
        controller: 'AssetListCtrl',
        controllerAs: 'pc'
      })
      .when('/assets/create/', {
        templateUrl: 'routes/assets/create.html',
        controller: 'AssetCreateCtrl',
        controllerAs: 'pc'
      })
      // settings
      .when('/settings/', {
        templateUrl: 'routes/settings/main.html',
      })
      // invoices
      .when('/invoices/', {
        templateUrl: 'routes/invoices/list.html',
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
  })
  .config(function(uiZeroclipConfigProvider) {
    uiZeroclipConfigProvider.setOverrideConfig(false);
  });
