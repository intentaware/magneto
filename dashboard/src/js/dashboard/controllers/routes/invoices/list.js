'use strict';

angular.module('adomattic.dashboard')
  .controller('InvoiceListCtrl', function (Invoice) {
    var self = this;
    Invoice.query(function (data) {
      console.log(data);
      self.invoices = data;
    });
  });
