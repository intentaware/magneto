'use strict';

angular.module('adomattic.dashboard')
  .controller('SidebarNavigationCtrl', ['$scope', '$location', function($scope, $location) {
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
  }]);
