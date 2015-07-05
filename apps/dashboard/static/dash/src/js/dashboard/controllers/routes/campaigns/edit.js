'use strict';

/**
 * Edit controller for campaigns
 */

angular.module('adomattic.dashboard')
  .controller('CampaignEditCtrl', function($routeParams, Campaign) {
    var self = this;
    if ($routeParams.hasOwnProperty('campaignID')) {
      Campaign.get({
        id: $routeParams.campaignID
      }).$promise.then(function(response) {
        response.starts_on = new Date(response.starts_on);
        response.ends_on = new Date(response.ends_on);
        response.coupon_value = parseFloat(response.coupon_value);
        response.input_budget = parseFloat(response.budget);
        self.campaign = response;
      });
    }
  });
