'use strict';

angular.module('adomattic.dashboard')
  .factory('Invoice', function($resource, urls) {
    return $resource(
      urls.apiBaseUrl + 'finances/invoices/:id:list/:doc/',
      {
        id: '@id',
        doc: '@doc',
        list: '@list'
      }, {
        update: {
          method: 'PUT',
          isArray: false
        },
        charge: {
          method: 'POST',
          isArray: false,
          params: {
            doc: 'charge'
          }
        }
      }
    );
  });
