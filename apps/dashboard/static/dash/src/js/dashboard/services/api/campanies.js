'use strict';

angular.module('adomattic.dashboard')
  .factory('Company', function($resource, urls) {
    return $resource(
      urls.apiBaseUrl + 'companies/companies/:id:doc/:list/',
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
