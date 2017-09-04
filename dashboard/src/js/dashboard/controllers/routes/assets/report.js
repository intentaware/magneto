'use strict';

angular.module('adomattic.dashboard')
  .controller('AssetReportCtrl', function ($routeParams, Reporter, Helper) {
    var self = this;
    var urlParams = {
      app: 'guages',
      endPoint: 'assets',
      id: $routeParams.assetID
    };

    self.getData = function () {
      urlParams.period = self.periodOption;
      self.data = [];
      Reporter.datatable(urlParams).$promise.then(function (response) {
        self.options = {
          rowHeight: 30,
          headerHeight: 50,
          footerHeight: 50,
          scrollbarV: false,
          selectable: false,
          columns: response.columns,
          // columnMode: 'force',
          paging: {
            externalPaging: true,
            size: 12
          }
        };

        self.response = response.data;
        self.options.paging.count = response.data.length;

        self.paging = function (offset, size) {
          var set = self.response.splice(offset, size);

          _.forEach(set, function (value, key) {
            var index = key + offset * size;

            self.data[index] = value;
          });
        };
      });
    };

    self.periodOptions = [];
    self.periodOption = 1;

    _.forEach(_.range(1, 13), function (val) {
      self.periodOptions.push({
        name: val + ' months',
        val: val
      });
    });

    self.csv = function () {
      var URL = '/api/guages/assets/' + $routeParams.assetID + '/reports/csv/';
      var queryParams = Helper.jsonToURL({
        period: self.periodOption
      }, URL);

      return queryParams;
    };

    // init view
    self.getData();
  });
