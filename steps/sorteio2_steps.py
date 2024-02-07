from behave import when,then
from nose.tools import assert_equal
from random import randint


@when(u'sorteio o primeiro número de {num1} a {num2}')
def step_impl(context, num1, num2):
    context.res1 = randint(int(num1), int(num2))


@when(u'outro número de {num1} a {num2}')
def step_impl(context, num1, num2):
    context.res2 = randint(int(num1), int(num2))


@then(u'verifico se o primeiro resultado é igual a {res1}')
def step_impl(context, res1):
    assert_equal(context.res1, int(res1))


@then(u'o segundo é igual {res2}')
def step_impl(context, res2):
    assert_equal(context.res2, int(res2))
