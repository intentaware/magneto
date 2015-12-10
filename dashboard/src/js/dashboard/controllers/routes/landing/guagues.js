'use strict';

angular.module('adomattic.dashboard')
  .controller('GuagesLandingCtrl', function(Asset, $location) {
    var self = this;

    Asset.query().$promise.then(function(r){
      self.assets = r;
    });

    self.goToAssetCreate = function() {
      $location.path('/assets/create/');
    };

    self.goToAssetList = function() {
      $location.path('/assets/');
    };
  });
