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
      console.log(response);
      self.columns = response.columns;
      self.data = response.data;
    });
});
