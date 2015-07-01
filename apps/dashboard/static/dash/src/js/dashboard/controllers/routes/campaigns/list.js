'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignListCtrl', function($scope, $mdDialog, urls, Campaign) {
    $scope.campaigns = Campaign.query();

    $scope.showPreview = function(ev, data) {
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

    $scope.openStripePaymentDialog = function(invoiceID) {
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
        $scope.campaigns = Campaign.query();
      });
    };
  });
