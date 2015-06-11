'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignersLandingCtrl', function($rootScope, $scope, $location, Campaign) {
    var getCampaigns = function() {
      Campaign.query().$promise.then(function(data) {
        $scope.campaigns = data;
      });
    };

    $scope.gotoCampaignList = function() {
      $location.path('/campaigns/');
    };

    getCampaigns();

    $scope.options = {
      chart: {
        type: 'pieChart',
        height: '300',
        donut: true,
        x: function(d) {
          return d.key;
        },
        y: function(d) {
          return d.y;
        },
        //showLabels: true,
        transitionDuration: 500,
        labelThreshold: 0.01,
      }
    };

    $scope.data = [{
      key: 'Return on Investment',
      y: $rootScope.globals.coupons.claimed
    }, {
      key: 'Carry Over',
      y: $rootScope.globals.coupons.remaining
    }];
  });
