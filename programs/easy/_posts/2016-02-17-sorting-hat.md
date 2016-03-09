---

title: micro:bit Sorting Hat
layout: project

# excerpt for teaser links and Google descriptions
excerpt: "Use Python to code a Harry Potter sorting hat."

# exact sizes to match your project. PNG or JPG.
# File name matches project title eg. 2014-11-29-feature-building-a-score-counter.png
# Resides in /images/ folder
image:
  feature: 2016-02-17-sorting-hat-feature.svg
  teaser:  2016-02-17-sorting-hat-teaser.gif

# edit /data/author.yml with your details for info box. Please consider attributing your contribution to inspire kids.
# the author box contains links to twitter/websites etc

# Add only if project is updated after publication. 2016-12-25
modified:

share: true
author: jez_dean
comments: yes

---

This program displays a random string when button_a is pressed on the micro:bit.

{% highlight python %}
{% include_relative 2016-02-17-sorting-hat.py %}
{% endhighlight %}


### How it Works

#### Create a List of Hogwarts Houses

The names are loaded into a list. In the example above the list is created over 5 lines making it easier to read. A list can be created on one line too:

{% highlight python %}
HOUSES   = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff",]
{% endhighlight %}

A list contains "objects" (the Python way to say "whatsists", "thingamabobs" or "doodahs"). An object can be any type of thing. In this example the objects are _strings_ (of characters) so the value is surrounded by quotation marks like this: `"`Gryffindor`"`.

#### random.choice(HOUSES)

When `button_a` is pressed, the micro:bit's display scrolls a random house (or in code: `display.scroll(random.choice(HOUSES))`). It uses the `random.choice` method to randomly choose an object in the `HOUSES` list. How simple is that?

`random.choice` requires the `random` module. This is not included by defaults so we need to import it:

{% highlight python %}
import microbit from *
import random
{% endhighlight %}


### What to `import` and when

So when should you import modules? It's very simple to understand. You will only ever need to import 3 other modules: neopixel, random and music:

`import neopixel`: Import this to connect to a neopixel. These strips of colourful lights make it easy to create digital art and Christmas decorations.

`import random`: Import this to use random numbers. Anything beginning `random.` needs this module.

`import music`: Import this to  make a sound on your micro:bit. Anything beginning `music.` will need this module.

**RULE**: you only need to `import` a module if your code needs random numbers, makes a sound or uses a neopixel. Most of the time you will
just use `import microbit from *`
{: .notice-info}


### What is `sleep(100)`?

`while True:` puts the micro:bit into an infinite loop. This means the micro:bit repeats the program's loop as fast as it can. The program runs so fast that the processor cannot keep up and the micro:bit crashes.

`sleep(100)` makes the processor do nothing for 100 milliseconds (or .1 of a second). This slows down the program so the processor can keep up. The processor in your micro:bit is so fast that `microbit.sleep(1)` is enough of a wait.

Computer or phone crashes are often caused by badly written code that creates an infinite loop!
