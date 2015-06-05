'use strict';
/**
 * Created by yousuf on 06/03/2015.
 */

angular.module('adomattic.dashboard')
  .controller('CampaignFormCtrl', function($scope, $rootScope, $location, $mdDialog, urls, Campaign, Money) {
    var self = this;

    self.circles = [];

    /*
    Circle.query().$promise.then(function(data) {
      self.circles = data.map(function(d) {
        d._name = d.name.toLowerCase();
        console.log(d);
        return d;
      });
      console.log(self.circles);
    });
    */

    self.ad = {
      name: undefined,
      description: undefined,
      image: undefined,
      budget: 10,
      coupon_value: 2,
      circles: []
    };

    console.log($rootScope);

    self.now = new Date();

    self.getImpressionCount = function() {
      return Money.getImpressionCountAndChargeValue(
          self.ad.budget, self.ad.coupon_value, $rootScope.globals.company.advertiser_rate, 0.25, true
        );
    };

    self.saveAd = function() {
      self.$saving = true;
      Campaign.save(self.ad).$promise.then(function(data) {
        console.log(data);
        //$location.path('/campaigns/');
        openStripePaymentDialog(data.invoice, self.ad.budget);
      }, function(data) {
        console.log(data);
        self.$saving = false;
      });
    };

    /*
    self.calculateImpressions = function () {
      return Math.round((self.ad.budget * (1 - $rootScope.globals.company.advertiser_rate))/self.ad.coupon_value) || 0;
    };
    */

    $scope.$watchGroup(['campaignForm.ad.name', 'campaignForm.ad.description', 'campaignForm.ad.image'], function() {
      //console.log(self.ad);
      $rootScope.$emit('campaginFormUpdated', self.ad);
    });

    var openStripePaymentDialog = function (invoiceID, amount) {
      $mdDialog.show({
        controller: 'StripeCreditCardDialogCtrl',
        controllerAs: 'creditCard',
        templateUrl: urls.partials.dialogs + 'payments/stripe-credit-card.html',
        locals: {
          invoiceID: invoiceID,
          amount: amount
        },
        //targetEvent: ev,
        parent: angular.element(document.body)
      }).then(function() {
        $location.path('/campaigns/');
      });
    };
  });
