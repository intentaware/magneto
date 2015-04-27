'use strict';
/**
 * Created by yousuf on 06/03/2015.
 */

angular.module('adomattic.dashboard')
  .controller('CampaignFormCtrl', function($scope, $rootScope, $location, Campaign) {
    var self = this;

    self.ad = {
      name: undefined,
      description: undefined,
      image: undefined,
      budget: 10,
      coupon_value: 2
    };

    self.saveAd = function() {
      self.$saving = true;
      Campaign.save(self.ad).$promise.then(function(data) {
        console.log(data);
        $location.path('/campaigns/');
      }, function(data) {
        console.log(data);
        self.$saving = false;
      });
    };

    self.calculateImpressions = function () {
      return Math.round((self.ad.budget * (1 - $rootScope.globals.company.advertiser_rate))/self.ad.coupon_value) || 0;
    };

    $scope.$watchGroup(['campaignForm.ad.name', 'campaignForm.ad.description', 'campaignForm.ad.image'], function() {
      $rootScope.$emit('campaginFormUpdated', self.ad);
    });
  });
