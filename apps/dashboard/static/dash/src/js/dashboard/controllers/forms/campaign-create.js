'use strict';
/**
 * Created by yousuf on 06/03/2015.
 */

angular.module('adomattic.dashboard')
  .controller('CampaignFormCtrl', function($scope, $rootScope, $location, $mdDialog, urls, Campaign, Circle) {
    var self = this;

    self.circles = [];

    Circle.query().$promise.then(function(data) {
      self.circles = data.map(function(d) {
        d._name = d.name.toLowerCase();
        console.log(d);
        return d;
      });
      console.log(self.circles);
    });

    self.ad = {
      name: undefined,
      description: undefined,
      image: undefined,
      budget: 10,
      coupon_value: 2,
      circles: []
    };

    self.now = new Date();

    // autocomplete chips
    self.selectedItem = null;
    self.searchText = null;
    self.circleLookup = function (query) {
      console.log(query);
      var result = _.filter(self.circles, function(key) {
        return key._name.indexOf(query) > -1 ? true : false;
      });
      console.log(result);
      return result;
    };

    self.saveAd = function() {
      self.$saving = true;
      Campaign.save(self.ad).$promise.then(function(data) {
        console.log(data);
        //$location.path('/campaigns/');
        openStripePaymentDialog(data.invoice);
      }, function(data) {
        console.log(data);
        self.$saving = false;
      });
    };

    self.calculateImpressions = function () {
      return Math.round((self.ad.budget * (1 - $rootScope.globals.company.advertiser_rate))/self.ad.coupon_value) || 0;
    };

    $scope.$watchGroup(['campaignForm.ad.name', 'campaignForm.ad.description', 'campaignForm.ad.image'], function() {
      console.log(self.ad);
      $rootScope.$emit('campaginFormUpdated', self.ad);
    });

    var openStripePaymentDialog = function (invoiceID) {
      $mdDialog.show({
        controller: 'StripeCreditCardDialogCtrl',
        controllerAs: 'creditCard',
        templateUrl: urls.partials.dialogs + 'payments/stripe-credit-card.html',
        locals: {
          invoiceID: invoiceID
        },
        //targetEvent: ev,
        parent: angular.element(document.body)
      });
    };
  });
