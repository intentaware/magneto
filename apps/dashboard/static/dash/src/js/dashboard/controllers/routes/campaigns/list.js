'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignListCtrl', function($scope, Ad) {
    $scope.ads = Ad.query();
  });
