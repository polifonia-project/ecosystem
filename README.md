# Polifonia Ecosystem

This project is under development. See
https://polifonia-project.github.io/ecosystem/ for the live version of this website. 

## Contributing

The website is built with [Jekyll](https://jekyllrb.com/) and hosted on [Github
pages](https://pages.github.com/). It means that one needs to write the code on
their machine in a git repository and then push it on Github. Then, Github will
render the content as browsable static pages (with CSS/JS).

### Packages

Jekyll is written in Ruby and Ruby packages are managed with `gem`. So, as [this
page](https://jekyllrb.com/docs/installation/) states, you will need to have
Ruby and Gem installed on your computer.

[Bundler](https://bundler.io/) is also a recommended gem (required?) to work
with Jekyll.

### How-to start working on the Ecosystem website

Install jekyll and bundler with:

```bash
gem install jekyll bundler
```

Then, clone the code from this website in a folder on your computer:
```bash
git clone git@github.com:polifonia-project/ecosystem.git
```
And update the submodules:
```bash
./update-submodules.sh
```

Go into the directory and run the following to grab the dependencies (it may be
rather long):

```bash
bundle install
```

Then, you should be able to run

```
bundle exec jekyll serve --config=_config.yml,_config-local.yml --livereload
```

to have Jekyll `serve` a version of this website (you don't need any other web
server such as Apache or Nginx). A small message should tell you the state of
the rendering process and then invite you to open
[http://127.0.0.1:4000/ecosystem/](http://127.0.0.1:4000/ecosystem/) in your computer.

You may leave this terminal open and start hacking the code with your tool of
choice, it will detect the changes and update automatically (a simple refresh of
the page in the browser is needed though).

After a satisfactory version is obtained, don't forget to commit (`git add <files>`, 
`git commit -m"<message>"`) your changes and push them on Github (`git push`), so that 
the world may see them. Obvisouly, try to not commit a broken version (ie: which does not 
compile with Jekyll).


