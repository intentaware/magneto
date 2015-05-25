'use strict';

angular.module('adomattic.dashboard')
  .controller('StripeCreditCardDialogCtrl', function($mdDialog, Invoice, invoiceID, amount) {
    var self = this;
    /*
    self.creditCard = {
      id: invoiceID,
      amount: '32.56',
      number: '4242424242424242',
      exp_month: 10,
      exp_year: 18,
      cvc: 561,
      description: 'Invoice ID: ' + String(invoiceID)
    };*/
    self.creditCard = {
      id: invoiceID,
      description: 'Invoice ID: ' + String(invoiceID),
      amount: amount
    };

    self.chargeCard = function() {
      Invoice.charge(self.creditCard).$promise.then(function() {
        $mdDialog.hide();
      });
    };

    self.chargeLater = function() {
      $mdDialog.hide();
    };
  });
