Feature:  Xinqi draw features
  As a person who want to make check Xinqi identity
  I want to figure out if the person is Xinqi, given a input id number


  Scenario Outline: Xinqi Draw API Query
    When the Xinqi Draw API is queried with <number>
    Then the response status code is 200
    And the response shows <result>

    Examples: draws
      | number | result                     |
      | 1      | Oh you are not Xinqi       |
      | 2      | Geez you are exactly Xinqi |
      | 3      | Please try one more time   |
      | 4      | Please try one more time   |
