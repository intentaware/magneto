'use strict';

angular.module('adomattic.dashboard')
  .controller('HomeCtrl', function($scope, $location, Campaign) {
    var getCampaigns = function () {
      Campaign.query().$promise.then(function(data) {
        $scope.campaigns = data;
      });
    };

    $scope.gotoCampaignList = function () {
      $location.path('/campaigns/');
    };

    getCampaigns();
  });
