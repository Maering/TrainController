from setuptools import setup, find_packages

setup(
   name='src',
   version='1.0',
   description='A useful module for controlling rc trains',
   author='Segan Salomon',
   author_email='segan.salomon@he-arc.ch',
   packages=['src'],  #same as name
   install_requires=['bitarray'], #external packages as dependencies
   scripts=[
            'src/IO/serialHandler.py',
            'src/Orders/orders.py',
            'src/Tests/test_orders.py',
            'src/Tests/test_trains.py',
            'src/Trains/train.py',
            'src/trainController.py',
            'src/main.py',
           ]
)