'use strict';

angular.module('adomattic.dashboard')
  .service('City', function($q, $http, urls) {
    var self = this;
    self.lookupString = false;
    self.pending = false;
    self.results = [];
    self.recursiveCallback = null;

    self.search = function(lookupString) {
      var defer = $q.defer();

      // this makes sure that we stop all other callbacks
      self.recursiveCallback = function(ls) {
        if (typeof(self.recursiveCallback) === 'function') {
          clearTimeout(self.recursiveCallback);
        }

        setTimeout(function() {
          performSearch(ls);
        }, 2000);
      };

      var performSearch = function(ls) {
        if (ls.length > 2) {
          // first check if the lookup string is part of the previous string
          if (self.lookupString && ls.toLowerCase().indexOf(self.lookupString.toLowerCase()) > -1) {
            // check if the previous result is still pending
            // if yes, wait, otherwise apply filter on previous result
            if (self.pending) {
              self.recursiveCallback(ls);
            } else {
              defer.resolve(self.results.filter(function(city) {
                return (city.name_std.toLowerCase().indexOf(ls.toLowerCase()) > -1);
              }));
            }
          } else if (self.pending) {
            self.recursiveCallback(ls);
          } else {
            self.pending = true;
            self.lookupString = ls;

            var queryParams = {
              name: ls
            };
            // lookup from the server
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
