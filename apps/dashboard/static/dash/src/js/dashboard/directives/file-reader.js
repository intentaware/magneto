'use strict';

angular.module('adomattic.dashboard')
  .directive('readFile', function($q) {
    return {
      restrict: 'A',
      require: '?ngModel',
      link: function (scope, elm, atr, ngModel) {
        console.log(scope);


        var bindElement = function () {
          ngModel.$render = function() {};

          elm.bind('change', function (e) {

            var el = e.target;

            if (!el.value) {
              return
            }

            var read = function (f) {
              console.log(f);
              var d = $q.defer();
              var r = new FileReader();

              r.onload = function (ev) {
                console.log(ev);
                d.resolve(ev.target.result);
              };

              r.onerror = function (ev) {
                console.log(ev);
                d.reject(ev);
              };

              r.readAsDataURL(f);

              return d.promise;
            };

            el.disabled = true;

            console.log(e);

            $q.all(Array.prototype.slice.call(el.files, 0).map(read))
              .then(function (values) {
                (el.multiple) ? ngModel.$setViewValue(values) : ngModel.$setViewValue(values.length ? values[0] : null);
                el.disabled = false;
              })
          });
        };

        return (ngModel) ? bindElement() : false;
      }
    };
  });
