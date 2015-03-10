from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.shortcuts import redirect


class LoginRequiredMixin(TemplateView):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class SetSessionData(TemplateView):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """
        Sets the data to set the company information inside the session
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = self.request.user
        if user and user.memberships.count() > 0:
            membership = user.memberships.get(is_default=True)
            request.session['company'] = membership.company.id

            if membership.is_owner or membership.is_superuser:
                request.session['superuser'] = True
            else:
                request.session['superuser'] = False

            return super(SetSessionData, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('/companies/create/')


class DashboardView(SetSessionData):

    def get_template_names(self):
        from django.conf import settings

        if settings.DEBUG:
            template = 'debug/__base.html'
        else:
            template = 'dist/__base.html'
        return [template]


class AngularPartials(LoginRequiredMixin):

    def get_template_names(self):
        from django.conf import settings

        if settings.DEBUG:
            base = 'debug/partials/'
        else:
            base = 'dist/partials/'

        template_name = base + self.kwargs['template_name']
        return [template_name]
