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
      id: 11
    }).$promise.then(function(data) {
      data.map(function(d) {
        d._added_day = moment(d.added_on).format('DD-MMM-YYYY');
        d._added_month = moment(d.added_on).format('MMM');
      });

      var parser = new UAParser();

      $scope.impressionData = _.reduce(data, function(result, value) {
        /*
        Reduce the impression data to generate reports, daily, monthly and like that.
         */
        (result.days[value._added_day]) ? result.days[value._added_day] += 1: result.days[value._added_day] = 1;
        (result.days_claimed[value._added_day]) ? result.days_claimed[value._added_day] += 1: result.days_claimed[value._added_day] = value.is_claimed;
        (result.days_redeemed[value._added_day]) ? result.days_redeemed[value._added_day] += 1: result.days_redeemed[value._added_day] = value.is_redeemed;

        (result.months[value._added_month]) ? result.months[value._added_month] += 1: result.months[value._added_month] = 1;

        (result.cities[value.city]) ? result.cities[value.city] += 1: result.cities[value.city] = 1;

        if (value.navigator) {
          console.log(value.navigator.userAgent);
          var sysInfo = parser.setUA(value.navigator.userAgent).getResult();
          (result.sysInfo.os[sysInfo.os.name]) ? (result.sysInfo.os[sysInfo.os.name]) += 1: (result.sysInfo.os[sysInfo.os.name]) = 1;
          (result.sysInfo.browser[sysInfo.browser.name]) ? (result.sysInfo.browser[sysInfo.browser.name]) += 1: (result.sysInfo.browser[sysInfo.browser.name]) = 1;
          (result.sysInfo.device[sysInfo.device.type]) ? (result.sysInfo.device[sysInfo.device.type]) += 1: (result.sysInfo.device[sysInfo.device.type]) = 1;
        }

        return result;
      }, {
        days: {},
        days_claimed: {},
        days_redeemed: {},
        months: {},
        cities: {},
        sysInfo: {
          os: {},
          browser: {},
          device: {},
        }
      });

      var desktop = $scope.impressionData.sysInfo.device['undefined'];

      delete $scope.impressionData.sysInfo.device['undefined'];

      $scope.impressionData.sysInfo.device.desktop = desktop;
      console.log($scope.impressionData);

      // simplifying time data

      var countTimeData = _.reduce($scope.impressionData.days, function(result, count, key) {
        result.push([key, count]);
        return result;
      }, []);

      var claimedTimeData = _.reduce($scope.impressionData.days_claimed, function(result, count, key) {
        result.push([key, count]);
        return result;
      }, []);

      var redeemTimeData = _.reduce($scope.impressionData.days_redeemed, function(result, count, key) {
        result.push([key, count]);
        return result;
      }, []);

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
      }, {
        key: 'Sales',
        values: redeemTimeData
      }];

      $scope.cityOptions = angular.copy($scope.timeOptions);
      $scope.cityOptions.chart.xAxis.axisLabel = 'City';

      $scope.cityData = [{
        key: 'Cities',
        values: cityData
      }];

        $scope.incomeOptions = {
            chart: {
                type: 'sunburstChart',
                height: 450,
                color: d3.scale.category20c(),
                duration: 250
            }
        };

        $scope.incomeData = [{
            'name': 'Demographics',
            children: [
              {
                name: 'Vancouver',
                'children': [
                    {
                        'name': 'Income',
                        'children': [
                            {'name': '200K +', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '150K - 200K', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '100K - 150K', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '60K - 100K', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '> 60K', 'size': Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Education',
                        children: [
                            {name: 'No Educaiton', size: Math.floor((Math.random() * 1000) + 1)},
                            {name: 'High School', size: Math.floor((Math.random() * 1000) + 1)},
                            {name: 'Some School', size: Math.floor((Math.random() * 1000) + 1)},
                            {name: 'Bechelors', size: Math.floor((Math.random() * 10000) + 1)},
                            {name: 'Post Grad', size: Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Transport',
                        children: [
                          {name: 'Drives Alone', size: Math.floor((Math.random() * 10000) + 1)},
                          {name: 'Carpooled', size: Math.floor((Math.random() * 1000) + 1)},
                          {name: 'Public Transit', size: Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Marital Status',
                        children: [
                          {name: 'Single', size: Math.floor((Math.random() * 2000) + 1)},
                          {name: 'Married', size: Math.floor((Math.random() * 1000) + 1)},
                          {name: 'Divorced', size: Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Device Info',
                        children: [
                          {name: 'mobile', size: Math.floor((Math.random() * 2000) + 1)},
                          {name: 'tablet', size: Math.floor((Math.random() * 500) + 1)},
                          {name: 'desktop', size: Math.floor((Math.random() * 5000) + 1)}
                        ]
                    }
                ]
              },
              {
                name: 'Toronto',
                'children': [
                    {
                        'name': 'Income',
                        'children': [
                            {'name': '200K +', 'size': Math.floor((Math.random() * 6000) + 1)},
                            {'name': '150K - 200K', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '100K - 150K', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '60K - 100K', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '> 60K', 'size': Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Education',
                        children: [
                            {name: 'No Educaiton', size: Math.floor((Math.random() * 1000) + 1)},
                            {name: 'High School', size: Math.floor((Math.random() * 1000) + 1)},
                            {name: 'Some School', size: Math.floor((Math.random() * 1000) + 1)},
                            {name: 'Bechelors', size: Math.floor((Math.random() * 6000) + 1)},
                            {name: 'Post Grad', size: Math.floor((Math.random() * 2000) + 1)}
                        ]
                    }, {
                        name: 'Transport',
                        children: [
                          {name: 'Drives Alone', size: Math.floor((Math.random() * 6000) + 1)},
                          {name: 'Carpooled', size: Math.floor((Math.random() * 2000) + 1)},
                          {name: 'Public Transit', size: Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Marital Status',
                        children: [
                          {name: 'Single', size: Math.floor((Math.random() * 1000) + 1)},
                          {name: 'Married', size: Math.floor((Math.random() * 1000) + 1)},
                          {name: 'Divorced', size: Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Device Info',
                        children: [
                          {name: 'mobile', size: Math.floor((Math.random() * 2000) + 1)},
                          {name: 'tablet', size: Math.floor((Math.random() * 500) + 1)},
                          {name: 'desktop', size: Math.floor((Math.random() * 5000) + 1)}
                        ]
                    }
                ]
              },
              {
                name: 'Mississauga',
                'children': [
                    {
                        'name': 'Income',
                        'children': [
                            {'name': '200K +', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '150K - 200K', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '100K - 150K', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '60K - 100K', 'size': Math.floor((Math.random() * 1000) + 1)},
                            {'name': '> 60K', 'size': Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Education',
                        children: [
                            {name: 'No Educaiton', size: Math.floor((Math.random() * 1000) + 1)},
                            {name: 'High School', size: Math.floor((Math.random() * 1000) + 1)},
                            {name: 'Some School', size: Math.floor((Math.random() * 5000) + 1)},
                            {name: 'Bechelors', size: Math.floor((Math.random() * 6000) + 1)},
                            {name: 'Post Grad', size: Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Transport',
                        children: [
                          {name: 'Drives Alone', size: Math.floor((Math.random() * 1000) + 1)},
                          {name: 'Carpooled', size: Math.floor((Math.random() * 4000) + 1)},
                          {name: 'Public Transit', size: Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Marital Status',
                        children: [
                          {name: 'Single', size: Math.floor((Math.random() * 1000) + 1)},
                          {name: 'Married', size: Math.floor((Math.random() * 1000) + 1)},
                          {name: 'Divorced', size: Math.floor((Math.random() * 1000) + 1)}
                        ]
                    }, {
                        name: 'Device Info',
                        children: [
                          {name: 'mobile', size: Math.floor((Math.random() * 2000) + 1)},
                          {name: 'tablet', size: Math.floor((Math.random() * 500) + 1)},
                          {name: 'desktop', size: Math.floor((Math.random() * 5000) + 1)}
                        ]
                    }
                ]
              }
            ]
        }];

    });
  });
