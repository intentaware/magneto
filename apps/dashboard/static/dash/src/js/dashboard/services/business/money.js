'use strict';

/**
 * Quick calculation of money
 */

angular.module('adomattic.dashboard')
  .service('Money', function() {
    var self = this;

    /**
     * method to get number of impressions, and the actual charge value.
     * @param  {float} budget           the budget set by the user
     * @param  {int} offer            individual offer to create
     * @param  {float} advertiserRate   advertiser rate, will be individual
     * @param  {float} taxRate          tax rate applicable to advertiser
     * @param  {boolean} inclusiveCharges flag to check if we are to allow to exceed the budget
     * @return {json}                  json {impressions: int, charge: float, serviceCharges: float, taxes: float}
     */
    self.getImpressionCountAndChargeValue = function(budget, offer, advertiserRate, taxRate, inclusiveCharges) {
      var actualBudget = budget;
      var muxFactor = 1 + advertiserRate;

      /**
       * quickly calculates upto 2 decimal places
       * @param  {float} number         the number to round up
       * @return {float}                the returned number
       */
      var toFixed = function (number) {
        return parseFloat(number.toFixed(2));
      };

      if (inclusiveCharges) {
        muxFactor = toFixed(1/muxFactor);
      }

      actualBudget = muxFactor * budget;
      var impressions = Math.round(actualBudget / offer);
      var impressionsTotal = toFixed(impressions * offer);
      var serviceCharges = toFixed(impressionsTotal * advertiserRate);
      var taxes = toFixed((impressionsTotal + serviceCharges) * taxRate);
      var charge = toFixed(impressionsTotal + serviceCharges + taxes);

      return {
        impressions: impressions,
        charge: charge,
        serviceCharges: serviceCharges,
        taxes: taxes
      };
    };
  });
