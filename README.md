* Microbit Python Playground is at https://microbit-playground.github.io
* All micro:bit programs can be [downloaded as a zip file](https://microbit-playground.github.io/build/microbit-playground-code.zip).

## About

micro:bit Python Playground publishes Python code for kids to hack and mash (and hopefully learn something about Python!)

This is the code used to generate the website. It uses Jekyll, a Ruby program, to turn markdown into beautiful pages.

## Contributing

Please (please! please!) send us Python code and a brief overview of how your program works. My enail is jez@geekteacher.co.uk.

##### Easy Way:

1. Document your code with `/template/code-template.md`
2. Take photographs of your code or project.
3. Email them to me at jez@geekteacher.co.uk.
4. _Optional:_ Send through your name, photograph, webiste/twitter and a brief bio. These will be used to make you very cool author bio box!


##### Geeky Way:

1. Clone the repo
2. Document your code with `/template/program-template.md` or `/template/code-template-bare.md`.
3. Copy your `.py` and `.md` files to `/code/easy/_posts/` or `../medium/...` or `.../ninja/...` depending on difficulty. Naming scheme is `2016-02-24-my-program.*`.
4. Edit `/template/code-template-header.svg`, add your project name with a text editor and save to `/images/`. It's just an `xml` file.
5. Copy any images to `/images/` with the same file name as your program, eg. `2016-02-24-my-code-1.jpg` and `2016-02-24-my-code-2.png`
6. Edit `authors.yml` in the `_data` directory with your personal information.
6. Pull request

## Running the Website on Localhost

##### Running & Install Jekyll

1. install bundler ruby gem: `gem install bundler`
2. install required gems: `bundler install`
3. serve the website locally with installed gems: `bundle exec jekyll`
4. visit `http://localhost:4000`

#### Running `gulp`

_Do not use gulp!_ it's very messy! Here are some instructions if you insist:

The website uses `gulp` to complete tasks for production. `Gulp` requires `node.js` to be installed.

* in main directory run `npm install`
** `gulp scripts` to minify & combine javascript
** `gulp zip` creates a zip file of all the programs.
** `grunt svg2png`to convert svgs to pngs. This is used to make PNGs for opengraph (pretty Twitter cards).

`gulp images` is meant to smush images but please do not use it. The script should use graphicsmagic instead of gifsicle to smush gifs.

## Notes

#### Production / Development Environment

* `\_config.yml` loads variables for the production environment (eg. `url: https://github...`)
* `\_plugins\set_development_environment.rb` loads variables for development environment (eg `url:localhost`)

Plugins are not loaded by GitHub pages so it defaults to using the plugin and loading the development environment on localhost.


#### Contributing

Please follow the instructions above to contribute code.

Changes to code or documentation either edit through the github interface or follow steps above.
