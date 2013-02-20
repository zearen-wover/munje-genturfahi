from pyparsing import *
ParserElement.enablePackrat()

operand = Group(OneOrMore(Regex('[0-9]'))).setName('operand')
operand.resultsName = 'operand'
operator = Group(Literal('+') | Literal('-') | Literal('*') | Literal('/')).setName('operator')
operator.resultsName = 'operator'

rpn = Forward().setName('rpn')
rpn.resultsName = 'rpn'

rpn << Group(operand + ZeroOrMore(OneOrMore(Literal(',')) + rpn + operator))

