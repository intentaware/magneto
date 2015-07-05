'use strict';
/**
 * Created by yousuf on 06/03/2015.
 */

angular.module('adomattic.dashboard')
  .controller('CampaignFormCtrl', function($scope, $rootScope, $location, $mdDialog, urls, Campaign, Money) {
    var self = this;

    //self.circles = [];

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

   // initializing the main controller
    $scope.$watch('baseCampaignFormCtrl.campaign', function(n) {
      self.campaign = n;
    });

    console.log(self);
    console.log($scope);

    self.now = new Date();

    self.getImpressionCount = function() {
      self.money = Money.getImpressionCountAndChargeValue(
        self.campaign.input_budget, self.campaign.coupon_value, $rootScope.globals.company.advertiser_rate, 0.25, true
      );
      return self.money;
    };

    self.saveAd = function() {
      self.$saving = true;
      self.campaign.budget = self.money.charge;
      self.campaign.service_charges = self.money.serviceCharges;
      self.campaign.taxes = self.money.taxes;
      self.campaign.coupon_count = self.money.impressions;
      Campaign.save(self.campaign).$promise.then(function(data) {
        console.log(data);
        //$location.path('/campaigns/');
        openStripePaymentDialog(data.invoice);
      }, function(data) {
        console.log(data);
        self.$saving = false;
      });
    };

    $scope.$watchGroup(['campaignForm.ad.name', 'campaignForm.ad.description', 'campaignForm.ad.image'], function() {
      //console.log(self.campaign);
      $rootScope.$emit('campaginFormUpdated', self.campaign);
    });

    var openStripePaymentDialog = function(invoiceID) {
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
        $location.path('/campaigns/');
      });
    };
  });
