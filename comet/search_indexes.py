from haystack import indexes

from aristotle_mdr.search_indexes import conceptIndex

import models

class IndicatorIndex(conceptIndex, indexes.Indexable):
    def get_model(self):
        return models.Indicator

class QualityStatement(conceptIndex, indexes.Indexable):
    def get_model(self):
        return models.QualityStatement

class IndicatorSet(conceptIndex, indexes.Indexable):
    def get_model(self):
        return models.IndicatorSet

class OutcomeArea(conceptIndex, indexes.Indexable):
    def get_model(self):
        return models.OutcomeArea
