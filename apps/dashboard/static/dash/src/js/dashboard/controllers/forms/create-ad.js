'use strict';
/**
 * Created by yousuf on 06/03/2015.
 */

angular.module('adomattic.dashboard')
  .controller('CreateAdFormCtrl', function($scope, Ad) {
    console.log('i am the form');
    console.log($scope);


    $scope.saveAd = function() {
      Ad.save($scope.ad).$promise.then(function(data) {
        console.log(data);
      });
    };
  });
