import aristotle_mdr as aristotle
import comet
from django.views.generic import TemplateView

def indicator(*args,**kwargs):
    return aristotle.views.render_if_user_can_view(comet.models.Indicator,*args,**kwargs)

def datasource(*args,**kwargs):
    return aristotle.views.render_if_user_can_view(comet.models.DataSource,*args,**kwargs)

def qualitystatement(*args,**kwargs):
    return aristotle.views.render_if_user_can_view(comet.models.QualityStatement,*args,**kwargs)

class DynamicTemplateView(TemplateView):
    def get_template_names(self):
        return ['comet/static/%s.html' % self.kwargs['template']]
