'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignersLandingCtrl', function($rootScope, $scope, $location, Campaign) {
    var getCampaigns = function() {
      Campaign.query().$promise.then(function(data) {
        $scope.campaigns = data;
      });
    };

    $scope.gotoCampaignList = function() {
      $location.path('/campaigns/');
    };

    getCampaigns();

    // $scope.options = {
    //   chart: {
    //     type: 'pieChart',
    //     height: '300',
    //     donut: true,
    //     x: function(d) {
    //       return d.key;
    //     },
    //     y: function(d) {
    //       return d.y;
    //     },
    //     //showLabels: true,
    //     transitionDuration: 500,
    //     labelThreshold: 0.01,
    //   }
    // };

    // $scope.data = [{
    //   key: 'Return on Investment',
    //   y: $rootScope.globals.coupons.claimed || 0
    // }, {
    //   key: 'Carry Over',
    //   y: $rootScope.globals.coupons.remaining || 0
    // }];

    $scope.impressionData = null;

    Campaign.impressions({
      id: 55
    }).$promise.then(function(data) {
      data.map(function(d) {
        d._added_day = moment(d.added_on).format('DD-MMM-YYYY');
        d._added_month = moment(d.added_on).format('MMM');
      });
      console.log(data);

      $scope.impressionData = _.reduce(data, function(result, value) {
        /*
        Reduce the impression data to generate reports, daily, monthly and like that.
         */
        (result.days[value._added_day]) ? result.days[value._added_day] += 1: result.days[value._added_day] = 1;
        (result.days_claimed[value._added_day]) ? result.days_claimed[value._added_day] += 1: result.days_claimed[value._added_day] = value.is_claimed;
        (result.days_redeemed[value._added_day]) ? result.days_redeemed[value._added_day] += 1: result.days_redeemed[value._added_day] = value.is_redeemed;

        (result.months[value._added_month]) ? result.months[value._added_month] += 1: result.months[value._added_month] = 1;

        (result.cities[value.city]) ? result.cities[value.city] += 1: result.cities[value.city] = 1;


        return result;
      }, {
        days: {},
        days_claimed: {},
        days_redeemed: {},
        months: {},
        cities: {}
      });

      console.log($scope.impressionData);

      var countData = _.reduce($scope.impressionData.days, function(result, count, key) {
        result.push([key, count]);
        return result;
      }, []);

      var claimedData = _.reduce($scope.impressionData.days_claimed, function(result, count, key) {
        result.push([key, count]);
        return result;
      }, []);

      var redeemData = _.reduce($scope.impressionData.days_redeemed, function(result, count, key) {
        result.push([key, count]);
        return result;
      }, []);

      $scope.options = {
        chart: {
          type: 'multiBarChart',
          clipEdge: true,
          height: 300,
          x: function(d) {
            return d[0];
          },
          y: function(d) {
            return d[1];
          },
          showValues: true,
          duration: 300,
          xAxis: {
            axisLabel: 'Dates'
          },
          yAxis: {
            axisLabel: 'Count',
            axisLabelDistance: -20,
            tickFormat: function(d) {
              return d3.format(',.0f')(d);
            }
          }
        }
      };

      console.log(countData);

      $scope.data = [{
        key: 'Displayed',
        values: countData
      }, {
        key: 'Interacted',
        values: claimedData
      }, {
        key: 'Sales',
        values: redeemData
      }];

    });
  });
