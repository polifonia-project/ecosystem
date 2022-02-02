local:
	bundle exec jekyll serve --config=_config.yml,_config-local.yml

raph:
	bundle exec jekyll serve --config=_config.yml,_config-raph.yml 

clean:
	rm _site/* -fr
