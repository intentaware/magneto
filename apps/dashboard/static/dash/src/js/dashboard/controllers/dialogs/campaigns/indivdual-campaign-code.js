'use strict';
/**
 * Individual Campaign Code
 */

angular.module('adomattic.dashboard')
  .controller('CampaignIndividualIncludeCodeDialogCtrl', function ($mdDialog, campaignID) {
    var self = this;
    self.campaignID = campaignID;

    self.hide = function () {
      $mdDialog.hide();
    };
  });
