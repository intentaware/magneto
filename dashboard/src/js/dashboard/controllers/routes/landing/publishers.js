'use strict';

angular.module('adomattic.dashboard')
  .controller('PublisherLandingCtrl', function ($scope, $rootScope, Helper, $mdToast) {
    // $scope.assetRoot = (window.location.hostname === 'app.intentaware.com') ? 'http://app.intentaware.com/magneto/' : 'http://' + window.location.host + '/static/impressions/dist/';

    $scope.pixel = Helper.getPixel($rootScope.globals.company.publisher_key);
    $scope.helpText = {
      forPixel: true
    };
    $scope.showCopied = function () {
      $mdToast.show(
        $mdToast.simple()
          .content('Copied, Now Paste it in your source and get cracking')
          .position('right bottom')
      );
    };
  });
