import os
import frontmatter
from schema import Schema, And, Use, Or, Optional, Forbidden, SchemaError
from datetime import datetime
from urllib.parse import urlparse
from reeco import Validator

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

# TODO Allow applications to customise the mandatory schema elements (e.g. remote story, persona, etc...)
validators = [
    {Forbidden('id'): object}, # 'id' cannot be used as it clashes with Jekyll
    {'component-id': And(str, Use(str.lower))}, # TODO Check uniqueness
    {'name': str},
    {'description': str},
    {'type': str}, # TODO make enumerator and allow to customise types
    {'release-date': And(object)}, # TODO check date
    {'release-number': str},
    {'release-link': And(str, Use(uri_validator))},
    {'work-package': list},
    {'pilot': list},
    {'story': list},
    {'keywords': list},
    {'changelog': And(str, Use(uri_validator))},
    {'licence': str},
    {Optional('image'): And(str, Use(uri_validator))},
    {Optional('logo'): And(str, Use(uri_validator))},
    {Optional('demo'): And(Or(str, list), Use(uri_validator))},
    {Optional('links'): And(list, Use(uri_validator))},
    {Optional('running-instance'): And(str, Use(uri_validator))},
    {Optional('credits'): Or(str,list)},
    {Optional('related-components'): list}, # TODO test component-ids
    {Optional('bibliography'): list}, # TODO test?
]

def validate_yml():
    report = {}
    for root, subFolders, files in os.walk('content'):
        for fi in files:
            with open(root + "/" + fi) as f:
                try:
                    annotations, content = frontmatter.parse(f.read())
                    if 'component-id' in annotations.keys():
                        errors = []
                        for attribute in validators:
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

    if "GITHUB_OUTPUT" in os.environ :
        with open(os.environ["GITHUB_OUTPUT"], "a") as f :
            print("{0}={1}".format("report", report), file=f)

validate_yml()
