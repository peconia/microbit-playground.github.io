---

title: Scrolling Bauble
layout: project

# excerpt for teaser links and Google descriptions
excerpt: "Two lines of code to make a bauble."

# exact sizes to match your project. PNG or JPG.
# File name matches project title eg. 2014-11-29-feature-building-a-score-counter.png
# Resides in /images/ folder
image:
  feature: 2016-02-17-christmas-bauble-feature.svg
  teaser:  2016-02-17-christmas-bauble-teaser.gif

# Add only if project is updated after publication. 2016-12-25
modified:

share: true
author: jez_dean
comments: yes
---



<figure class="pull-right">
  <img src="{{ site.baseurl }}/images/2016-02-17-christmas-bauble-teaser.gif" alt="Right">
  <figcaption>Image by <a href="https://github.com/geekfish">geekfish</a>.</figcaption>
</figure>


This simple program displays "ho! ho! ho!" on the micro:bit. Let's go through it line by line... there are only two lines!

{% highlight python %}
{% include_relative 2016-02-17-christmas-bauble.py %}
{% endhighlight %}


### How it Works

#### Import the microbit module

`from microbit import *`

This imports the microbit module into the program. `*` imports _everything_ in the module. Start all your programs with this.

#### Scroll the Text
`display.scroll("ho ho ho")`

Scrolls the text across the microbit's display. Everything inside the `"` is shown in the display.

### Reading the API

[The microbit API for the display module](http://microbit-micropython.readthedocs.org/en/latest/display.html) describes a `delay` parameter for the `scroll` function.

`display.scroll("ho ho ho", delay=500)` updates the display every 500 milliseconds (or half a second). It slows down the speed of the scrolling text.

The API documentation has information about every function. Try reading it when you're coding for ideas. It's not as scary as it looks!

### Going Further

This only scrolls the message once. Can you make it repeat?
