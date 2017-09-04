'use strict';
/**
 * Individual Campaign Code
 */

angular.module('adomattic.dashboard')
  .controller('CampaignIndividualIncludeCodeDialogCtrl', function ($mdDialog, $mdToast, $rootScope, Helper, campaignID) {
    var self = this;
    self.campaignID = campaignID;

    self.hide = function () {
      $mdDialog.hide();
    };

    self.pixel = Helper.getPixel($rootScope.globals.company.publisher_key, campaignID);
    self.helpText = {
      forPixel: true
    };

    self.showCopied = function () {
      $mdToast.show(
        $mdToast.simple()
          .content('Copied, Now Paste it in your source and get cracking')
          .position('right bottom')
      );
      $mdDialog.hide();
    };
  });
