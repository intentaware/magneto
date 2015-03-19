/**
 * Created by yousuf on 02/03/2015.
 */

'use strict';

angular.module('adomattic.dashboard', [])
  .config(function ($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('grey')
      .accentPalette('orange');

  });
