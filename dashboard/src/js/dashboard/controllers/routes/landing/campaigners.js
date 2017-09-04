'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignersLandingCtrl', function ($scope, $location, Campaign, Reporter) {
    var urlParamsCampaign = {
      app: 'campaigns',
      endPoint: 'campaigns'
    };

    $scope.activeCampaign = null;

    $scope.getCampaignReport = function (id) {
      var params = urlParamsCampaign;

      params.id = id;
      Reporter.useragents(params).$promise.then(function (d) {
        $scope.useragents = d;
      });

      Reporter.history(params).$promise.then(function (d) {
        $scope.history = [{
          key: 'History',
          values: d
        }];
      });
    };

    var init = function () {
      Campaign.query().$promise.then(function (data) {
        $scope.campaigns = data;
        if (data.length) {
          $scope.activeCampaign = data[0].id;
          $scope.getCampaignReport($scope.activeCampaign);
          // var params = urlParamsCampaign;

          // params.id = data[0].id;
          // $scope.activeCampaign = data[0].id;
          // console.log($scope.activeCampaign);

          // Reporter.useragents(params).$promise.then(function(d) {
          //   $scope.useragents = d;
          // });

          // Reporter.history(params).$promise.then(function(d) {
          //   $scope.history = [{
          //     key: 'History',
          //     values: d
          //   }];
          // });
        }
      });
    };

    // navigations
    $scope.gotoCampaignList = function () {
      $location.path('/campaigns/');
    };

    $scope.gotoCampaignReport = function (id) {
      $location.path('/campaigns/' + id + '/report/');
    };
    // various graph options
    $scope.historyOptions = {
      'chart': {
        'type': 'multiBarChart',
        'height': 300,
        'margin': {
          'top': 25,
          'right': 25,
          'bottom': 50,
          'left': 50
        },
        x: function (d) {
          return d.date;
        },
        y: function (d) {
          return d.count;
        },
        'clipEdge': true,
        'duration': 500,
        'stacked': true,
        'xAxis': {
          'axisLabel': 'Date',
          'rotateLabels': -30,
          'showMaxMin': false
        },
        'yAxis': {
          'axisLabel': 'Count',
          'axisLabelDistance': -20
        }
      }
    };

    init();
  });
