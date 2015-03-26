#!/usr/bin/python

## @validate_dataset.py
#  This script performs validation on the svm data.
import json
import sys
from jsonschema.validators import Draft4Validator
from brain.schema.jsonschema_definition import jsonschema_dataset, jsonschema_dataset_id

## Class: Validate_Dataset, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py'
class Validate_Dataset(object):

    ## constructor: saves a subset of the passed-in form data
    def __init__(self, svm_data, svm_session=None):
        self.svm_data    = svm_data
        self.svm_session = svm_session
        self.list_error  = []

    ## validate_label: validate either the dependent variable (observation) label,
    #                  or the independent variable (feature) label.
    def validate_label(self):
        try:
            Draft4Validator(jsonschema_string()).validate(self.data)
        except Exception, error:
            self.list_error.append(str(error))
