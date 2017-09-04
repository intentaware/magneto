'use strict';

angular.module('adomattic.dashboard')
  .controller('SettingsFormCtrl', function ($rootScope, $location, Company, Circle, Helper) {
    var self = this;
    self.company = $rootScope.globals.company;

    self.circles = [];

    // md-autocomplete settings
    self.getMatches = function (query, lookup) {
      var results = query ? lookup.filter(createFilterFor(query)) : [];
      // console.log(results);
      console.log(self.campaign);
      return results;
    };

    var createFilterFor = function (query) {
      var _q = isNaN(parseInt(query)) ? query.toLowerCase() : parseInt(query);
      // console.log(_q);
      return function (index) {
        // console.log(index.id);
        return (index.name.toLowerCase().indexOf(_q) === 0) || (index.id === _q);
      };
    };

    Circle.query().$promise.then(function (response) {
      self.circles = response;
      self.company.circles = Helper.toObjects(self.company.circles, self.circles);
      console.log(self.company);
    });

    self.updateSettings = function () {
      var company = _.clone(self.company);
      company.circles = Helper.toIDs(company.circles);
      Company.update(company).$promise.then(function () {
        $rootScope.company = company;
        $location.path('/');
      });
    };
  });
