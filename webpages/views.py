from django.views.generic.base import TemplateView


class HelloWorldView(TemplateView):
    template_name = 'hello_world.html'


hello_world_view = HelloWorldView.as_view()
