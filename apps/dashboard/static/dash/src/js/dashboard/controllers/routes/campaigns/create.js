'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignCreateCtrl', function($rootScope) {
    var self = this;
    $rootScope.$on('campaginFormUpdated', function(e, args){
      self.ad = args;
      //console.log(args);
    });
  });
