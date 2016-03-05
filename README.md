* micro:bit Playground website is at https://microbit-playground.github.io
* All micro:bit programs can be [downloaded as a zip file](https://microbit-playground.github.io/build/microbit-playground-code.zip).

## About

micro:bit Playground publishes python code for kids to hack and mash (and hopefully learn something about python!)

This repo contains the code used to generate the website. It uses Jekyll, a ruby program, to turn markdown into beautiful pages.

## Contributing

Please (please! please!) send me your python code and a brief overview of how your program works. My email is jez@geekteacher.co.uk.

##### Easy Way:

1. Document your code with `/templates/program-template.md` [[download link]](https://raw.githubusercontent.com/microbit-playground/microbit-playground.github.io/master/templates/program-template.md)
2. Take photographs of your code or project.
3. Email them to me at jez@geekteacher.co.uk.
4. _Optional:_ Send through your name, photograph, webiste/twitter and a brief bio. These will be used to make you very cool author bio box!

##### Geeky Way:

1. `git clone git@github.com:microbit-playground/microbit-playground.github.io.git`
2. Document your code with `/templates/program-template.md` or `/templates/program-template-bare.md`.
3. Copy your `.py` and `.md` files to `/code/easy/_posts/` or `../medium/...` or `.../ninja/...` depending on difficulty. Naming scheme is `2016-02-24-my-program.*`.
4. Edit `/templates/code-template-header.svg`, add your project name with a text editor and save to `/images/`. It's just an `xml` file.
5. Copy any images to `/images/` with the same file name as your program, eg. `2016-02-24-my-code-1.jpg` and `2016-02-24-my-code-2.png`
6. Edit `authors.yml` in the `_data` directory with your personal information.
6. Pull request

## Running the Website on Localhost

##### Running & Install Jekyll

1. clone this repo
2. install bundler for ruby: `gem install bundler`
3. install required gems: `bundler install`
4. serve the website locally with installed gems: `bundle exec jekyll serve`
5. visit `http://localhost:4000`

The website loads javascript from a CDN. This helps the page load quickly (500ms!) but means the website looks... _retro_ without an internet connection.

##### Running `gulp`

_There's no need to run `gulp`_ it's very messy!

The website uses `gulp` to complete tasks for production. `gulp` requires `node.js` to be installed.

* in main directory run `npm install`
 * `gulp scripts` to minify & combine javascript
 * `gulp zip` creates a zip file of all the programs.
 * `gulp svg2png`to convert svgs to pngs. This is used to make PNGs for opengraph (pretty Twitter cards).

`gulp images` is meant to smush images but please do not use it. The script should use graphicsmagic instead of gifsicle to smush gifs.

##### Production / Development Environment

* `\_config.yml` loads variables for the production environment (eg. `url: https://github...`)
* `\_plugins\set_development_environment.rb` loads variables for development environment (eg. `url: http://localhost`)

Plugins are not loaded by GitHub pages so it defaults to using the plugin and loading the development environment on localhost.

## TODO

* More programs
* Use gulp to build images from src/
* ~~build pretty header images for opengraph (twitter cards/facebook etc)~~
* Style guide & fix typos
  * micro:bit / Microbit / microbit
  * python / Python
  * licence / license 
  * practice / practise
  * noun / verb
  * etc 

## Contributing

Instructions are above or on the [developers page](https://jezdean.github.io/developers/). Programs for beginners are especially welcome.

Changes to code or documentation can be made this way or through the Github interface.

Drop me an email if you have any ideas or want to get involved. 

Carry on being amazing!
