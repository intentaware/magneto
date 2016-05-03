'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignersLandingCtrl', function($rootScope, $scope, $location, Campaign, Reporter) {

    var init = function() {
      Campaign.query().$promise.then(function(data) {
        $scope.campaigns = data;
        if (data.length) {
          Reporter.useragents({
            id: data[0].id
          }).$promise.then(function(d) {
            console.info(d);
          });
        }
      });
    };

    $scope.gotoCampaignList = function() {
      $location.path('/campaigns/');
    };

    init();
  });
