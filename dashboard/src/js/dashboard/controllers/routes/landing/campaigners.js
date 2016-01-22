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
      id: 10
    }).$promise.then(function(data) {
      console.log(data);
      data.map(function(d) {
        d._added_day = moment(d.added_on).format('DD-MMM-YYYY');
        d._added_month = moment(d.added_on).format('MMM');
      });

      var parser = new UAParser();

      var setInfo = function(parser, ua, obj) {

        var info = parser.setUA(ua).getResult();

        console.log(info);

        (obj.devices.os[info.os.name]) ? obj.devices.os[info.os.name] ++ : obj.devices.os[info.os.name] = 1;

        (obj.devices.browser[info.browser.name]) ? obj.devices.browser[info.browser.name] ++ : obj.devices.browser[info.browser.name] = 1;

        if (info.device.type) {
          (obj.devices.device[info.device.type]) ? obj.devices.device[info.device.type] ++ : obj.devices.device[info.device.type] = 1;
        } else {
          (obj.devices.device['system-x86']) ? obj.devices.device['system-x86'] ++ : obj.devices.device['system-x86'] = 1;
        }

      };

      $scope.impressionData = _.reduce(data, function(result, value, inx) {
        console.log(inx);
        /*
        Reduce the impression data to generate reports, daily, monthly and like that.
         */
        (result.days[value._added_day]) ? result.days[value._added_day] += 1: result.days[value._added_day] = 1;
        (result.days_claimed[value._added_day]) ? result.days_claimed[value._added_day] += 1: result.days_claimed[value._added_day] = value.is_claimed;
        (result.days_redeemed[value._added_day]) ? result.days_redeemed[value._added_day] += 1: result.days_redeemed[value._added_day] = value.is_redeemed;

        (result.months[value._added_month]) ? result.months[value._added_month] += 1: result.months[value._added_month] = 1;

        (result.cities[value.city]) ? result.cities[value.city] += 1: result.cities[value.city] = 1;

        // if (value.navigator) {
        //   //console.log(value.navigator.userAgent);
        //   var sysInfo = parser.setUA(value.navigator.userAgent).getResult();
        //   (result.sysInfo.os[sysInfo.os.name]) ? (result.sysInfo.os[sysInfo.os.name]) += 1: (result.sysInfo.os[sysInfo.os.name]) = 1;
        //   (result.sysInfo.browser[sysInfo.browser.name]) ? (result.sysInfo.browser[sysInfo.browser.name]) += 1: (result.sysInfo.browser[sysInfo.browser.name]) = 1;
        //   (result.sysInfo.device[sysInfo.device.type]) ? (result.sysInfo.device[sysInfo.device.type]) += 1: (result.sysInfo.device[sysInfo.device.type]) = 1;
        // }

        if (result.countries[value.country]) {
          // Setting Country level data

          result.countries[value.country].count ++;

          if (value.navigator) {
              setInfo(parser, value.navigator.userAgent, result.countries[value.country]);
          }

          // Setting City Level Data
          if (result.countries[value.country].cities[value.city]) {
            // Adding count and seeting city level matrix
            result.countries[value.country].cities[value.city].count ++;


            // Setting Postal Code Level Data
            if (result.countries[value.country].cities[value.city].postal_codes[value.postal_code]) {
              // Adding if exists
              result.countries[value.country].cities[value.city].postal_codes[value.postal_code].count ++;
            } else {
              // Setting default count to 1
              result.countries[value.country].cities[value.city].postal_codes[value.postal_code] = { count: 1, devices: { os: {}, browser: {}, device: {} }};
            }

            if (value.navigator) {
              setInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city]);
              setInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city].postal_codes[value.postal_code]);
            }

          } else {
            // Settings the city level Data (if it does not exist)
            result.countries[value.country].cities[value.city] = { count: 1, devices: { os: {}, browser: {}, device: {} }, postal_codes: {}};
            result.countries[value.country].cities[value.city].postal_codes[value.postal_code] = { count: 1, devices: { os: {}, browser: {}, device: {} }};

            if (value.navigator) {

              setInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city]);
              setInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city].postal_codes[value.postal_code]);
            }
          }
        } else {
          result.countries[value.country] = { count: 1, devices: { os: {}, browser: {}, device: {} }, cities: {} };
          result.countries[value.country].cities[value.city] = { count: 1, devices: { os: {}, browser: {}, device: {} }, postal_codes: {}};
          result.countries[value.country].cities[value.city].postal_codes[value.postal_code] = { count: 1, devices: { os: {}, browser: {}, device: {} }};

          if (value.navigator) {
            setInfo(parser, value.navigator.userAgent, result.countries[value.country]);
            setInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city]);
            setInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city].postal_codes[value.postal_code]);
          }
        }

        return result;
      }, {
        days: {},
        days_claimed: {},
        days_redeemed: {},
        months: {},
        cities: {},
        countries: {
        },
        sysInfo: {
          os: {},
          browser: {},
          device: {},
        }
      });

      var desktop = $scope.impressionData.sysInfo.device['undefined'];

      delete $scope.impressionData.sysInfo.device['undefined'];

      $scope.impressionData.sysInfo.device.desktop = desktop;
      // console.log($scope.impressionData);

      // simplifying time data

      var countTimeData = _.reduce($scope.impressionData.days, function(result, count, key) {
        result.push([key, count]);
        return result;
      }, []);

      var claimedTimeData = _.reduce($scope.impressionData.days_claimed, function(result, count, key) {
        result.push([key, count]);
        return result;
      }, []);

      // var redeemTimeData = _.reduce($scope.impressionData.days_redeemed, function(result, count, key) {
      //   result.push([key, count]);
      //   return result;
      // }, []);

      var cityData = _.reduce($scope.impressionData.cities, function(result, count, key) {
        result.push([key, count]);
        return result;
      }, []);

      $scope.timeOptions = {
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

      $scope.timeData = [{
        key: 'Displayed',
        values: countTimeData
      }, {
        key: 'Interacted',
        values: claimedTimeData
      }];

      $scope.cityOptions = angular.copy($scope.timeOptions);
      $scope.cityOptions.chart.xAxis.axisLabel = 'City';

      $scope.cityData = [{
        key: 'Count',
        values: cityData
      }];

    });
  });
