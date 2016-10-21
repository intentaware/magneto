'use strict';

angular.module('adomattic.dashboard')
  .controller('GuagesLandingCtrl', function(Asset, Reporter, $location) {
    var self = this;

    var urlParamsReports = {
      app: 'guages',
      endPoint: 'assets'
    };

    self.activeAsset = null;

    self.getAssetReport = function(id) {
      var params = urlParamsReports;

      params.id = id;
      Reporter.useragents(params).$promise.then(function(d) {
        self.useragents = d;
      });

      Reporter.history(params).$promise.then(function(d) {
        self.history = [{
          key: 'History',
          values: d
        }];
      });
    };

    self.init = function() {
      Asset.query().$promise.then(function(r) {
        self.assets = r;

        if (self.assets.length) {
          self.activeAsset = self.assets[0].id;
          self.getAssetReport(self.activeAsset);
        }
      });
    };

    self.init();

    self.gotoAssetReport = function(id) {
      $location.path('/assets/' + id + '/report/');
    };

    // Asset.query().$promise.then(function(r) {
    //   self.assets = r;
    // });

    self.goToAssetCreate = function() {
      $location.path('/assets/create/');
    };

    self.goToAssetList = function() {
      $location.path('/assets/');
    };
  });
