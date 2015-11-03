'use strict';

/**
 * Edit controller for campaigns
 */

angular.module('adomattic.dashboard')
  .controller('CampaignEditCtrl', ['$routeParams', 'Campaign', 'Circle', 'Helper', function($routeParams, Campaign, Circle, Helper) {
    var self = this;
    if ($routeParams.hasOwnProperty('campaignID')) {
      Circle.query().$promise.then(function(data) {

        self.circles = data.map(function(d) {
          d._id = String(d.id);
          d._name = d.name.toLowerCase();
          return d;
        });

        Campaign.get({
          id: $routeParams.campaignID
        }).$promise.then(function(response) {
          response.starts_on = new Date(response.starts_on);
          response.ends_on = new Date(response.ends_on);
          response.coupon_value = parseFloat(response.coupon_value);
          response.input_budget = parseFloat(response.budget);

          response.circles = Helper.toObjects(response.circles, self.circles);

          /*
          response.circles = response.circles.map(function(d) {
            var index = _.findIndex(self.circles, function(c) {
              return parseInt(c.id) === parseInt(d);
            });
            console.log(index);
            d = self.circles[index];
            return d;
          });
          */

          self.campaign = response;
          console.log(response);
        });
      });
    }
  }]);
