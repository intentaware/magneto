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
        self.campaign = response;
      });
    }
  });
