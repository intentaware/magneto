'use strict';

angular.module('adomattic.dashboard')
  .factory('Reporter', function ($resource, urls) {
    return $resource(
      urls.apiBaseUrl + ':app/:endPoint/:id:list/reports/:doc/', {
        endPoint: '@endPoint',
        app: '@app',
        id: '@id',
        list: '@list',
        doc: '@doc'
      }, {
        useragents: {
          method: 'GET',
          params: {
            doc: 'useragents'
          }
        },
        history: {
          method: 'GET',
          isArray: true,
          params: {
            doc: 'history'
          }
        },
        datatable: {
          method: 'GET',
          params: {
            doc: 'datatable'
          }
        }
      }
    );
  });
