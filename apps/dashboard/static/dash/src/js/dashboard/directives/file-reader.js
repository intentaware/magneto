'use strict';

angular.module('adomattic.dashboard')
  .directive('readFile', function($q, urls) {
    return {
      restrict: 'E',
      scope: {
        label: '@',
        accept: '@',
        ngModel: '=',
      },
      templateUrl: urls.partials.directives + 'file-reader.html',
      replace: true,
      require: '^ngModel',
      link: function(scope, elm, atr, ngModelCtrl) {
        ngModelCtrl.$render = function() {};
        //scope.fileName = '';
        var $file = elm[0].querySelector('.overlay');
        console.log($file);

        // watch for a new file in input
        $file.onchange = function (e) {
          var el = e.target;
          console.log(el.value);

          if (!el.value) {
            return
          }

          console.log(scope);
          console.log(el.files);
          //scope.apply();
          //
          var name = el.files[0].name;

          $q.all(Array.prototype.slice.call(el.files, 0).map(read))
            .then(function(vals) {
              scope.fileName = name;
              ngModelCtrl.$setViewValue(vals.length ? vals[0] : null)
            }, function() {
              scope.fileName = 'Unable to load file, please try again';
              scope.$apply();
            });
        };

        // return the file contents in base64 format
        var read = function (f) {
          console.log(f);
          var d = $q.defer();
          var r = new FileReader();

          r.onload = function(ev) {
            d.resolve(ev.target.result);
          }

          r.onerror = function(ev) {
            d.reject(ev);
          }

          r.readAsDataURL(f);

          return d.promise;
        };
        /*
        var bindElement = function() {
          ngModel.$render = function() {};

          elm.bind('change', function(e) {
            var el = e.target;

            if (!el.value) {
              return;
            }

            var read = function(f) {
              var d = $q.defer();
              var r = new FileReader();

              r.onload = function(ev) {
                d.resolve(ev.target.result);
              };

              r.onerror = function(ev) {
                d.reject(ev);
              };

              r.readAsDataURL(f);

              return d.promise;
            };

            el.disabled = true;

            console.log(e);

            $q.all(Array.prototype.slice.call(el.files, 0).map(read))
              .then(function(values) {
                (el.multiple) ? ngModel.$setViewValue(values): ngModel.$setViewValue(values.length ? values[0] : null);
                el.disabled = false;
              });
          });
        };

        return (ngModel) ? bindElement() : false;
        */
      }
    };
  });
