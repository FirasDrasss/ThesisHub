from django.shortcuts import render
from .models import thesis_listings,institutes
from .forms import ThesisForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,)
# Create your views here.
class ListingsView(ListView):
    model = thesis_listings
    template_name = 'thesis_listings.html' 
    context_object_name = 'thesis_listings'
    ordering = ['-creation_date']

class ListingDetailView(DetailView):
    template_name='listing_detail.html'
    model = thesis_listings


class ListingCreateView( CreateView):
    template_name='listing_upload.html'
    model = thesis_listings
    form_class=ThesisForm
    success_url = reverse_lazy('listing_view')

    def form_valid(self, form):
        return super().form_valid(form)
    
def load_institutes(request):
    department_id = request.GET.get('department')
    institues = institutes.objects.filter(department_id=department_id).order_by('institute_name')
    return render(request, 'institues_dropdown_list_options.html', {'institues': institues})