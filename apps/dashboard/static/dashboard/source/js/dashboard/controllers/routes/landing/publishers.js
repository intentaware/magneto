'use strict';

angular.module('adomattic.dashboard')
  .controller('PublisherLandingCtrl', ['$scope', function($scope) {
    $scope.assetRoot = (window.location.hostname === 'app.intentaware.com') ? 'http://app.intentaware.com/magneto/' : 'http://' + window.location.host + '/static/impressions/dist/';
  }]);
