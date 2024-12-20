from .generators import *



listOfQuestions = [
        ("Analytic geometry", AnalyticGeometryQuestionGenerator),
        ("Derivative", DerivativeQuestionGenerator),
        ("Fraction", FractionQuestionGenerator),
        ("Infinitive series", InfinitiveSeriesQuestionGenerator),
        ("Integral", IntegralQuestionGenerator),
        ("Kardinal numbers", KardinalNumberQuestionGenerator),
        ("Linear equation system", LinearEquationSystemQuestionGenerator),
        ("Matrix", MatrixQuestionGenerator),
        ("Ordinal numbers", OrdinalNumberQuestionGenerator),
        ("Set", SetQuestionGenerator),
        ("Regular language", RegularLanguageQuestionGenerator),
        ("Vector", VectorQuestionGenerator),
        ("Complex number", ComplexQuestionGenerator)
    ]
"""Seznam generátorů otázek. Každý generátor je dvojice, kde první prvek je název tématu a druhý prvek je generátor otázek.
"""
