Feature: Calculadora

  Scenario: testar soma
    Given que acesso a calculadora
    When somo 100 + 100
    Then o resultado é 200