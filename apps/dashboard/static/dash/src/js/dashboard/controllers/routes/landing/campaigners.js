'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignersLandingCtrl', function($rootScope, $scope, $location, Campaign, City) {
    var getCampaigns = function() {
      Campaign.query().$promise.then(function(data) {
        $scope.campaigns = data;
      });
    };

    $scope.gotoCampaignList = function() {
      $location.path('/campaigns/');
    };

    City.search('mul').then(function(data) {
      console.log('Initial Query');
      console.log(data);
    }, function(error) {
      console.log(error);
    });

    City.search('mult').then(function(data) {
      console.log('Secondary Query');
      console.log(data);
    });

    City.search('new').then(function(data) {
      console.log('this is the third query and should cancel the 2nd one');
      console.log(data);
    });

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
      y: $rootScope.globals.coupons.claimed || 0
    }, {
      key: 'Carry Over',
      y: $rootScope.globals.coupons.remaining || 0
    }];
  });
