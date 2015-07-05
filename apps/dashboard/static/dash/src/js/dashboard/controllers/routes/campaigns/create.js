'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignCreateCtrl', function($rootScope) {
    var self = this;

    self.campaign = {
      name: undefined,
      description: undefined,
      image: undefined,
      input_budget: 10,
      coupon_value: 2,
      circles: []
    };

    $rootScope.$on('campaginFormUpdated', function(e, args) {
      self.campaign = args;
    });
  });
