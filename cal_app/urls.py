from django.urls import path
from django.views.generic import TemplateView

from cal_app.views import CircleView, ConeView, CubeView, CylinderView, ParallelepipedView, PyramidView, RectangleView, RhombusView, SphereView, SquareView, TrapezoidView, TriangleView


urlpatterns = [
    
    path('', TemplateView.as_view(template_name="index.html"), name='calculator'),
    path('square/', SquareView.as_view(), name='square'),
    path('rectangle/', RectangleView.as_view(), name='rectangle'),
    path('circle/', CircleView.as_view(), name='circle'),
    path('triangle/', TriangleView.as_view(), name='triangle'),
    path('trapezoid/',TrapezoidView.as_view(), name='trapezoid'),
    path('rhombus/', RhombusView.as_view(), name='rhombus'),
    path('cube/', CubeView.as_view(), name='cube'),
    path('sphere/', SphereView.as_view(), name='sphere'),
    path('cone/', ConeView.as_view(), name='cone'),
    path('cylinder/', CylinderView.as_view(), name='cylinder'),
    path('parallelepiped/', ParallelepipedView.as_view(), name='parallelepiped'),
    path('pyramid/', PyramidView.as_view(), name='pyramid'),

]
 
