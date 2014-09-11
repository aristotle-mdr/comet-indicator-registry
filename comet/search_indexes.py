from haystack import indexes

from aristotle_mdr.search_indexes import baseObjectIndex, managedObjectIndex

import models

class IndicatorIndex(managedObjectIndex, indexes.Indexable):
    def get_model(self):
        return models.Indicator

class QualityStatement(managedObjectIndex, indexes.Indexable):
    def get_model(self):
        return models.QualityStatement

class IndicatorSet(managedObjectIndex, indexes.Indexable):
    def get_model(self):
        return models.IndicatorSet

class OutcomeArea(managedObjectIndex, indexes.Indexable):
    def get_model(self):
        return models.OutcomeArea

class DataSource(managedObjectIndex, indexes.Indexable):
    def get_model(self):
        return models.DataSource

