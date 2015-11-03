'use strict';
/**
 * Individual Campaign Code
 */

angular.module('adomattic.dashboard')
  .controller('CampaignIndividualIncludeCodeDialogCtrl', ['$mdDialog', '$rootScope', 'campaignID', function($mdDialog, $rootScope, campaignID) {
    var self = this;
    self.campaignID = campaignID;

    self.hide = function() {
      $mdDialog.hide();
    };

    self.assetRoot = (window.location.hostname === 'app.intentaware.com') ? 'http://app.intentaware.com/magneto/' : 'http://' + window.location.host + '/static/impressions/dist/';
    self.globals = $rootScope.globals;
  }]);
