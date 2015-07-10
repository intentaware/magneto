'use strict';
/**
 * Individual Campaign Code
 */

angular.module('adomattic.dashboard')
  .controller('CampaignIndividualIncludeCodeDialogCtrl', function ($mdDialog, $rootScope, campaignID) {
    var self = this;
    self.campaignID = campaignID;

    self.hide = function () {
      $mdDialog.hide();
    };

    self.assetRoot = (window.location.hostname === 'app.adomattic.com') ? 'http://app.adomattic.com/magneto/' : 'http://' + window.location.host + '/static/impressions/dist/';
    self.globals = $rootScope.globals;
  });
