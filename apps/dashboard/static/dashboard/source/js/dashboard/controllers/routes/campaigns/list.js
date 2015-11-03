'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignListCtrl', ['$mdDialog', '$location', '$routeParams', 'urls', 'Campaign', function($mdDialog, $location, $routeParams, urls, Campaign) {
    var self = this;

    var path = window.location.href;


    if (path.indexOf('path') > -1) {
      console.log(path.indexOf('path'));
      self.campaigns = Campaign.past();
      self.title = 'Past';
    } else {
      self.campaigns = Campaign.query();
      self.title = 'Current';
    }


    self.showPreview = function(ev, data) {
      $mdDialog.show({
        controller: 'CampaignPreviewDialogCtrl',
        controllerAs: 'previewController',
        templateUrl: urls.partials.dialogs + 'campaigns/preview.html',
        locals: {
          data: data
        },
        targetEvent: ev,
        parent: angular.element(document.body)
      });
    };

    self.openStripePaymentDialog = function(invoiceID) {
      $mdDialog.show({
        controller: 'StripeCreditCardDialogCtrl',
        controllerAs: 'creditCard',
        templateUrl: urls.partials.dialogs + 'payments/stripe-credit-card.html',
        locals: {
          invoiceID: invoiceID
        },
        //targetEvent: ev,
        parent: angular.element(document.body)
      }).then(function() {
        self.campaigns = Campaign.query();
      });
    };

    self.openIndivdualCampaignCodeDialog = function(campaignID) {
      $mdDialog.show({
        controller: 'CampaignIndividualIncludeCodeDialogCtrl',
        controllerAs: 'offerCode',
        templateUrl: urls.partials.dialogs + 'campaigns/indivdual-campaign-code.html',
        locals: {
          campaignID: campaignID
        },
        parent: angular.element(document.body)
      }).then(function() {
        self.campaigns = Campaign.query();
      });
    };

    self.editCampaign = function(campaignID) {
      var p = '/campaigns/' + campaignID + '/edit/';
      console.log(p);
      $location.path(p);
    };
  }]);
