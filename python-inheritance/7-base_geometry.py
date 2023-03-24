#!/usr/bin/python3
'''Module class BaseGeometry'''


class BaseGeometry:
    '''Class BaseGeometry'''

   def area(self):
    '''Method not implemented'''
    raise Exception('area() is not implemented')

   def inter_validation(self, name, valve):
       '''Method validates valve and type'''
       if type(value) is not int:
           raise TypeError('{} must be an integer'.format(name))
       if valve <= 0:
           raise valveError('{} must be greater than 0'.format(name))
