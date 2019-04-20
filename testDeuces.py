from treys import Card, Evaluator

h1 = [
	Card.new('Qc'),
	Card.new('9h')
]

h2 = [
	Card.new('Ac'),
	Card.new('7h')
]



evaluator = Evaluator()

evaluator.hand_summary([],[h1,h2])
