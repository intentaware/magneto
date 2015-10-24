'use strict';

angular.module('adomattic.dashboard')
  .controller('SettingsFormCtrl', function($rootScope, $location, Company, Circle) {

    var self = this;
    self.company = $rootScope.globals.company;

    self.circles = [];

    Circle.query().$prome.then(function(response) {
      self.circles = response;
    });

    self.updateSettings = function () {
      console.log(self.company);
      Company.update(self.company).$promise.then(function (response) {
        console.log(response);
        $location.path('/');
      });
    };
  });
