from django.shortcuts import render

from django.views.generic.base import TemplateView

from .models import CircleShape, Cone, Cube, Cylinder, Parallelepiped, Pyramid, RectangleShape, Rhombus, Shape, Sphere, \
    Square, Trapezoid, Triangle
from .forms import TrapezoidForm, TriangleForm, RhombusForm, ShapeOneSideForm, ShapeTwoSideForm, ShapeThreeSideForm


class SquareView(TemplateView):
    template_name = 'square.html'
    form = ShapeOneSideForm
    a = None

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            self.a = form.cleaned_data['a']
            context = self.get_context_data()
            return super().render_to_response(context)
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.a:
            square = Square(a=self.a)
            fig = square.draw_shape()
            context['square'] = square
            context['uri'] = Shape.get_png(fig)

        context['form'] = self.form

        return context


class RectangleView(SquareView):
    template_name = 'rectangle.html'
    form = ShapeTwoSideForm
    b = None

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            self.b = form.cleaned_data['b']
        return super().post(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.a:
            rectangle = RectangleShape(a=self.a, b=self.b)
            fig = rectangle.draw_shape()
            context['uri'] = Shape.get_png(fig)
            context['rectangle'] = rectangle
        context['form'] = self.form

        return context


class CircleView(SquareView):
    template_name = 'circle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.a:
            circle = CircleShape(a=self.a)
            fig = circle.draw_shape()
            context['uri'] = Shape.get_png(fig)
            context['circle'] = circle
        context['form'] = self.form

        return context


class RhombusView(RectangleView):
    template_name = 'rhombus.html'
    form = RhombusForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.a:
            rhombus = Rhombus(a=self.a, b=self.b)
            fig = rhombus.draw_shape()
            context['uri'] = Shape.get_png(fig)
            context['rhombus'] = rhombus
        context['form'] = self.form

        return context


class TriangleView(RectangleView):
    template_name = 'triangle.html'
    form = TriangleForm
    c = None

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            self.c = form.cleaned_data['c']
        return super().post(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.a:
            triangle = Triangle(a=self.a, b=self.b, c=self.c)
            fig = triangle.draw_shape()

            context['uri'] = Shape.get_png(fig)
            context['triangle'] = triangle
        context['form'] = self.form

        return context


class TrapezoidView(TriangleView):
    template_name = 'trapezoid.html'
    form = TrapezoidForm
    d = None

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            self.d = form.cleaned_data['d']
        return super().post(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.a:
            trapezoid = Trapezoid(a=self.a, b=self.b, c=self.c, d=self.d)
            fig = trapezoid.draw_shape()
            context['uri'] = Shape.get_png(fig)
            context['trapezoid'] = trapezoid

        context['form'] = self.form

        return context


class SphereView(SquareView):
    template_name = 'sphere.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.a:
            sphere = Sphere(a=self.a)
            fig = sphere.draw_shape()
            context['uri'] = Shape.get_png(fig)

            context['sphere'] = sphere

        context['form'] = self.form

        return context


class CubeView(SquareView):
    template_name = 'cube.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.a:
            cube = Cube(a=self.a)
            fig = cube.draw_shape()
            context['uri'] = Shape.get_png(fig)

            context['cube'] = cube

        context['form'] = self.form

        return context


class CylinderView(RectangleView):
    template_name = 'cylinder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.a:
            cylinder = Cylinder(a=self.a, b=self.b)
            fig = cylinder.draw_shape()

            context['uri'] = Shape.get_png(fig)

            context['cylinder'] = cylinder

        context['form'] = self.form

        return context


class ParallelepipedView(TriangleView):
    template_name = 'parallelepiped.html'
    form = ShapeThreeSideForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.a:
            parallelepiped = Parallelepiped(a=self.a, b=self.b, c=self.c)

            fig = parallelepiped.draw_shape()

            context['uri'] = Shape.get_png(fig)

            context['parallelepiped'] = parallelepiped

        context['form'] = self.form

        return context


class PyramidView(ParallelepipedView):
    template_name = 'pyramid.html'
    form = ShapeThreeSideForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.a:
            pyramid = Pyramid(a=self.a, b=self.b, c=self.c)
            fig = pyramid.draw_shape()

            context['pyramid'] = pyramid

            context['uri'] = pyramid.get_png(fig)
        context['form'] = self.form

        return context


class ConeView(CylinderView):
    template_name = 'cone.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.a:
            cone = Cone(a=self.a, b=self.b)
            fig = cone.draw_shape()
            context['uri'] = Shape.get_png(fig)
            context['cone'] = cone

        context['form'] = self.form

        return context