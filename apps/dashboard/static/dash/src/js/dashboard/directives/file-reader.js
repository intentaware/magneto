'use strict';

angular.module('adomattic.dashboard')
  .directive('readFile', function($q, urls) {
    return {
      restrict: 'E',
      scope: {
        label: '@',
        accept: '@',
      },
      templateUrl: urls.partials.directives + 'file-reader.html',
      replace: true,
      require: '?ngModel',
      link: function(scope, elm, atr, ngModel) {
        var $file = elm[0].querySelector('.overlay');
        console.log($file);

        $file.onchange = function (e) {
          var el = e.target;
          console.log(el.value);

          if (!el.value) {
            return
          }

          console.log(scope);
          scope.fileName = el.value;
          //scope.apply();
        }
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
