'use strict';

angular.module('adomattic.dashboard')
  .factory('Company', function($resource, urls) {
    return $resource(
      urls.apiBaseUrl + 'companies/companies/:id:list/:doc/',
      {
        id: '@id',
        doc: '@doc',
        list: '@list'
      }, {
        update: {
          method: 'PUT',
          isArray: false
        }
      }
    );
  });
