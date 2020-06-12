from wtforms import Form, FloatField, validators

class InputForm1(Form):
    x = FloatField(
        label='first number',
        validators=[validators.InputRequired()])
    y = FloatField(
        label='second number',
        validators=[validators.InputRequired()])


class InputForm2(Form):
    x = FloatField(
        label='first number',
        validators=[validators.InputRequired()])
    y = FloatField(
        label='GST', default=15.00,
        validators=[validators.InputRequired()])
