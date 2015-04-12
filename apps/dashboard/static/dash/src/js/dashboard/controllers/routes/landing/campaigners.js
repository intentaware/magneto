'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignersLandingCtrl', function($scope, $location, Campaign) {
    console.log('The advertiser has landed');
    var getCampaigns = function() {
      Campaign.query().$promise.then(function(data) {
        $scope.campaigns = data;
      });
    };

    $scope.gotoCampaignList = function() {
      $location.path('/campaigns/');
    };

    getCampaigns();
  });
