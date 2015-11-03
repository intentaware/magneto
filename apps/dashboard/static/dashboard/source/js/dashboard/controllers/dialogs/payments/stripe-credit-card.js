'use strict';

angular.module('adomattic.dashboard')
  .controller('StripeCreditCardDialogCtrl', ['$mdDialog', '$mdToast', 'Invoice', 'invoiceID', function($mdDialog, $mdToast, Invoice, invoiceID) {
    var self = this;
    self.invoice = {};

    Invoice.get({
      id: invoiceID
    }).$promise.then(function(response) {
      console.log(response);
      self.invoice = response;
    });

    self.creditCard = {
      id: invoiceID,
      description: 'Invoice ID: ' + String(invoiceID)
    };

    self.chargeCard = function() {
      self.creditCard.amount = self.invoice.amount;
      Invoice.charge(self.creditCard).$promise.then(function() {
        $mdToast.show(
          $mdToast.simple()
          .content('Campaign Activated')
          .position('top right')
          .hideDelay(3000)
        );
        $mdDialog.hide();
      });
    };

    self.chargeLater = function() {
      $mdDialog.hide();
    };
  }]);
