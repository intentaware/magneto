'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignCreateCtrl', function($rootScope, Circle) {
    var self = this;

    Circle.query().$promise.then(function(data) {

      self.circles = data.map(function(d) {
        d._id = String(d.id);
        d._name = d.name.toLowerCase();
        return d;
      });

      self.campaign = {
        name: undefined,
        description: undefined,
        image: undefined,
        input_budget: 10,
        coupon_value: 2,
        circles: []
      };
    });

    $rootScope.$on('campaginFormUpdated', function(e, args) {
      self.campaign = args;
    });
  });
