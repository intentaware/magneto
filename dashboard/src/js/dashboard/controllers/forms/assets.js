'use strict';

angular.module('adomattic.dashboard')
  .controller('AssetFormCtrl', function(Asset, $location) {
    var self = this;

    self.saveAsset = function() {
      Asset.save(self.asset).$promise.then(function() {
        $location.path('/assets/');
      });
    };
  });
