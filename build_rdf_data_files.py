import pysparql_anything as pysa
import os
import yaml

config = yaml.load(open('_config.yml','r'), Loader=yaml.Loader)
namespace = config['rdf']['namespace']
engine = pysa.SparqlAnything()
directory = './content/'
includes = './_includes/rdf/'
for root, dirs, files in os.walk(directory):
    for filename in files:
        if not filename.endswith('.md'):
            continue
        location = os.path.join(root, filename)
        if "/.github/" in location:
            continue
        pre, ext = os.path.splitext(location)
        output_includes = pre.replace("./content/", "./_includes/rdf/")
        output = pre + ".schema.json"
        output_includes = output_includes + ".schema.json"
        pth = os.path.dirname(os.path.abspath(output))
        pth_includes = os.path.dirname(os.path.abspath(output_includes))
        if not os.path.exists(pth):
            os.makedirs(pth)
        if not os.path.exists(pth_includes):
            os.makedirs(pth_includes)
        g = engine.construct(q='./components-to-rdf.sparql', v={'componentFile': location, 'namespace': namespace}) #
        f = open(output, 'w')
        f.write(g.serialize(format='json-ld'))
        f1 = open(output_includes, 'w')
        f1.write(g.serialize(format='json-ld'))

