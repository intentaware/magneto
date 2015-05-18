'use strict';

angular.module('adomattic.dashboard')
  .controller('StripeCreditCardDialogCtrl', function($mdDialog, invoiceID) {
    var self = this;
    self.invoice = invoiceID;
  });
