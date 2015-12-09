'use strict';

angular.module('adomattic.dashboard')
  .controller('AssetListCtrl', function(Asset, Helper, $mdToast) {
    var self = this;

    Asset.query().$promise.then(function(response) {
      self.assets = response;
    });

    self.showCode = function(index) {

      self.assets.map(function(a) {
        a.show_code = false;
      });

      self.assets[index].show_code = true;
      self.setActivePixel(self.assets[index]);
    };

    self.setActivePixel = function(asset) {
      self.pixel = Helper.getGuagePixel(asset.key);
    };

    self.showCopied = function() {
      $mdToast.show(
        $mdToast.simple()
        .content('Copied, Paste it anywhere inside <body></body> tag to know more about your website.')
        .position('right bottom')
      );
    };

  });
