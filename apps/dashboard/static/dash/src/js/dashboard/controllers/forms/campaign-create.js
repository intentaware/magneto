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
      image: undefined
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

    $scope.$watchGroup(['campaignForm.ad.name', 'campaignForm.ad.description', 'campaignForm.ad.image'], function() {
      $rootScope.$emit('campaginFormUpdated', self.ad);
    });
  });
