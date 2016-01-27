'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignersLandingCtrl', function($rootScope, $scope, $location, Campaign, Reporter) {
    var getCampaigns = function() {
      Campaign.query().$promise.then(function(data) {
        $scope.campaigns = data;
      });
    };

    $scope.gotoCampaignList = function() {
      $location.path('/campaigns/');
    };

    getCampaigns();

    $scope.impressionData = null;

    var map = L.mapbox.map('map')
      .setView([0, 0], 1)
      .addLayer(L.mapbox.tileLayer('mapbox.streets'));

    Campaign.impressions({
      id: 11
    }).$promise.then(function(data) {
      console.log(data);
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

        if (value.city) {
          (result.cities[value.city]) ? result.cities[value.city] += 1: result.cities[value.city] = 1;
        }

        // if (value.navigator) {
        //   //console.log(value.navigator.userAgent);
        //   var sysInfo = parser.setUA(value.navigator.userAgent).getResult();
        //   (result.sysInfo.os[sysInfo.os.name]) ? (result.sysInfo.os[sysInfo.os.name]) += 1: (result.sysInfo.os[sysInfo.os.name]) = 1;
        //   (result.sysInfo.browser[sysInfo.browser.name]) ? (result.sysInfo.browser[sysInfo.browser.name]) += 1: (result.sysInfo.browser[sysInfo.browser.name]) = 1;
        //   (result.sysInfo.device[sysInfo.device.type]) ? (result.sysInfo.device[sysInfo.device.type]) += 1: (result.sysInfo.device[sysInfo.device.type]) = 1;
        // }

        if (result.countries[value.country]) {
          // Setting Country level data

          result.countries[value.country].count++;

          if (value.navigator) {
            Reporter.setUserAgentInfo(parser, value.navigator.userAgent, result.countries[value.country]);
          }

          // Setting City Level Data
          if (result.countries[value.country].cities[value.city]) {
            // Adding count and seeting city level matrix
            result.countries[value.country].cities[value.city].count++;


            // Setting Postal Code Level Data
            if (result.countries[value.country].cities[value.city].postal_codes[value.postal_code]) {
              // Adding if exists
              result.countries[value.country].cities[value.city].postal_codes[value.postal_code].count++;
            } else {
              // Setting default count to 1
              result.countries[value.country].cities[value.city].postal_codes[value.postal_code] = {
                count: 1,
                devices: {
                  os: {},
                  browser: {},
                  device: {}
                }
              };
            }

            if (value.navigator) {
              Reporter.setUserAgentInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city]);
              Reporter.setUserAgentInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city].postal_codes[value.postal_code]);
            }

          } else {
            // Settings the city level Data (if it does not exist)
            result.countries[value.country].cities[value.city] = {
              count: 1,
              devices: {
                os: {},
                browser: {},
                device: {}
              },
              postal_codes: {}
            };
            result.countries[value.country].cities[value.city].postal_codes[value.postal_code] = {
              count: 1,
              devices: {
                os: {},
                browser: {},
                device: {}
              }
            };

            if (value.navigator) {

              Reporter.setUserAgentInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city]);
              Reporter.setUserAgentInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city].postal_codes[value.postal_code]);
            }
          }
        } else {
          result.countries[value.country] = {
            count: 1,
            devices: {
              os: {},
              browser: {},
              device: {}
            },
            cities: {}
          };
          result.countries[value.country].cities[value.city] = {
            count: 1,
            devices: {
              os: {},
              browser: {},
              device: {}
            },
            postal_codes: {}
          };
          result.countries[value.country].cities[value.city].postal_codes[value.postal_code] = {
            count: 1,
            devices: {
              os: {},
              browser: {},
              device: {}
            }
          };

          if (value.navigator) {
            Reporter.setUserAgentInfo(parser, value.navigator.userAgent, result.countries[value.country]);
            Reporter.setUserAgentInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city]);
            Reporter.setUserAgentInfo(parser, value.navigator.userAgent, result.countries[value.country].cities[value.city].postal_codes[value.postal_code]);
          }

          result.markers.push(value.marker);
        }

        return result;
      }, {
        days: {},
        days_claimed: {},
        days_redeemed: {},
        months: {},
        cities: {},
        countries: {},
        sysInfo: {
          os: {},
          browser: {},
          device: {},
        },
        markers: []
      });

      var desktop = $scope.impressionData.sysInfo.device['undefined'];

      delete $scope.impressionData.sysInfo.device['undefined'];

      $scope.impressionData.sysInfo.device.desktop = desktop;
      console.log($scope.impressionData);

      // Adding cluster of markers and settings bounds
      var markers = new L.MarkerClusterGroup();

      $scope.impressionData.markers.forEach(function(k) {
        var marker =  L.marker(new L.LatLng(k[0], k[1]), {
          'marker-color': '0044FF'
        });
        markers.addLayer(marker);
      });

      map.addLayer(markers);
      map.fitBounds(markers.getBounds());

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
      //
      $scope.starBurstOptions = {
        chart: {
          type: 'sunburstChart',
          height: 450,
          color: d3.scale.category20(),
          duration: 500
        }
      };

      var starBurst = _.reduce($scope.impressionData.countries, function(r, v, k) {
        //console.log(k);
        if (k && k !== 'null') {
          r.children.push({
            name: k,
            children: _.reduce(v.cities, function(rr, vv, kk) {
              if (kk && kk !== 'null') {
                rr.push({
                  name: kk,
                  children: _.reduce(vv.postal_codes, function(rrr, vvv, kkk) {
                    //console.log(vvv);

                    rrr.push({
                      name: kkk,
                      children: _.reduce(vvv.devices, function(rrrr, vvvv, kkkk) {
                        //console.log(kkkk);

                        if (kkkk && kkkk !== 'null') {
                          rrrr.push({
                            name: kkkk,
                            children: _.reduce(vvvv, function(rd, vd, kd) {
                              rd.push({
                                name: kd,
                                size: vd
                              });

                              //console.log(rd);

                              return rd;
                            }, [])
                          });
                        }

                        return rrrr;
                      }, [])
                    });

                    return rrr;
                  }, [])
                });
              }

              return rr;
            }, [])
          });
        }

        return r;
      }, {
        name: 'Breakdown',
        children: []
      });

      $scope.starBurst = [starBurst];
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
