'use strict';

angular.module('adomattic.dashboard')
  .controller('DashboardAdList', function($scope, Ad) {
    $scope.ads = Ad.query();
  });
