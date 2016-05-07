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
        rowHeight: 50,
        headerHeight: 50,
        footerHeight: false,
        scrollbarV: false,
        selectable: false,
        columns: response.columns,
      };
      self.data = response.data;
    });
  });
