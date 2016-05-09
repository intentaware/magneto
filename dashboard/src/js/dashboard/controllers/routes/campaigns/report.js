'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignReportCtrl', function($routeParams, Reporter) {
    var self = this;

    var urlParams = {
      app: 'campaigns',
      endPoint: 'campaigns',
      id: $routeParams.campaignID
    };

    Reporter.datatable(urlParams).$promise.then(function(response) {
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

      self.data = [];
      self.response = response.data;
      self.options.paging.count = response.data.length;

      self.paging = function(offset, size) {
        var set = self.response.splice(offset, size);

        _.forEach(set, function(value, key) {
          var index = key + offset * size;

          self.data[index] = value;
        });
      };
    });

    self.periodOptions = [];

    _.forEach(_.range(1, 13), function(val) {
      self.periodOptions.push({
        name: val + 'months',
        val: val
      });
    });
  });