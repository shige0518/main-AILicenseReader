import logging
from django.urls import reverse_lazy
from django.views import generic
from .forms import ReaderForm
from .forms import SingleUploadForm

logger = logging.getLogger(__name__)

class IndexView(generic.FormView):
    template_name = "index.html"
    form_class = ReaderForm
    success_url = reverse_lazy('reader:index')
    
    def form_valid(self, form):
        # logger.info(form.cleaned_data['license_type'])
        form.analyze()
        return super().form_valid(form)    
    

    def form_valid(self, form):
        download_url = form.save()
        context = {
            'download_url': download_url,
            'form': form,
        }
        return self.render_to_response(context)
    
