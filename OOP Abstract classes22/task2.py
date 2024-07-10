
# Task 2: Create a Plugin System Using Abstract Classes
# Develop a simple plugin system using abstract classes. 
# Create an abstract class called Plugin with an abstract method run.
#  Create two concrete plugins, PluginA and PluginB, that inherit from Plugin 
# and implement the run method to perform different tasks. 
# Then, create a program that dynamically loads and runs these plugins. ?????????????
from abc import ABC, abstractmethod

class Plugin(ABC):
    
    @abstractmethod
    def run(self):
        pass

class PluginA(Plugin):
    def run(self):
        return "A"
    

class PluginB(Plugin):
    def run(self):
        return "B"
    
