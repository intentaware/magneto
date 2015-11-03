'use strict';
/**
 * Created by yousuf on 06/03/2015.
 */

angular.module('adomattic.dashboard')
  .controller('CampaignFormCtrl', ['$scope', '$rootScope', '$location', '$mdDialog', 'urls', 'Campaign', 'Circle', 'Money', 'Helper', function($scope, $rootScope, $location, $mdDialog, urls, Campaign, Circle, Money, Helper) {
    var self = this;

    // md-autocomplete settings
    self.getMatches = function (query, lookup) {
      var results = query ? lookup.filter(createFilterFor(query)) : [];
      //console.log(results);
      console.log(self.campaign);
      return results;
    };

    var createFilterFor = function (query) {
      var _q = isNaN(parseInt(query)) ? query.toLowerCase() : parseInt(query);
      //console.log(_q);
      return function(index) {
        //console.log(index.id);
        return (index._name.indexOf(_q) === 0) || (index.id === _q);
      };
    };

    self.now = new Date();

    self.getImpressionCount = function() {
      if (self.campaign) {
        self.money = Money.getImpressionCountAndChargeValue(
          self.campaign.input_budget, self.campaign.coupon_value, $rootScope.globals.company.advertiser_rate, 0.25, true
        );
      } else {
        self.money = 0;
      }
      return self.money;
    };

    self.isDisabled = function() {
      return (self.campaign && self.campaign.id) ? true : false;
    };

    self.saveAd = function() {
      self.$saving = true;
      self.campaign.budget = self.money.charge;
      self.campaign.service_charges = self.money.serviceCharges;
      self.campaign.taxes = self.money.taxes;
      self.campaign.coupon_count = self.money.impressions;
      self.campaign.circles = Helper.toIDs(self.campaign.circles);
      console.log(self.campaign);
      if (!self.campaign.id) {
        Campaign.save(self.campaign).$promise.then(function(data) {
          console.log(data);
          //$location.path('/campaigns/');
          openStripePaymentDialog(data.invoice);
        }, function(data) {
          console.log(data);
          self.$saving = false;
        });
      } else {
        Campaign.update(self.campaign).$promise.then(function() {
          $location.path('/campaigns/');
        }, function() {
          self.$saving = false;
        });
      }
    };

    //this watches changes on the main controller
    $scope.$watchGroup(['campaignForm.ad.name', 'campaignForm.ad.description', 'campaignForm.ad.image'], function() {
      //console.log(self.campaign);
      $rootScope.$emit('campaginFormUpdated', self.campaign);
    });

    // initializing the main controller
    $scope.$watch('baseCampaignFormCtrl.campaign', function(n) {
      self.campaign = n;
    });

    $scope.$watch('baseCampaignFormCtrl.circles', function(n) {
      console.log(n);
      self.circles = n;
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
  }]);
