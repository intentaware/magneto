'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignPreviewDialogCtrl', function ($mdDialog, data) {
    console.log('dialog');
    console.log(data);

    var self = this;

    self.data = data;

    self.hide = function () {
      $mdDialog.hide();
    };
  });
