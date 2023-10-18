import os
import frontmatter
from schema import Schema, And, Use, Or, Optional, Forbidden, SchemaError
from datetime import datetime
from urllib.parse import urlparse
from reeco import Validator
import yaml

def validate_yml():
    VALIDATOR = Validator()
    report = {}
    for root, subFolders, files in os.walk('content'):
        for fi in files:
            with open(root + "/" + fi) as f:
                try:
                    annotations, content = frontmatter.parse(f.read())
                    if 'component-id' in annotations.keys() or 'container-id' in annotations.keys():
                        errors = []
                        try:
                            ## Start validation
                            if 'component-id' in annotations.keys():
                                ### Validate as component
                                errors = VALIDATOR.asComponent(annotations)
                            elif 'container-id' in annotations.keys():
                                ### Validate as container
                                errors = VALIDATOR.asContainer(annotations)
                            else:
                                # do nothing
                                print("neither a component nor a container")
                        except Exception as e:
                            errors.append(e)
                        if errors: # TODO print nicely
                            report[root + "/" + fi] = errors
                except Exception as e:
                    # Malformed YAML in Markdown
                    report[root + "/" + fi] = [e]
    asYaml = yaml.dump(report)
    with open("./_data/validation.yml", "w") as f :
        f.write(asYaml)
        f.close()

validate_yml()
