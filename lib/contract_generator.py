#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GYSC
# gyb_generator.py
#
# Created by Jeff Kereakoglow on 8/31/18.
# Copyright © 2018 AlexisDigital. All rights reserved.

import os
from swagger import Swagger

# http://petstore.swagger.io/v2/swagger.json
class ContractGenerator(object):
    def __init__(self, swagger):
        if type(swagger) is not Swagger:
            raise TypeError("Expected a Swagger object")

        self.swagger = swagger

    def generate(self):
        directory = "contracts"
        self.mkdir(directory)

        definitions = self.swagger.parse_definitions()

        for contract_name in definitions.keys():
            properties = definitions[contract_name]

            with open(directory + '/' + contract_name + ".swift", 'w') as contract:
                
                contract.write("struct " + contract_name + " {\n")

                for property_name in properties.keys():
                    property_type = properties[property_name]
                    contract.write("    let " + property_name + ": " + property_type + "\n")

                contract.write('}')

    def mkdir(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)

def main():
    try:
        swagger = Swagger("../temp/swagger.json")
        generator = ContractGenerator(swagger)

        generator.generate()

    except ValueError:
        # TODO: Report an error to the Shell script
        print("Failed to parse the JSON file")

if __name__ == "__main__":
    main()