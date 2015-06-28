'use strict';

angular.module('adomattic.dashboard')
  .controller('PublisherLandingCtrl', function($scope) {
    $scope.assetRoot = (window.location.hostname === 'app.adomattic.com') ? 'http://app.adomattic.com/magneto/' : 'http://' + window.location.host + '/static/impressions/dist/';
  });
