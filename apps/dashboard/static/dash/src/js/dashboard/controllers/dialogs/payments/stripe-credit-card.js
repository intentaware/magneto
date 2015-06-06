'use strict';

angular.module('adomattic.dashboard')
  .controller('StripeCreditCardDialogCtrl', function($mdDialog, Invoice, invoiceID) {
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
        $mdDialog.hide();
      });
    };

    self.chargeLater = function() {
      $mdDialog.hide();
    };
  });
