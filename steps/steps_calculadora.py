from behave import given, when, then
from teste1 import calculadora
from nose.tools import assert_equal



@given(u'que acesso a calculadora')
def step_impl(context):
    pass


@when(u'somo {num1} + {num2}')
def step_impl(context, num1, num2):
    context.res = int(num1) + int(num2)


@then(u'o resultado é {total}')
def step_impl(context, total):
    assert_equal(int(total), context.res)
