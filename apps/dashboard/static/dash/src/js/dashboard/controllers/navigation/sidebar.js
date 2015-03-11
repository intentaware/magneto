'use strict';

angular.module('adomattic.dashboard')
  .controller('SidebarNavigationCtrl', function ($scope, $location) {
    $scope.gotoHome = function () {
      $location.path('/');
    };

    $scope.gotoCampaignList = function () {
      $location.path('/campaigns/');
    };

    $scope.goToCampaignCreate = function () {
      $location.path('/campaigns/create/');
    };
  });
