
from aristotle_mdr.perms import user_can_view, user_can_edit, user_in_workgroup, user_is_workgroup_manager, user_can_change_status
import aristotle_mdr.forms as MDRForms # Treble-one seven nine
import aristotle_mdr.models as MDR # Treble-one seven nine

import aristotle_mdr as aristotle
import comet
from django.views.generic import TemplateView

#def datasetspecification(*args,**kwargs):
#    return render_if_user_can_view(MDR.DataSetSpecification,*args,**kwargs)

def indicator(*args,**kwargs):
    return aristotle.views.render_if_user_can_view(comet.models.Indicator,*args,**kwargs)

def datasource(*args,**kwargs):
    return aristotle.views.render_if_user_can_view(comet.models.DataSource,*args,**kwargs)

def qualitystatement(*args,**kwargs):
    return aristotle.views.render_if_user_can_view(comet.models.QualityStatement,*args,**kwargs)

class DynamicTemplateView(TemplateView):
    def get_template_names(self):
        return ['comet/static/%s.html' % self.kwargs['template']]
