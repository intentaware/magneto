'use strict';

angular.module('adomattic.dashboard')
  .service('City', function($q, $http, urls) {
    var self = this;
    self.lookupString = false;
    self.pending = false;
    self.results = [];

    self.search = function(lookupString) {
      var defer = $q.defer();

      var performSearch = function(ls) {
        if (ls.length > 2) {
          // first check if the lookup string is part of the previous string
          if (self.lookupString && ls.toLowerCase().indexOf(self.lookupString.toLowerCase()) > -1) {
            // check if the previous result is still pending
            // if yes, wait, otherwise apply filter on previous result
            if (self.pending) {
              setTimeout(function() {
                performSearch(ls);
              }, 2000);
            } else {
              defer.resolve(self.results.filter(function(city) {
                return (city.name_std.toLowerCase().indexOf(ls.toLowerCase()) > -1);
              }));
            }
          } else if (self.pending) {
            console.log(ls);
            console.log(self.lookupString);
            setTimeout(function() {
              performSearch(ls);
            }, 2000);

          } else {
            self.pending = true;
            self.lookupString = ls;

            var queryParams = {
              name: ls
            };

            $http({
              method: 'GET',
              url: urls.apiBaseUrl + 'cities/cities/',
              params: queryParams
            }).success(function(data) {
              defer.resolve(data);
              self.results = data;
              self.pending = false;
            }).error(function(err) {
              defer.reject(err);
              self.pending = false;
            });
          }
        } else {
          defer.reject('Lookup must be 3 or more characters.');
          self.pending = false;
        }
      };

      performSearch(lookupString);
      return defer.promise;
    };
  });
