import logging
from django.urls import reverse_lazy
from django.views import generic
from .forms import ReaderForm

logger = logging.getLogger(__name__)

class IndexView(generic.FormView):
    template_name = "index.html"
    form_class = ReaderForm
    success_url = reverse_lazy('reader:index')
    
    def form_valid(self, form):
        # logger.info(form.cleaned_data['license_type'])
        form.analyze()
        download_url = form.save()        
        # return super().form_valid(form)
        context = {
            'download_url': download_url,
            'form': form,
        }
        return self.render_to_response(context)
    
