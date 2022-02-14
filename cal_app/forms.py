from django import forms



class ShapeOneSideForm(forms.Form):
    a = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control input-w'}))

    def clean(self):
        cleaned_data = super().clean()
        a = cleaned_data.get('a')
        if a is None or a <= 0:
            self.add_error('a', "Не корректное значение")

        return cleaned_data


class ShapeTwoSideForm(ShapeOneSideForm):
    b = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control input-w'}))

    def clean(self):
        cleaned_data = super().clean()
        b = cleaned_data.get('b')
        if b is None or b <= 0:
            self.add_error('b', "Не корректные значения")

        return cleaned_data


class RhombusForm(ShapeTwoSideForm):

    def clean(self):
        cleaned_data = super().clean()
        a = cleaned_data.get('a')
        b = cleaned_data.get('b')

        if a is None or a <= 0 or b is None or b <= 0 or a <= b:
            self.add_error('a', "Не корректные значения")

        return cleaned_data


class ShapeThreeSideForm(ShapeTwoSideForm):
    c = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control input-w'}))

    def clean(self):
        cleaned_data = super().clean()
        c = cleaned_data.get('c')
        if c is None or c <= 0:
            self.add_error('c', "Не корректные значения")

        return cleaned_data


class TriangleForm(ShapeThreeSideForm):

    def clean(self):
        cleaned_data = super().clean()
        a = cleaned_data.get('a')
        b = cleaned_data.get('b')
        c = cleaned_data.get('c')

        if a is None or a <= 0 or b is None or b <= 0 or c is None or c <= 0 or a + b <= c or a + c <= b or c + b <= a:
            self.add_error('a', "Не корректные значения")

        return cleaned_data


class TrapezoidForm(TriangleForm):
    d = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control input-w'}))

    def clean(self):
        cleaned_data = super().clean()
        a = cleaned_data.get('a')
        b = cleaned_data.get('b')
        c = cleaned_data.get('c')
        d = cleaned_data.get('d')

        if a is None or a <= 0 or b is None or b <= 0 or c is None or c <= 0 or d is None or d <= 0 or a == b == c == d or a + b + d <= c or a + c + d <= b or c + b + d <= a or c + b + a <= d or b >= d:
            self.add_error('a', "Не корректные значения")

        return cleaned_data


class PyramidForm(ShapeThreeSideForm):

    def clean(self):
        cleaned_data = super().clean()
        a = cleaned_data.get('a')
        b = cleaned_data.get('b')
        c = cleaned_data.get('c')

        if a is None or a <= 0 or b is None or b <= 0 or c is None or c <= 0 or b <= 2 or a >= c:
            self.add_error('a', "Не корректные значения")

        return cleaned_data

