Feature:  Xinqi draw features
  As a person who believes in fate & fortune,
  I want to figure out if it is xinqi, given a input number


  Scenario Outline: Xinqi Draw API Query
    When the Xinqi Draw API is queried with <number>
    Then the response status code is 200
    And the response shows <result>

    Examples: draws
      | number   | result                       |
      | 1        | Oh you are not xinqi         |
      | 2        | Geez you are extremely xinqi |
      | 3        | Please try one more time     |
      | 4        | Please try one more time     |
