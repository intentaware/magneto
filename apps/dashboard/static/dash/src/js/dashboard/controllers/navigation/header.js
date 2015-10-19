'use strict';

angular.module('adomattic.dashboard')
  .controller('HeaderNavigationCtrl', function($scope, $mdSidenav) {
    $scope.openLeftMenu = function() {
      $mdSidenav('left').toggle();
    };
  });
