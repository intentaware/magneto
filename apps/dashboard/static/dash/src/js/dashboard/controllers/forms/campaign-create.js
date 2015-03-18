'use strict';
/**
 * Created by yousuf on 06/03/2015.
 */

angular.module('adomattic.dashboard')
  .controller('CampaignFormCtrl', function($scope, $location, Campaign) {
    console.log($scope);


    $scope.saveAd = function() {
      Campaign.save($scope.ad).$promise.then(function(data) {
        console.log(data);
        $location.path('/campaigns/');
      });
    };
  });
