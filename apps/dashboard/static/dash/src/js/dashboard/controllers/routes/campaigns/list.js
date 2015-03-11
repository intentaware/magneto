'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignListCtrl', function($scope, Campaign) {
    $scope.campaigns = Campaign.query();
  });
