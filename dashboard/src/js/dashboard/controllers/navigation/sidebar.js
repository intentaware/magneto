'use strict';

angular.module('adomattic.dashboard')
  .controller('SidebarNavigationCtrl', function($scope, $location) {
    $scope.gotoHome = function() {
      $location.path('/');
    };

    $scope.gotoCampaignList = function(level) {
      level ? $location.path('/campaigns/' + level + '/') : $location.path('/campaigns/');
    };

    $scope.goToCampaignCreate = function() {
      $location.path('/campaigns/create/');
    };

    $scope.goToSettings = function() {
      $location.path('/settings/');
    };

    $scope.goToInvoices = function() {
      $location.path('/invoices/');
    };

    $scope.goToAssetCreate = function() {
      $location.path('/assets/create/');
    };

    $scope.goToAssetList = function() {
      $location.path('/assets/');
    };
  });
