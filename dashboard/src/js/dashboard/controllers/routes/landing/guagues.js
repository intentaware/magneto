'use strict';

angular.module('adomattic.dashboard')
  .controller('GuagesLandingCtrl', function(Asset) {
    var self = this;
    Asset.query().$promise.then(function(r){
      self.assets = r;
      console.log(r);
    });
  });
