'use strict';

angular.module('adomattic.dashboard')
  .controller('HeaderNavigationCtrl', ['$scope', '$mdSidenav', function($scope, $mdSidenav) {
    $scope.openLeftMenu = function() {
      $mdSidenav('left').toggle();
    };
  }]);
